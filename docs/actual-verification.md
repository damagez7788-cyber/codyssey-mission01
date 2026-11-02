# 실제 검증 명령과 출력

실행 ID: 20261102T170206Z. 모든 블록은 원문 로그를 그대로 포함합니다. 시각은 UTC이며 한국 시간은 9시간을 더합니다. 실행 주체는 jarvis-assisted입니다.

## 실행 환경

```text
[2026-11-02T17:02:06.439274+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ uname -a
Linux DESKTOP-1K2JO3L 6.18.54.1-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC Tue Oct  6 19:13:07 UTC 2026 x86_64 GNU/Linux

exit_code=0

[2026-11-02T17:02:06.447311+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ cat /etc/os-release
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="26.04"
VERSION="26.04.1 LTS (Resolute Raccoon)"
VERSION_CODENAME=resolute
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=resolute
LOGO=ubuntu-logo

exit_code=0

[2026-11-02T17:02:06.454613+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ bash --version
GNU bash, version 5.3.9(1)-release (x86_64-pc-linux-gnu)
Copyright (C) 2025 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

exit_code=0

[2026-11-02T17:02:06.458794+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ git --version
git version 2.53.0

exit_code=0

[2026-11-02T17:02:06.464927+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker --version
Docker version 29.9.2, build a82e528

exit_code=0

[2026-11-02T17:02:06.960010+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker info
Client: Docker Engine - Community
 Version:    29.9.2
 Context:    default
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.38.1
    Path:     /usr/libexec/docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v5.7.0
    Path:     /usr/libexec/docker/cli-plugins/docker-compose

Server:
 Containers: 7
  Running: 2
  Paused: 0
  Stopped: 5
 Images: 5
 Server Version: 29.9.2
 Storage Driver: overlayfs
  driver-type: io.containerd.snapshotter.v1
 Logging Driver: json-file
 Cgroup Driver: systemd
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: b7a25261e029d68978bbf290df0a62fc819b3c51
 runc version: v1.5.2-0-g29dd3dc2
 init version: de40ad0
 Security Options:
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 6.18.54.1-microsoft-standard-WSL2
 Operating System: Ubuntu 26.04.1 LTS
 OSType: linux
 Architecture: x86_64
 CPUs: 8
 Total Memory: 7.535GiB
 Name: DESKTOP-1K2JO3L
 ID: d46f9f31-abd7-4640-9c29-0847570b087e
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Experimental: false
 Insecure Registries:
  127.0.0.0/8
  ::1/128
 Live Restore Enabled: false
 Firewall Backend: iptables
  EnableUserlandProxy: true
  UserlandProxyPath: /usr/bin/docker-proxy


exit_code=0

[2026-11-02T17:02:07.489386+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ id damagez
uid=1000(damagez) gid=1000(damagez) groups=1000(damagez),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),100(users)

exit_code=0
```

## CLI와 권한

```text
[2026-11-02T17:02:07.498980+00:00] actor=jarvis-assisted; linux_user=damagez
cwd=/home/damagez/codyssey-mission01/.verification-lab/20261102T170206Z
$ bash -c 'set -eux
pwd
mkdir notes archive
touch empty.txt .hidden-note
ls -la
printf '"'"'Fresh mission verification\n'"'"' > notes/original.txt
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
'
/home/damagez/codyssey-mission01/.verification-lab/20261102T170206Z
total 16
drwxr-xr-x 4 damagez damagez 4096 Nov  3 02:02 .
drwxr-xr-x 5 damagez damagez 4096 Nov  3 02:02 ..
-rw-r--r-- 1 damagez damagez    0 Nov  3 02:02 .hidden-note
drwxr-xr-x 2 damagez damagez 4096 Nov  3 02:02 archive
-rw-r--r-- 1 damagez damagez    0 Nov  3 02:02 empty.txt
drwxr-xr-x 2 damagez damagez 4096 Nov  3 02:02 notes
Fresh mission verification
archive:
total 4
-rw-r--r-- 1 damagez damagez 27 Nov  3 02:02 renamed.txt

notes:
total 4
-rw-r--r-- 1 damagez damagez 27 Nov  3 02:02 original.txt
Fresh mission verification
total 8
drwxr-xr-x 2 damagez damagez 4096 Nov  3 02:02 .
drwxr-xr-x 4 damagez damagez 4096 Nov  3 02:02 ..
-rw-r--r-- 1 damagez damagez 27 Nov  3 02:02 notes/original.txt
-rw------- 1 damagez damagez 27 Nov  3 02:02 notes/original.txt
drwxr-xr-x 2 damagez damagez 4096 Nov  3 02:02 archive
drw------- 2 damagez damagez 4096 Nov  3 02:02 archive
+ pwd
+ mkdir notes archive
+ touch empty.txt .hidden-note
+ ls -la
+ printf 'Fresh mission verification\n'
+ cat notes/original.txt
+ cp notes/original.txt notes/copy.txt
+ mv notes/copy.txt archive/renamed.txt
+ ls -l notes archive
+ cat archive/renamed.txt
+ rm archive/renamed.txt
+ ls -la archive
+ chmod 644 notes/original.txt
+ ls -l notes/original.txt
+ chmod 600 notes/original.txt
+ ls -l notes/original.txt
+ chmod 755 archive
+ ls -ld archive
+ chmod 600 archive
+ ls -ld archive

exit_code=0

[2026-11-02T17:02:07.628717+00:00] actor=jarvis-assisted; linux_user=damagez
cwd=/home/damagez/codyssey-mission01/.verification-lab/20261102T170206Z
$ bash -c 'cd archive'
bash: line 1: cd: archive: Permission denied

exit_code=1

[2026-11-02T17:02:07.642895+00:00] actor=jarvis-assisted; linux_user=damagez
cwd=/home/damagez/codyssey-mission01/.verification-lab/20261102T170206Z
$ chmod 755 archive

exit_code=0

[2026-11-02T17:02:07.662226+00:00] actor=jarvis-assisted; linux_user=damagez
cwd=/home/damagez/codyssey-mission01/.verification-lab/20261102T170206Z
$ bash -c 'cd archive; pwd'
/home/damagez/codyssey-mission01/.verification-lab/20261102T170206Z/archive

exit_code=0
```

## 컨테이너와 attach

```text
[2026-11-02T17:02:07.676703+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker run --name jun-m01-20261102t170206z-hello hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/


exit_code=0

[2026-11-02T17:02:08.820948+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker run -dit --name jun-m01-20261102t170206z-ubuntu ubuntu:24.04 bash
8d0963b469d17e0b5702d851d7b8c37b2d5a03b836b6570403d98f8d24afe30e

exit_code=0

[2026-11-02T17:02:09.737520+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker exec jun-m01-20261102t170206z-ubuntu bash -lc 'ls /; echo inside-ubuntu'
bin
boot
dev
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
inside-ubuntu

exit_code=0

[2026-11-02T17:02:10.277891+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ python3 /home/damagez/codyssey-mission01/scripts/observe_attach.py jun-m01-20261102t170206z-ubuntu
$ docker exec jun-m01-20261102t170206z-ubuntu bash -lc "echo EXEC_SHELL; exit"
EXEC_SHELL
Main process still running after exec exit: true
$ docker attach jun-m01-20261102t170206z-ubuntu; echo ATTACH_MAIN_SHELL; [Ctrl+P Ctrl+Q]

[K
]0;root@8d0963b469d1: /root@8d0963b469d1:/# echo ATTACH_MAIN_SHELL
[?2004l
ATTACH_MAIN_SHELL
[?2004h[K
Main process running after detach: true

exit_code=0

[2026-11-02T17:02:14.963083+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker inspect --format '{{.State.Status}}' jun-m01-20261102t170206z-ubuntu
running

exit_code=0

[2026-11-02T17:02:15.450848+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker stop jun-m01-20261102t170206z-ubuntu
jun-m01-20261102t170206z-ubuntu

exit_code=0

[2026-11-02T17:02:26.138303+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker start jun-m01-20261102t170206z-ubuntu
jun-m01-20261102t170206z-ubuntu

exit_code=0

[2026-11-02T17:02:26.852282+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker image ls
IMAGE                           ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-world:latest              c567b231f656       25.9kB         9.49kB   U    
jun-workshop:20261102t165758z   c1af4c4a1231       92.7MB         26.1MB   U    
jun-workshop:20261102t170027z   829d455949c6       92.7MB         26.1MB   U    
nginx:stable-alpine             0e52bd054126       93.5MB           27MB        
ubuntu:24.04                    fe81560990fa        119MB         31.7MB   U    

exit_code=0

[2026-11-02T17:02:27.883082+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker ps -a
CONTAINER ID   IMAGE                           COMMAND                  CREATED              STATUS                          PORTS     NAMES
8d0963b469d1   ubuntu:24.04                    "bash"                   19 seconds ago       Up 1 second                               jun-m01-20261102t170206z-ubuntu
08fb865c1c0e   hello-world                     "/hello"                 20 seconds ago       Exited (0) 19 seconds ago                 jun-m01-20261102t170206z-hello
8e77b04a090d   jun-workshop:20261102t170027z   "/docker-entrypoint.…"   About a minute ago   Exited (0) 39 seconds ago                 jun-m01-20261102t170027z-bind
50044163c04b   jun-workshop:20261102t170027z   "/docker-entrypoint.…"   About a minute ago   Exited (0) 39 seconds ago                 jun-m01-20261102t170027z-web-b
976a5a5f876a   jun-workshop:20261102t170027z   "/docker-entrypoint.…"   About a minute ago   Exited (0) 39 seconds ago                 jun-m01-20261102t170027z-web-a
4033cffd1288   ubuntu:24.04                    "bash"                   About a minute ago   Up About a minute                         jun-m01-20261102t170027z-ubuntu
d880b11c694e   hello-world                     "/hello"                 About a minute ago   Exited (0) About a minute ago             jun-m01-20261102t170027z-hello
2d949ff62f95   ubuntu:24.04                    "bash"                   4 minutes ago        Up 4 minutes                              jun-m01-20261102t165758z-ubuntu
7ebddd6ec08b   hello-world                     "/hello"                 4 minutes ago        Exited (0) 4 minutes ago                  jun-m01-20261102t165758z-hello

exit_code=0
```

## 이미지 제작

```text
[2026-11-02T17:02:28.469125+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker pull nginx:stable-alpine
stable-alpine: Pulling from library/nginx
Digest: sha256:0e52bd054126cdc040b1276c0af347aeb02a41b9cfe305d6094767ac30e97949
Status: Image is up to date for nginx:stable-alpine
docker.io/library/nginx:stable-alpine

exit_code=0

[2026-11-02T17:02:30.766991+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker build -t jun-workshop:20261102t170206z .
#0 building with "default" instance using docker driver

#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile: 334B done
#1 DONE 0.0s

#2 [internal] load metadata for docker.io/library/nginx:stable-alpine
#2 DONE 0.1s

#3 [internal] load .dockerignore
#3 transferring context: 105B done
#3 DONE 0.0s

#4 [internal] load build context
#4 transferring context: 190B done
#4 DONE 0.0s

#5 [1/3] FROM docker.io/library/nginx:stable-alpine@sha256:0e52bd054126cdc040b1276c0af347aeb02a41b9cfe305d6094767ac30e97949
#5 resolve docker.io/library/nginx:stable-alpine@sha256:0e52bd054126cdc040b1276c0af347aeb02a41b9cfe305d6094767ac30e97949 0.1s done
#5 DONE 0.1s

#6 [2/3] COPY nginx/default.conf /etc/nginx/conf.d/default.conf
#6 CACHED

#7 [3/3] COPY site/ /usr/share/nginx/html/
#7 CACHED

#8 exporting to image
#8 exporting layers done
#8 exporting manifest sha256:598466d7d57890b8d1a25df3aa385ed2e443f0b51c1499008f7db6d213edf5cc done
#8 exporting config sha256:9a9046d15002bfbe0f39d4cfc42d3fad71cbd90df7480c47c026d319d4f94747 done
#8 exporting attestation manifest sha256:98a5e2f268975366495462d3d260e0bc6fc20ffb81c16d9c34ca567bfd582cd4
#8 exporting attestation manifest sha256:98a5e2f268975366495462d3d260e0bc6fc20ffb81c16d9c34ca567bfd582cd4 0.0s done
#8 exporting manifest list sha256:e0cb2800945b64800172929c430e8cd01c90b08fb9bac2b9bed9e0f145d78912 0.0s done
#8 naming to docker.io/library/jun-workshop:20261102t170206z done
#8 unpacking to docker.io/library/jun-workshop:20261102t170206z 0.0s done
#8 DONE 0.2s

exit_code=0

[2026-11-02T17:02:32.529995+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker image inspect jun-workshop:20261102t170206z
[
    {
        "Id": "sha256:e0cb2800945b64800172929c430e8cd01c90b08fb9bac2b9bed9e0f145d78912",
        "RepoTags": [
            "jun-workshop:20261102t170206z"
        ],
        "RepoDigests": [
            "jun-workshop@sha256:e0cb2800945b64800172929c430e8cd01c90b08fb9bac2b9bed9e0f145d78912"
        ],
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2026-11-03T01:58:36.401565426+09:00",
        "Config": {
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.30.6",
                "PKG_RELEASE=1",
                "DYNPKG_RELEASE=1",
                "NJS_VERSION=1.0.2",
                "NJS_RELEASE=1",
                "ACME_VERSION=0.4.1"
            ],
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "WorkingDir": "/",
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>",
                "org.opencontainers.image.description": "Codyssey mission 01: reproducible CLI, Docker and Git workshop",
                "org.opencontainers.image.title": "Jun Workshop Notes"
            },
            "StopSignal": "SIGQUIT"
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 92705913,
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:75c137aedfb2760f88629236cb7b797630aed0c3d91d626d1d1bb694878fc2ba",
                "sha256:5b91dba2fc11b3e6dab4d25e913db11e6e701065af717028e060dfb5ab8532e4",
                "sha256:a8a09d37d441c540c613402fa23c75308b04f4801e80f6d193316949f3df4b42",
                "sha256:d87f6628aa86314e48021285bd5dce15a2cf5166c1c80246d2e03dbb674abaf2",
                "sha256:313dac429378b98567656151706777045067624f9a6678873dd6fdc7ecf35545",
                "sha256:2ba21653acee34632d9eab26da39a5ff0cac12021817e6a5e9efac9507628575",
                "sha256:3212502c73d1691bd2b186efdda493ca750fc99795b6b0b85741af01b4e79aa4",
                "sha256:8ff2a17964b4a163c6ba0fa456ebd70ed12823a74324ba3b6f49d87bc25c1456",
                "sha256:101c1ed8485ab40c0699b6042410abbdf96f50827e0e47cc58b7202a75977884",
                "sha256:ad2ee25b3337d51d08904f2c2596a884f8bf487e29fc9a8074367b0c42d19a3c"
            ]
        },
        "Metadata": {
            "LastTagTime": "2026-11-02T17:02:32.234235462Z"
        },
        "Descriptor": {
            "mediaType": "application/vnd.oci.image.index.v1+json",
            "digest": "sha256:e0cb2800945b64800172929c430e8cd01c90b08fb9bac2b9bed9e0f145d78912",
            "size": 856
        },
        "Identity": {
            "Build": [
                {
                    "Ref": "l4mkhgwes2dudgs42yhmrg40f",
                    "CreatedAt": "2026-11-03T02:02:32.264835962+09:00"
                }
            ]
        }
    }
]

exit_code=0

[2026-11-02T17:02:33.041149+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker image inspect nginx:stable-alpine
[
    {
        "Id": "sha256:0e52bd054126cdc040b1276c0af347aeb02a41b9cfe305d6094767ac30e97949",
        "RepoTags": [
            "nginx:stable-alpine"
        ],
        "RepoDigests": [
            "nginx@sha256:0e52bd054126cdc040b1276c0af347aeb02a41b9cfe305d6094767ac30e97949"
        ],
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2026-10-21T23:23:59.165417074Z",
        "Config": {
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.30.6",
                "PKG_RELEASE=1",
                "DYNPKG_RELEASE=1",
                "NJS_VERSION=1.0.2",
                "NJS_RELEASE=1",
                "ACME_VERSION=0.4.1"
            ],
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "WorkingDir": "/",
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGQUIT"
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 92643363,
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:75c137aedfb2760f88629236cb7b797630aed0c3d91d626d1d1bb694878fc2ba",
                "sha256:5b91dba2fc11b3e6dab4d25e913db11e6e701065af717028e060dfb5ab8532e4",
                "sha256:a8a09d37d441c540c613402fa23c75308b04f4801e80f6d193316949f3df4b42",
                "sha256:d87f6628aa86314e48021285bd5dce15a2cf5166c1c80246d2e03dbb674abaf2",
                "sha256:313dac429378b98567656151706777045067624f9a6678873dd6fdc7ecf35545",
                "sha256:2ba21653acee34632d9eab26da39a5ff0cac12021817e6a5e9efac9507628575",
                "sha256:3212502c73d1691bd2b186efdda493ca750fc99795b6b0b85741af01b4e79aa4",
                "sha256:8ff2a17964b4a163c6ba0fa456ebd70ed12823a74324ba3b6f49d87bc25c1456"
            ]
        },
        "Metadata": {
            "LastTagTime": "2026-11-02T17:02:30.712884339Z"
        },
        "Descriptor": {
            "mediaType": "application/vnd.oci.image.index.v1+json",
            "digest": "sha256:0e52bd054126cdc040b1276c0af347aeb02a41b9cfe305d6094767ac30e97949",
            "size": 10317
        },
        "Identity": {
            "Pull": [
                {
                    "Repository": "docker.io/library/nginx"
                }
            ]
        }
    }
]

exit_code=0
```

## 포트와 로그

```text
[2026-11-02T17:02:33.599790+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker run -d --name jun-m01-20261102t170206z-web-a -p 127.0.0.1:18080:80 jun-workshop:20261102t170206z
5ed09f2d853694f62024f0bbdb4fdff24faf74fa6b768d4ef6f400deef4fc4ff

exit_code=0

[2026-11-02T17:02:34.584240+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker run -d --name jun-m01-20261102t170206z-web-b -p 127.0.0.1:18081:80 jun-workshop:20261102t170206z
c205dab32063838fcffb123c3b870a6037753887049e9ec3a85707168315b66a

exit_code=0

[2026-11-02T17:02:35.560808+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ curl --fail --silent --show-error --retry 10 --retry-all-errors --retry-delay 1 --max-time 3 http://127.0.0.1:18080/health
workshop-ready

exit_code=0

[2026-11-02T17:02:35.587284+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ curl --fail --silent --show-error --include http://127.0.0.1:18080/
HTTP/1.1 200 OK
Server: nginx/1.30.6
Date: Mon, 02 Nov 2026 17:02:35 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 3938
Last-Modified: Mon, 02 Nov 2026 16:53:40 GMT
Connection: keep-alive
ETag: "6ae8c014-f62"
Cache-Control: no-store
Accept-Ranges: bytes

<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="description" content="Ubuntu에서 Docker와 Git까지, 준짱의 첫 개발 작업실 학습 노트">
  <title>Jun Workshop · 첫 개발 작업실</title>
  <link rel="stylesheet" href="styles.css">
  <script src="app.js" defer></script>
</head>
<body>
  <header class="topbar"><a class="brand" href="#home"><span>J</span> JUN WORKSHOP</a><span class="label">CODYSSEY · MISSION 01</span></header>
  <main id="home">
    <section class="hero">
      <div><p class="eyebrow">나의 첫 번째 개발 작업실</p><h1>작은 명령에서<br><em>실행되는 환경까지.</em></h1><p class="intro">폴더를 만들고, 서버를 띄우고, 변경을 기록합니다.<br>배운 내용을 내 말로 설명하기 위한 작업실 노트입니다.</p><a class="button" href="#notes">작업실 둘러보기 <span aria-hidden="true">↗</span></a></div>
      <aside class="terminal" aria-label="개발 흐름 설명 예시"><div class="terminal-head"><span>● ● ●</span> workshop / bash</div><pre><span class="muted"># 이 화면은 학습 흐름 예시입니다</span>
<b>$</b> pwd
/home/damagez/mission01

<b>$</b> docker build -t jun-workshop:1.0 .
<span class="muted">이미지를 만들고 실행 환경을 준비합니다</span>

<b>$</b> git commit -m "Build my workshop"
<span class="muted">변경 내용을 내 컴퓨터에 기록합니다</span></pre><div class="version">CONTENT VERSION <strong id="content-version">WORKSHOP_V1</strong></div></aside>
    </section>
    <section id="notes" class="notes"><div class="section-top"><div><p class="eyebrow">THREE BUILDING BLOCKS</p><h2>작업실을 이루는 세 가지</h2></div><p>명령어의 목적과 결과를 연결합니다.</p></div>
      <div class="cards">
        <article><span class="number">01 / TERMINAL</span><h3>파일을 다루는 말</h3><p>현재 위치를 확인하고 파일을 생성·복사·이동합니다. 권한은 누가 읽고 쓰고 실행할 수 있는지 정합니다.</p><code>pwd · ls · cp · mv · chmod</code><button type="button" data-note="terminal">핵심 개념 보기</button></article>
        <article><span class="number">02 / DOCKER</span><h3>다시 실행할 수 있는 환경</h3><p>이미지로 환경을 묶고 컨테이너로 실행합니다. 포트는 접속을, 마운트와 볼륨은 파일 연결과 유지를 맡습니다.</p><code>build · run · logs · volume</code><button type="button" data-note="docker">핵심 개념 보기</button></article>
        <article><span class="number">03 / GIT</span><h3>변경에 남기는 기록</h3><p>저장한 파일 중 기록할 변경을 선택합니다. 로컬 commit과 GitHub push는 서로 다른 단계입니다.</p><code>status · add · commit · push</code><button type="button" data-note="git">핵심 개념 보기</button></article>
      </div>
      <div class="note-detail" aria-live="polite"><span>QUICK NOTE</span><p id="note-text">위 카드의 버튼을 누르면 핵심 개념을 짧게 확인할 수 있습니다.</p></div>
    </section>
    <section class="flow"><p class="eyebrow">FROM FILE TO SERVICE</p><h2>파일 하나가 웹페이지가 되기까지</h2><ol><li><b>01</b><strong>작성</strong><span>HTML과 설정 저장</span></li><li><b>02</b><strong>제작</strong><span>Dockerfile로 이미지 빌드</span></li><li><b>03</b><strong>실행</strong><span>컨테이너와 포트 연결</span></li><li><b>04</b><strong>검증</strong><span>접속·변경·데이터 확인</span></li><li><b>05</b><strong>기록</strong><span>Git과 README에 정리</span></li></ol></section>
  </main>
  <footer><span>JUN WORKSHOP / FIRST STEPS</span><p>이 웹페이지는 학습 노트입니다. 실제 검증 결과는 저장소의 README와 evidence 폴더에서 확인합니다.</p></footer>
</body>
</html>

exit_code=0

[2026-11-02T17:02:35.611722+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ curl --fail --silent --show-error --include http://127.0.0.1:18080/health
HTTP/1.1 200 OK
Server: nginx/1.30.6
Date: Mon, 02 Nov 2026 17:02:35 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 15
Connection: keep-alive

workshop-ready

exit_code=0

[2026-11-02T17:02:35.635619+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ curl --fail --silent --show-error --retry 10 --retry-all-errors --retry-delay 1 --max-time 3 http://127.0.0.1:18081/health
workshop-ready

exit_code=0

[2026-11-02T17:02:35.656434+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ curl --fail --silent --show-error --include http://127.0.0.1:18081/
HTTP/1.1 200 OK
Server: nginx/1.30.6
Date: Mon, 02 Nov 2026 17:02:35 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 3938
Last-Modified: Mon, 02 Nov 2026 16:53:40 GMT
Connection: keep-alive
ETag: "6ae8c014-f62"
Cache-Control: no-store
Accept-Ranges: bytes

<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="description" content="Ubuntu에서 Docker와 Git까지, 준짱의 첫 개발 작업실 학습 노트">
  <title>Jun Workshop · 첫 개발 작업실</title>
  <link rel="stylesheet" href="styles.css">
  <script src="app.js" defer></script>
</head>
<body>
  <header class="topbar"><a class="brand" href="#home"><span>J</span> JUN WORKSHOP</a><span class="label">CODYSSEY · MISSION 01</span></header>
  <main id="home">
    <section class="hero">
      <div><p class="eyebrow">나의 첫 번째 개발 작업실</p><h1>작은 명령에서<br><em>실행되는 환경까지.</em></h1><p class="intro">폴더를 만들고, 서버를 띄우고, 변경을 기록합니다.<br>배운 내용을 내 말로 설명하기 위한 작업실 노트입니다.</p><a class="button" href="#notes">작업실 둘러보기 <span aria-hidden="true">↗</span></a></div>
      <aside class="terminal" aria-label="개발 흐름 설명 예시"><div class="terminal-head"><span>● ● ●</span> workshop / bash</div><pre><span class="muted"># 이 화면은 학습 흐름 예시입니다</span>
<b>$</b> pwd
/home/damagez/mission01

<b>$</b> docker build -t jun-workshop:1.0 .
<span class="muted">이미지를 만들고 실행 환경을 준비합니다</span>

<b>$</b> git commit -m "Build my workshop"
<span class="muted">변경 내용을 내 컴퓨터에 기록합니다</span></pre><div class="version">CONTENT VERSION <strong id="content-version">WORKSHOP_V1</strong></div></aside>
    </section>
    <section id="notes" class="notes"><div class="section-top"><div><p class="eyebrow">THREE BUILDING BLOCKS</p><h2>작업실을 이루는 세 가지</h2></div><p>명령어의 목적과 결과를 연결합니다.</p></div>
      <div class="cards">
        <article><span class="number">01 / TERMINAL</span><h3>파일을 다루는 말</h3><p>현재 위치를 확인하고 파일을 생성·복사·이동합니다. 권한은 누가 읽고 쓰고 실행할 수 있는지 정합니다.</p><code>pwd · ls · cp · mv · chmod</code><button type="button" data-note="terminal">핵심 개념 보기</button></article>
        <article><span class="number">02 / DOCKER</span><h3>다시 실행할 수 있는 환경</h3><p>이미지로 환경을 묶고 컨테이너로 실행합니다. 포트는 접속을, 마운트와 볼륨은 파일 연결과 유지를 맡습니다.</p><code>build · run · logs · volume</code><button type="button" data-note="docker">핵심 개념 보기</button></article>
        <article><span class="number">03 / GIT</span><h3>변경에 남기는 기록</h3><p>저장한 파일 중 기록할 변경을 선택합니다. 로컬 commit과 GitHub push는 서로 다른 단계입니다.</p><code>status · add · commit · push</code><button type="button" data-note="git">핵심 개념 보기</button></article>
      </div>
      <div class="note-detail" aria-live="polite"><span>QUICK NOTE</span><p id="note-text">위 카드의 버튼을 누르면 핵심 개념을 짧게 확인할 수 있습니다.</p></div>
    </section>
    <section class="flow"><p class="eyebrow">FROM FILE TO SERVICE</p><h2>파일 하나가 웹페이지가 되기까지</h2><ol><li><b>01</b><strong>작성</strong><span>HTML과 설정 저장</span></li><li><b>02</b><strong>제작</strong><span>Dockerfile로 이미지 빌드</span></li><li><b>03</b><strong>실행</strong><span>컨테이너와 포트 연결</span></li><li><b>04</b><strong>검증</strong><span>접속·변경·데이터 확인</span></li><li><b>05</b><strong>기록</strong><span>Git과 README에 정리</span></li></ol></section>
  </main>
  <footer><span>JUN WORKSHOP / FIRST STEPS</span><p>이 웹페이지는 학습 노트입니다. 실제 검증 결과는 저장소의 README와 evidence 폴더에서 확인합니다.</p></footer>
</body>
</html>

exit_code=0

[2026-11-02T17:02:35.675799+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ curl --fail --silent --show-error --include http://127.0.0.1:18081/health
HTTP/1.1 200 OK
Server: nginx/1.30.6
Date: Mon, 02 Nov 2026 17:02:35 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 15
Connection: keep-alive

workshop-ready

exit_code=0

[2026-11-02T17:02:35.695142+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker logs jun-m01-20261102t170206z-web-a
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: /etc/nginx/conf.d/default.conf differs from the packaged version
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
172.17.0.1 - - [02/Nov/2026:17:02:35 +0000] "GET /health HTTP/1.1" 200 15 "-" "curl/8.18.0" "-"
172.17.0.1 - - [02/Nov/2026:17:02:35 +0000] "GET / HTTP/1.1" 200 3938 "-" "curl/8.18.0" "-"
172.17.0.1 - - [02/Nov/2026:17:02:35 +0000] "GET /health HTTP/1.1" 200 15 "-" "curl/8.18.0" "-"
2026/11/02 17:02:34 [notice] 1#1: using the "epoll" event method
2026/11/02 17:02:34 [notice] 1#1: nginx/1.30.6
2026/11/02 17:02:34 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0) 
2026/11/02 17:02:34 [notice] 1#1: OS: Linux 6.18.54.1-microsoft-standard-WSL2
2026/11/02 17:02:34 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1024:1048576
2026/11/02 17:02:34 [notice] 1#1: start worker processes
2026/11/02 17:02:34 [notice] 1#1: start worker process 29
2026/11/02 17:02:34 [notice] 1#1: start worker process 30
2026/11/02 17:02:34 [notice] 1#1: start worker process 31
2026/11/02 17:02:34 [notice] 1#1: start worker process 32
2026/11/02 17:02:34 [notice] 1#1: start worker process 33
2026/11/02 17:02:34 [notice] 1#1: start worker process 34
2026/11/02 17:02:34 [notice] 1#1: start worker process 35
2026/11/02 17:02:34 [notice] 1#1: start worker process 36

exit_code=0

[2026-11-02T17:02:36.148996+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker stats --no-stream jun-m01-20261102t170206z-web-a
CONTAINER ID   NAME                             CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O     PIDS
5ed09f2d8536   jun-m01-20261102t170206z-web-a   0.00%     8.789MiB / 7.535GiB   0.11%     2.25kB / 5.62kB   0B / 8.19kB   9

exit_code=0
```

## 바인드 마운트

```text
[2026-11-02T17:02:37.585070+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ cp -a /home/damagez/codyssey-mission01/site /home/damagez/codyssey-mission01/.verification-lab/20261102T170206Z/bind-site

exit_code=0

[2026-11-02T17:02:37.591440+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker run -d --name jun-m01-20261102t170206z-bind -p 127.0.0.1:18082:80 --mount type=bind,src=/home/damagez/codyssey-mission01/.verification-lab/20261102T170206Z/bind-site,dst=/usr/share/nginx/html,readonly jun-workshop:20261102t170206z
d73544cbf7ed7a3581e9f67bacd74618ed822e7a40e7cb48a391e4e2bd62ad03

exit_code=0

[2026-11-02T17:02:38.588904+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ curl --fail --silent --show-error --retry 10 --retry-all-errors --retry-delay 1 --max-time 3 http://127.0.0.1:18082/health
workshop-ready
curl: (56) Recv failure: Connection reset by peer

exit_code=0

[2026-11-02T17:02:39.610578+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ curl --fail --silent --show-error --include http://127.0.0.1:18082/
HTTP/1.1 200 OK
Server: nginx/1.30.6
Date: Mon, 02 Nov 2026 17:02:39 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 3938
Last-Modified: Mon, 02 Nov 2026 16:53:40 GMT
Connection: keep-alive
ETag: "6ae8c014-f62"
Cache-Control: no-store
Accept-Ranges: bytes

<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="description" content="Ubuntu에서 Docker와 Git까지, 준짱의 첫 개발 작업실 학습 노트">
  <title>Jun Workshop · 첫 개발 작업실</title>
  <link rel="stylesheet" href="styles.css">
  <script src="app.js" defer></script>
</head>
<body>
  <header class="topbar"><a class="brand" href="#home"><span>J</span> JUN WORKSHOP</a><span class="label">CODYSSEY · MISSION 01</span></header>
  <main id="home">
    <section class="hero">
      <div><p class="eyebrow">나의 첫 번째 개발 작업실</p><h1>작은 명령에서<br><em>실행되는 환경까지.</em></h1><p class="intro">폴더를 만들고, 서버를 띄우고, 변경을 기록합니다.<br>배운 내용을 내 말로 설명하기 위한 작업실 노트입니다.</p><a class="button" href="#notes">작업실 둘러보기 <span aria-hidden="true">↗</span></a></div>
      <aside class="terminal" aria-label="개발 흐름 설명 예시"><div class="terminal-head"><span>● ● ●</span> workshop / bash</div><pre><span class="muted"># 이 화면은 학습 흐름 예시입니다</span>
<b>$</b> pwd
/home/damagez/mission01

<b>$</b> docker build -t jun-workshop:1.0 .
<span class="muted">이미지를 만들고 실행 환경을 준비합니다</span>

<b>$</b> git commit -m "Build my workshop"
<span class="muted">변경 내용을 내 컴퓨터에 기록합니다</span></pre><div class="version">CONTENT VERSION <strong id="content-version">WORKSHOP_V1</strong></div></aside>
    </section>
    <section id="notes" class="notes"><div class="section-top"><div><p class="eyebrow">THREE BUILDING BLOCKS</p><h2>작업실을 이루는 세 가지</h2></div><p>명령어의 목적과 결과를 연결합니다.</p></div>
      <div class="cards">
        <article><span class="number">01 / TERMINAL</span><h3>파일을 다루는 말</h3><p>현재 위치를 확인하고 파일을 생성·복사·이동합니다. 권한은 누가 읽고 쓰고 실행할 수 있는지 정합니다.</p><code>pwd · ls · cp · mv · chmod</code><button type="button" data-note="terminal">핵심 개념 보기</button></article>
        <article><span class="number">02 / DOCKER</span><h3>다시 실행할 수 있는 환경</h3><p>이미지로 환경을 묶고 컨테이너로 실행합니다. 포트는 접속을, 마운트와 볼륨은 파일 연결과 유지를 맡습니다.</p><code>build · run · logs · volume</code><button type="button" data-note="docker">핵심 개념 보기</button></article>
        <article><span class="number">03 / GIT</span><h3>변경에 남기는 기록</h3><p>저장한 파일 중 기록할 변경을 선택합니다. 로컬 commit과 GitHub push는 서로 다른 단계입니다.</p><code>status · add · commit · push</code><button type="button" data-note="git">핵심 개념 보기</button></article>
      </div>
      <div class="note-detail" aria-live="polite"><span>QUICK NOTE</span><p id="note-text">위 카드의 버튼을 누르면 핵심 개념을 짧게 확인할 수 있습니다.</p></div>
    </section>
    <section class="flow"><p class="eyebrow">FROM FILE TO SERVICE</p><h2>파일 하나가 웹페이지가 되기까지</h2><ol><li><b>01</b><strong>작성</strong><span>HTML과 설정 저장</span></li><li><b>02</b><strong>제작</strong><span>Dockerfile로 이미지 빌드</span></li><li><b>03</b><strong>실행</strong><span>컨테이너와 포트 연결</span></li><li><b>04</b><strong>검증</strong><span>접속·변경·데이터 확인</span></li><li><b>05</b><strong>기록</strong><span>Git과 README에 정리</span></li></ol></section>
  </main>
  <footer><span>JUN WORKSHOP / FIRST STEPS</span><p>이 웹페이지는 학습 노트입니다. 실제 검증 결과는 저장소의 README와 evidence 폴더에서 확인합니다.</p></footer>
</body>
</html>

exit_code=0

[2026-11-02T17:02:39.629744+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ python3 -c 'from pathlib import Path; p=Path(__import__("sys").argv[1]); p.write_text(p.read_text().replace("WORKSHOP_V1","WORKSHOP_V2"))' /home/damagez/codyssey-mission01/.verification-lab/20261102T170206Z/bind-site/index.html

exit_code=0

[2026-11-02T17:02:39.709440+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ curl --fail --silent --show-error --include http://127.0.0.1:18082/
HTTP/1.1 200 OK
Server: nginx/1.30.6
Date: Mon, 02 Nov 2026 17:02:39 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 3938
Last-Modified: Mon, 02 Nov 2026 17:02:39 GMT
Connection: keep-alive
ETag: "6ae8c22f-f62"
Cache-Control: no-store
Accept-Ranges: bytes

<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="description" content="Ubuntu에서 Docker와 Git까지, 준짱의 첫 개발 작업실 학습 노트">
  <title>Jun Workshop · 첫 개발 작업실</title>
  <link rel="stylesheet" href="styles.css">
  <script src="app.js" defer></script>
</head>
<body>
  <header class="topbar"><a class="brand" href="#home"><span>J</span> JUN WORKSHOP</a><span class="label">CODYSSEY · MISSION 01</span></header>
  <main id="home">
    <section class="hero">
      <div><p class="eyebrow">나의 첫 번째 개발 작업실</p><h1>작은 명령에서<br><em>실행되는 환경까지.</em></h1><p class="intro">폴더를 만들고, 서버를 띄우고, 변경을 기록합니다.<br>배운 내용을 내 말로 설명하기 위한 작업실 노트입니다.</p><a class="button" href="#notes">작업실 둘러보기 <span aria-hidden="true">↗</span></a></div>
      <aside class="terminal" aria-label="개발 흐름 설명 예시"><div class="terminal-head"><span>● ● ●</span> workshop / bash</div><pre><span class="muted"># 이 화면은 학습 흐름 예시입니다</span>
<b>$</b> pwd
/home/damagez/mission01

<b>$</b> docker build -t jun-workshop:1.0 .
<span class="muted">이미지를 만들고 실행 환경을 준비합니다</span>

<b>$</b> git commit -m "Build my workshop"
<span class="muted">변경 내용을 내 컴퓨터에 기록합니다</span></pre><div class="version">CONTENT VERSION <strong id="content-version">WORKSHOP_V2</strong></div></aside>
    </section>
    <section id="notes" class="notes"><div class="section-top"><div><p class="eyebrow">THREE BUILDING BLOCKS</p><h2>작업실을 이루는 세 가지</h2></div><p>명령어의 목적과 결과를 연결합니다.</p></div>
      <div class="cards">
        <article><span class="number">01 / TERMINAL</span><h3>파일을 다루는 말</h3><p>현재 위치를 확인하고 파일을 생성·복사·이동합니다. 권한은 누가 읽고 쓰고 실행할 수 있는지 정합니다.</p><code>pwd · ls · cp · mv · chmod</code><button type="button" data-note="terminal">핵심 개념 보기</button></article>
        <article><span class="number">02 / DOCKER</span><h3>다시 실행할 수 있는 환경</h3><p>이미지로 환경을 묶고 컨테이너로 실행합니다. 포트는 접속을, 마운트와 볼륨은 파일 연결과 유지를 맡습니다.</p><code>build · run · logs · volume</code><button type="button" data-note="docker">핵심 개념 보기</button></article>
        <article><span class="number">03 / GIT</span><h3>변경에 남기는 기록</h3><p>저장한 파일 중 기록할 변경을 선택합니다. 로컬 commit과 GitHub push는 서로 다른 단계입니다.</p><code>status · add · commit · push</code><button type="button" data-note="git">핵심 개념 보기</button></article>
      </div>
      <div class="note-detail" aria-live="polite"><span>QUICK NOTE</span><p id="note-text">위 카드의 버튼을 누르면 핵심 개념을 짧게 확인할 수 있습니다.</p></div>
    </section>
    <section class="flow"><p class="eyebrow">FROM FILE TO SERVICE</p><h2>파일 하나가 웹페이지가 되기까지</h2><ol><li><b>01</b><strong>작성</strong><span>HTML과 설정 저장</span></li><li><b>02</b><strong>제작</strong><span>Dockerfile로 이미지 빌드</span></li><li><b>03</b><strong>실행</strong><span>컨테이너와 포트 연결</span></li><li><b>04</b><strong>검증</strong><span>접속·변경·데이터 확인</span></li><li><b>05</b><strong>기록</strong><span>Git과 README에 정리</span></li></ol></section>
  </main>
  <footer><span>JUN WORKSHOP / FIRST STEPS</span><p>이 웹페이지는 학습 노트입니다. 실제 검증 결과는 저장소의 README와 evidence 폴더에서 확인합니다.</p></footer>
</body>
</html>

exit_code=0

[2026-11-02T17:02:39.731346+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ curl --fail --silent --show-error --include http://127.0.0.1:18080/
HTTP/1.1 200 OK
Server: nginx/1.30.6
Date: Mon, 02 Nov 2026 17:02:39 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 3938
Last-Modified: Mon, 02 Nov 2026 16:53:40 GMT
Connection: keep-alive
ETag: "6ae8c014-f62"
Cache-Control: no-store
Accept-Ranges: bytes

<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="description" content="Ubuntu에서 Docker와 Git까지, 준짱의 첫 개발 작업실 학습 노트">
  <title>Jun Workshop · 첫 개발 작업실</title>
  <link rel="stylesheet" href="styles.css">
  <script src="app.js" defer></script>
</head>
<body>
  <header class="topbar"><a class="brand" href="#home"><span>J</span> JUN WORKSHOP</a><span class="label">CODYSSEY · MISSION 01</span></header>
  <main id="home">
    <section class="hero">
      <div><p class="eyebrow">나의 첫 번째 개발 작업실</p><h1>작은 명령에서<br><em>실행되는 환경까지.</em></h1><p class="intro">폴더를 만들고, 서버를 띄우고, 변경을 기록합니다.<br>배운 내용을 내 말로 설명하기 위한 작업실 노트입니다.</p><a class="button" href="#notes">작업실 둘러보기 <span aria-hidden="true">↗</span></a></div>
      <aside class="terminal" aria-label="개발 흐름 설명 예시"><div class="terminal-head"><span>● ● ●</span> workshop / bash</div><pre><span class="muted"># 이 화면은 학습 흐름 예시입니다</span>
<b>$</b> pwd
/home/damagez/mission01

<b>$</b> docker build -t jun-workshop:1.0 .
<span class="muted">이미지를 만들고 실행 환경을 준비합니다</span>

<b>$</b> git commit -m "Build my workshop"
<span class="muted">변경 내용을 내 컴퓨터에 기록합니다</span></pre><div class="version">CONTENT VERSION <strong id="content-version">WORKSHOP_V1</strong></div></aside>
    </section>
    <section id="notes" class="notes"><div class="section-top"><div><p class="eyebrow">THREE BUILDING BLOCKS</p><h2>작업실을 이루는 세 가지</h2></div><p>명령어의 목적과 결과를 연결합니다.</p></div>
      <div class="cards">
        <article><span class="number">01 / TERMINAL</span><h3>파일을 다루는 말</h3><p>현재 위치를 확인하고 파일을 생성·복사·이동합니다. 권한은 누가 읽고 쓰고 실행할 수 있는지 정합니다.</p><code>pwd · ls · cp · mv · chmod</code><button type="button" data-note="terminal">핵심 개념 보기</button></article>
        <article><span class="number">02 / DOCKER</span><h3>다시 실행할 수 있는 환경</h3><p>이미지로 환경을 묶고 컨테이너로 실행합니다. 포트는 접속을, 마운트와 볼륨은 파일 연결과 유지를 맡습니다.</p><code>build · run · logs · volume</code><button type="button" data-note="docker">핵심 개념 보기</button></article>
        <article><span class="number">03 / GIT</span><h3>변경에 남기는 기록</h3><p>저장한 파일 중 기록할 변경을 선택합니다. 로컬 commit과 GitHub push는 서로 다른 단계입니다.</p><code>status · add · commit · push</code><button type="button" data-note="git">핵심 개념 보기</button></article>
      </div>
      <div class="note-detail" aria-live="polite"><span>QUICK NOTE</span><p id="note-text">위 카드의 버튼을 누르면 핵심 개념을 짧게 확인할 수 있습니다.</p></div>
    </section>
    <section class="flow"><p class="eyebrow">FROM FILE TO SERVICE</p><h2>파일 하나가 웹페이지가 되기까지</h2><ol><li><b>01</b><strong>작성</strong><span>HTML과 설정 저장</span></li><li><b>02</b><strong>제작</strong><span>Dockerfile로 이미지 빌드</span></li><li><b>03</b><strong>실행</strong><span>컨테이너와 포트 연결</span></li><li><b>04</b><strong>검증</strong><span>접속·변경·데이터 확인</span></li><li><b>05</b><strong>기록</strong><span>Git과 README에 정리</span></li></ol></section>
  </main>
  <footer><span>JUN WORKSHOP / FIRST STEPS</span><p>이 웹페이지는 학습 노트입니다. 실제 검증 결과는 저장소의 README와 evidence 폴더에서 확인합니다.</p></footer>
</body>
</html>

exit_code=0
```

## 볼륨 데이터 유지

```text
[2026-11-02T17:02:39.752091+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker volume create jun-m01-20261102t170206z-data
jun-m01-20261102t170206z-data

exit_code=0

[2026-11-02T17:02:40.211278+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker run -d --name jun-m01-20261102t170206z-writer --mount type=volume,src=jun-m01-20261102t170206z-data,dst=/data ubuntu:24.04 sleep infinity
bbe2ab17976602ed6b953c71121c923f75dc6e7e2b2d58e74229d897deb6313d

exit_code=0

[2026-11-02T17:02:41.124043+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker exec jun-m01-20261102t170206z-writer bash -lc 'printf "persistent-workshop-data\n" > /data/note.txt; cat /data/note.txt'
persistent-workshop-data

exit_code=0

[2026-11-02T17:02:41.664252+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker exec jun-m01-20261102t170206z-writer sha256sum /data/note.txt
1ac123a97d636cf7220d4ba3d7b045857d820eee3ad33a216ebcb8651e56de73  /data/note.txt

exit_code=0

[2026-11-02T17:02:42.266809+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker stop jun-m01-20261102t170206z-writer
jun-m01-20261102t170206z-writer

exit_code=0

[2026-11-02T17:02:52.946045+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker rm jun-m01-20261102t170206z-writer
jun-m01-20261102t170206z-writer

exit_code=0

[2026-11-02T17:02:53.441314+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker run -d --name jun-m01-20261102t170206z-reader --mount type=volume,src=jun-m01-20261102t170206z-data,dst=/data,readonly ubuntu:24.04 sleep infinity
975e5114a80684fa1fe2d219b6d5f920cc483e82117e80a56a3b3fabdbe02661

exit_code=0

[2026-11-02T17:02:54.404619+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker exec jun-m01-20261102t170206z-reader cat /data/note.txt
persistent-workshop-data

exit_code=0

[2026-11-02T17:02:54.950055+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker exec jun-m01-20261102t170206z-reader sha256sum /data/note.txt
1ac123a97d636cf7220d4ba3d7b045857d820eee3ad33a216ebcb8651e56de73  /data/note.txt

exit_code=0

[2026-11-02T17:02:55.535232+00:00] actor=jarvis-assisted; linux_user=root
cwd=/home/damagez/codyssey-mission01
$ docker volume inspect jun-m01-20261102t170206z-data
[
    {
        "CreatedAt": "2026-11-03T02:02:40+09:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/jun-m01-20261102t170206z-data/_data",
        "Name": "jun-m01-20261102t170206z-data",
        "Options": null,
        "Scope": "local"
    }
]

exit_code=0
```
