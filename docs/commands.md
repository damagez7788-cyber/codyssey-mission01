# 검증 명령어와 결과 읽기

전체 실제 실행 명령·출력은 [코드 블록으로 정리한 검증 원문](actual-verification.md)과 [구조화한 실행 기록](../evidence/20261102T170206Z/commands.json)에 있습니다. 각 기록은 실행 시각·주체·Linux 계정·작업 위치·종료 코드를 포함합니다.

## Linux 파일과 권한

| 명령 또는 구성 | 전체 뜻과 주요 구성 | 이번 결과의 의미 |
| --- | --- | --- |
| `pwd` | 현재 폴더의 절대 경로 표시 | 새 검증 전용 폴더에서 작업함 |
| `mkdir notes archive` | mkdir로 폴더 두 개 생성 | 성공하면 보통 출력 없음 |
| `touch empty.txt .hidden-note` | 없는 두 파일 생성. 점으로 시작하는 이름은 숨김 항목 | 빈 파일과 숨김 파일 생성 |
| `ls -la` | l은 자세히, a는 숨김 항목 포함 | 생성된 파일·폴더와 권한 확인 |
| `printf 'Fresh mission verification\n' > notes/original.txt` | 글씨와 줄바꿈을 출력해 >로 대상 파일에 저장 | 화면 출력 대신 파일에 저장 |
| `cat notes/original.txt` | 파일 내용 출력 | 저장한 실제 글씨를 읽음 |
| `cp notes/original.txt notes/copy.txt` | 첫 파일을 둘째 이름으로 복사 | 원본을 유지하고 복사본 생성 |
| `mv notes/copy.txt archive/renamed.txt` | 복사본을 다른 폴더와 이름으로 이동 | 원래 경로에서는 사라지고 새 경로에 존재 |
| `rm archive/renamed.txt` | 이번에 생성한 복사본 삭제 | 이후 archive 목록에서 해당 파일이 사라짐 |
| `chmod 644 notes/original.txt` | 파일에 소유자 rw, 그룹 r, 나머지 r 부여 | `-rw-r--r--` |
| `chmod 600 notes/original.txt` | 소유자 rw만 부여 | `-rw-------` |
| `ls -ld archive` | l은 상세, d는 폴더 자체 확인 | 폴더의 권한 전후 비교 |
| `chmod 600 archive` | 소유자 r·w만 허용, 폴더 진입 x 없음 | 일반 사용자 cd가 의도대로 거부됨 |
| `chmod 755 archive` | 소유자 rwx, 나머지 r-x | 폴더 진입 가능 상태 복원 |
| `cd archive; pwd` | 폴더 진입 뒤 위치 확인 | 복원 후 실제 archive 경로 표시 |

`Permission denied`는 권한 거부입니다. 이번 폴더 실험의 종료 코드 1은 예상한 실험 결과이며, 불시에 발생한 문제 해결 사례로 계산하지 않았습니다. 빈 출력은 실패를 뜻하지 않으며 목록·내용·종료 코드로 함께 확인했습니다.

## Docker 상태와 컨테이너

| 명령 또는 구성 | 뜻 | 실제 결과 읽기 |
| --- | --- | --- |
| `docker --version` | 명령 도구 버전 | Docker 29.9.2 |
| `docker info` | 엔진과 시스템 정보 | Server 정보 반환, 엔진 연결 확인 |
| `docker run --name ... hello-world` | 이름 있는 테스트 컨테이너 생성·실행 | Hello from Docker 출력 뒤 정상 종료 |
| `docker run -dit --name ... ubuntu:24.04 bash` | d 백그라운드, i 입력 유지, t 터미널, bash 실행 | 컨테이너 ID 반환, bash 유지 |
| `docker exec ... bash -lc 'ls /; echo inside-ubuntu'` | 실행 중 컨테이너에 새 셸 명령 수행. l 로그인 셸, c 문자열 실행 | 내부 목록과 inside-ubuntu 출력 |
| `docker attach ...` | 기존 주 프로세스의 입출력에 연결 | 주 bash에서 echo 확인 후 Ctrl+P Ctrl+Q로 분리 |
| `docker inspect --format '{{.State.Status}}' ...` | 대상의 상태만 정해진 형식으로 조회 | 분리 후 running 유지 |
| `docker stop ...` | 지정 컨테이너 중지 | 이름 출력. 이후 상태 확인 가능 |
| `docker start ...` | 기존 중지 컨테이너 재시작 | 이름 출력 |
| `docker image ls` | 엔진의 이미지 목록 | 이미지와 태그 확인 |
| `docker ps -a` | 중지된 것 포함 컨테이너 목록 | Up과 Exited 구분 |
| `docker logs ...` | 주 프로세스가 남긴 출력 확인 | 웹 요청에 따른 서버 기록 확인 |
| `docker stats --no-stream ...` | CPU·메모리 등의 사용량을 한 번만 출력 | 실행 시점 실제 사용량 확인 |

## 이미지와 접속

`docker pull nginx:stable-alpine`은 기본 이미지를 엔진에 명시적으로 내려받습니다. `docker build -t 이름:태그 .`은 현재 폴더의 Dockerfile과 파일을 이용해 커스텀 이미지를 제작합니다. `docker image inspect`는 이미지 ID·설정·digest 등을 확인합니다.

`-p 127.0.0.1:18080:80`은 이 컴퓨터의 18080을 컨테이너의 80에 연결합니다. 다른 호스트 포트 18081에서도 같은 이미지를 실행했습니다. `curl --include 주소`는 주소에 요청해 헤더와 본문을 출력합니다. 200 OK는 요청 성공입니다.

`--retry 10 --retry-all-errors --retry-delay 1 --max-time 3`은 준비 상태 확인 요청에 재시도 상한·간격·각 요청 제한 시간을 둡니다. 재시도 무한 루프가 아닙니다.

## 마운트와 볼륨

`--mount type=bind,src=원본경로,dst=컨테이너경로,readonly`는 호스트 원본 폴더를 컨테이너 경로에 읽기 전용 연결합니다. 검증에서는 전용 복사 폴더의 HTML 표시를 V1에서 V2로 바꿨습니다. 저장소 원본 파일은 V1을 유지했습니다.

`docker volume create 이름`은 Docker 관리 저장 공간을 만듭니다. `--mount type=volume,src=이름,dst=/data`로 연결했습니다. writer의 `/data/note.txt`에 글을 저장한 뒤, `docker stop`과 `docker rm`으로 **이번 writer만** 중지·삭제했습니다. 같은 볼륨을 새 reader에 연결했을 때 cat 내용과 `sha256sum`이 같아 데이터 유지를 확인했습니다.

## Git과 인증

`git init -b main`은 새 저장소를 main 브랜치로 시작합니다. `git config user.name`, `user.email`, `init.defaultBranch`는 이번 저장소의 작성자와 기본 브랜치를 설정합니다. `git config --local --list`로 이 저장소 설정만 기록했습니다.

`gh api user`의 공개 계정명·계정 ID 반환은 기존 GitHub CLI 인증이 유효하다는 확인입니다. 이번 저장소의 push나 VS Code 로그인 성공을 뜻하지 않습니다. `git add`는 기록할 변경 선택, `git commit`은 로컬 이력 생성, `git push`는 별도 원격 전송입니다.
