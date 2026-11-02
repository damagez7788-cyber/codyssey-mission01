#!/usr/bin/env python3
"""Observe exec and attach on a container made specifically for this test."""
import os,pty,select,subprocess,sys,time
name=sys.argv[1]
before=subprocess.check_output(['docker','inspect','--format','{{.State.Running}}',name],text=True).strip()
print('$ docker exec '+name+' bash -lc "echo EXEC_SHELL; exit"',flush=True)
subprocess.run(['docker','exec',name,'bash','-lc','echo EXEC_SHELL; exit'],check=True)
print('Main process still running after exec exit:',subprocess.check_output(['docker','inspect','--format','{{.State.Running}}',name],text=True).strip(),flush=True)
master,slave=pty.openpty()
proc=subprocess.Popen(['docker','attach',name],stdin=slave,stdout=slave,stderr=slave,start_new_session=True)
os.close(slave)
buf=bytearray()
try:
    time.sleep(.7)
    os.write(master,b'echo ATTACH_MAIN_SHELL\n')
    deadline=time.monotonic()+2
    while time.monotonic()<deadline:
        if select.select([master],[],[],.2)[0]:
            try:buf.extend(os.read(master,8192))
            except OSError:break
    os.write(master,b'\x10\x11')
    proc.wait(timeout=8)
finally:
    if proc.poll() is None:proc.terminate();proc.wait(timeout=5)
    os.close(master)
after=subprocess.check_output(['docker','inspect','--format','{{.State.Running}}',name],text=True).strip()
print('$ docker attach '+name+'; echo ATTACH_MAIN_SHELL; [Ctrl+P Ctrl+Q]')
print(buf.decode('utf-8',errors='replace'))
print('Main process running after detach:',after)
assert before=='true' and after=='true' and b'ATTACH_MAIN_SHELL' in buf
