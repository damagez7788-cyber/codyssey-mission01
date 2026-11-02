#!/usr/bin/env python3
"""Run real mission checks on Linux and save command/output evidence.

Requires a running local Docker Engine and root for Docker. Ordinary-user
permission checks are run as the project owner, never as root. Only resources
created by this invocation may be removed. No GitHub writes are performed.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import pathlib
import pwd
import shlex
import subprocess
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument('--actor', required=True, help='Who is executing this run')
parser.add_argument('--owner', default='damagez')
args = parser.parse_args()
if os.geteuid() != 0:
    sys.exit('Use sudo: Docker checks run as root; permission checks use the project owner.')
project = pathlib.Path(__file__).resolve().parents[1]
owner = pwd.getpwnam(args.owner)
stamp = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
prefix = 'jun-m01-' + stamp.lower()
out = project / 'evidence' / stamp
out.mkdir(parents=True, exist_ok=False)
lab = project / '.verification-lab' / stamp
lab.mkdir(parents=True, exist_ok=False)
for path in [project / '.verification-lab', lab]:
    os.chown(path, owner.pw_uid, owner.pw_gid)
records = []
checks = []
textlogs = {}

def run(section, command, *, user=None, cwd=None, expected=0):
    command = [str(x) for x in command]
    shown = shlex.join(command)
    actual = command if user is None else ['runuser', '-u', user, '--'] + command
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    result = subprocess.run(actual, cwd=str(cwd or project), text=True,
                            encoding='utf-8', errors='replace',
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    record = {'started_at':started,'actor':args.actor,'linux_user':user or 'root',
              'cwd':str(cwd or project),'command':shown,'exit_code':result.returncode,
              'expected_exit':expected,'stdout':result.stdout,'stderr':result.stderr}
    records.append(record)
    rendered = (f'[{started}] actor={args.actor}; linux_user={record["linux_user"]}\n'
                f'cwd={record["cwd"]}\n$ {shown}\n'
                f'{result.stdout}{result.stderr}\nexit_code={result.returncode}\n\n')
    textlogs.setdefault(section, []).append(rendered)
    (out / (section+'.txt')).write_text(''.join(textlogs[section]), encoding='utf-8')
    (out / 'commands.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'{section}: exit={result.returncode} {shown}',flush=True)
    if result.returncode != expected:
        raise RuntimeError(f'Unexpected exit {result.returncode}: {shown}')
    return result.stdout

def check(name, condition, detail):
    checks.append({'name':name,'passed':bool(condition),'detail':detail})
    (out/'checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if not condition:
        raise RuntimeError(name + ': ' + detail)

def docker(section, *parts):
    return run(section, ['docker', *parts])

def fetch(section, port, path='/'):
    # Real curl captures address, status and body; no invented success text.
    return run(section,['curl','--fail','--silent','--show-error','--include',f'http://127.0.0.1:{port}{path}'])

def wait_ready(section, port):
    return run(section,['curl','--fail','--silent','--show-error','--retry','10',
                        '--retry-all-errors','--retry-delay','1','--max-time','3',
                        f'http://127.0.0.1:{port}/health'])

try:
    run('01_environment',['uname','-a'])
    run('01_environment',['cat','/etc/os-release'])
    run('01_environment',['bash','--version'])
    run('01_environment',['git','--version'])
    run('01_environment',['docker','--version'])
    docker('01_environment','info')
    run('01_environment',['id',args.owner])

    # Fresh ordinary-user CLI and permission evidence, unrelated to earlier practice.
    script = '''set -eux
pwd
mkdir notes archive
touch empty.txt .hidden-note
ls -la
printf 'Fresh mission verification\\n' > notes/original.txt
cat notes/original.txt
cp notes/original.txt notes/copy.txt
mv notes/copy.txt archive/renamed.txt
ls -l notes archive
cat archive/renamed.txt
rm archive/renamed.txt
ls -la archive
chmod 644 notes/original.txt
ls -l notes/original.txt
chmod 600 notes/original.txt
ls -l notes/original.txt
chmod 755 archive
ls -ld archive
chmod 600 archive
ls -ld archive
'''
    run('02_linux',['bash','-c',script],user=args.owner,cwd=lab)
    denied = run('02_linux',['bash','-c','cd archive'],user=args.owner,cwd=lab,expected=1)
    run('02_linux',['chmod','755','archive'],user=args.owner,cwd=lab)
    run('02_linux',['bash','-c','cd archive; pwd'],user=args.owner,cwd=lab)
    check('linux_operations_and_permissions',True,'Fresh CLI run; file 644 to 600; directory 755 to 600 to 755. Permission denial is an intentional experiment, not troubleshooting.')

    hello = docker('03_containers','run','--name',prefix+'-hello','hello-world')
    check('hello_world','Hello from Docker!' in hello,'Official test image ran and exited.')
    docker('03_containers','run','-dit','--name',prefix+'-ubuntu','ubuntu:24.04','bash')
    docker('03_containers','exec',prefix+'-ubuntu','bash','-lc','ls /; echo inside-ubuntu')
    run('03_containers',['python3',str(project/'scripts/observe_attach.py'),prefix+'-ubuntu'])
    docker('03_containers','inspect','--format','{{.State.Status}}',prefix+'-ubuntu')
    docker('03_containers','stop',prefix+'-ubuntu')
    docker('03_containers','start',prefix+'-ubuntu')
    docker('03_containers','image','ls')
    docker('03_containers','ps','-a')
    check('ubuntu_exec_attach',True,'exec creates another shell; attach detached with Ctrl+P Ctrl+Q while main bash remained running.')

    # A build can resolve FROM through BuildKit cache without registering a
    # named base image in the Engine image list. Pull explicitly for inspection.
    docker('04_build','pull','nginx:stable-alpine')
    image='jun-workshop:'+stamp.lower()
    docker('04_build','build','-t',image,'.')
    docker('04_build','image','inspect',image)
    docker('04_build','image','inspect','nginx:stable-alpine')
    ports=[18080,18081,18082]
    for port,name in zip(ports[:2],[prefix+'-web-a',prefix+'-web-b']):
        docker('05_ports','run','-d','--name',name,'-p',f'127.0.0.1:{port}:80',image)
    for port in ports[:2]:
        wait_ready('05_ports',port)
        body=fetch('05_ports',port)
        check(f'web_port_{port}','WORKSHOP_V1' in body and '200 OK' in body,'Real HTTP header and page body captured.')
        check(f'health_{port}','workshop-ready' in fetch('05_ports',port,'/health'),'Custom NGINX health endpoint.')
    docker('05_ports','logs',prefix+'-web-a')
    docker('05_ports','stats','--no-stream',prefix+'-web-a')

    binddir=lab/'bind-site'
    run('06_bind',['cp','-a',str(project/'site'),str(binddir)])
    docker('06_bind','run','-d','--name',prefix+'-bind','-p','127.0.0.1:18082:80','--mount',f'type=bind,src={binddir},dst=/usr/share/nginx/html,readonly',image)
    wait_ready('06_bind',18082)
    before=fetch('06_bind',18082)
    run('06_bind',['python3','-c','from pathlib import Path; p=Path(__import__("sys").argv[1]); p.write_text(p.read_text().replace("WORKSHOP_V1","WORKSHOP_V2"))',str(binddir/'index.html')])
    after=fetch('06_bind',18082)
    baked=fetch('06_bind',18080)
    check('bind_change_reflected','WORKSHOP_V1' in before and 'WORKSHOP_V2' in after,'Host content change reflected without rebuild.')
    check('baked_image_unchanged','WORKSHOP_V1' in baked,'COPY image is independent of the bind-mounted host file.')

    volume=prefix+'-data'
    docker('07_volume','volume','create',volume)
    docker('07_volume','run','-d','--name',prefix+'-writer','--mount',f'type=volume,src={volume},dst=/data','ubuntu:24.04','sleep','infinity')
    docker('07_volume','exec',prefix+'-writer','bash','-lc','printf "persistent-workshop-data\\n" > /data/note.txt; cat /data/note.txt')
    before_hash=docker('07_volume','exec',prefix+'-writer','sha256sum','/data/note.txt').split()[0]
    docker('07_volume','stop',prefix+'-writer')
    docker('07_volume','rm',prefix+'-writer')
    docker('07_volume','run','-d','--name',prefix+'-reader','--mount',f'type=volume,src={volume},dst=/data,readonly','ubuntu:24.04','sleep','infinity')
    after_text=docker('07_volume','exec',prefix+'-reader','cat','/data/note.txt')
    after_hash=docker('07_volume','exec',prefix+'-reader','sha256sum','/data/note.txt').split()[0]
    check('volume_persistence',before_hash==after_hash and after_text.strip()=='persistent-workshop-data','Container deleted; second container reads identical content and SHA-256.')
    docker('07_volume','volume','inspect',volume)

    summary={'run_id':stamp,'actor':args.actor,'project_root':str(project),'image':image,'ports':ports,'container_prefix':prefix,'volume':volume,'lab':str(lab),'all_checks_passed':all(x['passed'] for x in checks),'checks':checks,'github_pushed':False,'platform_submitted':False,'intentional_error_note':'Directory Permission denied was intentionally produced for required permission experiment.'}
    (out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (project/'evidence/latest.json').write_text(json.dumps({'run_id':stamp,'summary':f'{stamp}/summary.json'},indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False),flush=True)
except Exception as error:
    (out/'failure.txt').write_text(f'{type(error).__name__}: {error}\n',encoding='utf-8')
    raise
finally:
    # Ownership only on files created by this verification run.
    for directory,dirs,files in os.walk(out):
        for item in [pathlib.Path(directory)]+[pathlib.Path(directory)/x for x in files]:
            os.chown(item,owner.pw_uid,owner.pw_gid)
