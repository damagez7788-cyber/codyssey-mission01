# 트러블슈팅: 실제 실패 2건과 포트 충돌 대응

제출자: 강준권

### 사례 1: 빌드 성공 후 바탕 이미지 태그 조회 실패

**문제:** 최초 검증에서 커스텀 이미지 build는 성공했지만 `nginx:stable-alpine` 조회가 종료 코드 1로 실패했습니다.

```text
$ docker image inspect nginx:stable-alpine
[]
Error response from daemon: No such image: nginx:stable-alpine
exit_code=1
```

**원인 가설:** BuildKit이 FROM을 빌드용으로 해석한 것과 Docker 엔진에 이름 있는 기본 이미지 태그가 등록된 것은 별개일 수 있습니다. 빌드 성공만으로 기본 태그 조회 성공까지 가정한 점을 확인했습니다.

**검증:** [첫 실패 원문](../evidence/20261102T165758Z/04_build.txt)에서 커스텀 이미지 build·조회 성공과 기본 이미지 조회 실패가 연속으로 기록돼 있습니다. 의도적으로 만든 오류가 아닙니다.

**조치:** 검증 스크립트에 `docker pull nginx:stable-alpine`을 명시해 기본 이미지를 받은 뒤 build와 inspect를 수행하도록 보완했습니다. `pull`은 이미지 받기, `build`는 Dockerfile로 제작하기, `image inspect`는 등록된 이미지의 세부 정보 확인입니다.

**재검증 결과(실제 출력 발췌):**

```text
$ docker pull nginx:stable-alpine
stable-alpine: Pulling from library/nginx
Digest: sha256:0e52bd054126cdc040b1276c0af347aeb02a41b9cfe305d6094767ac30e97949
Status: Image is up to date for nginx:stable-alpine
docker.io/library/nginx:stable-alpine
exit_code=0
```


```text
$ docker image inspect nginx:stable-alpine
[
    {
        "Id": "sha256:0e52bd054126cdc040b1276c0af347aeb02a41b9cfe305d6094767ac30e97949",
        "RepoTags": [
            "nginx:stable-alpine"
[긴 출력 중략]
exit_code=0
```

두 명령 모두 `exit_code=0`으로 성공했습니다. 정확한 이미지 ID·digest·빌드 출력은 [최종 빌드 원문](../evidence/20261102T170206Z/04_build.txt)에서 확인할 수 있습니다.

### 사례 2: 컨테이너 생성 직후 웹 접속 초기화

**문제:** 두 번째 검증에서 컨테이너 run은 성공했지만, 즉시 요청한 HTTP 접속이 종료 코드 56으로 실패했습니다.

```text
$ curl --fail --silent --show-error --include http://127.0.0.1:18082/
curl: (56) Recv failure: Connection reset by peer
exit_code=56
```

**원인 가설:** 컨테이너 생성 직후 서버가 요청을 받을 준비가 끝나기 전에 curl이 실행됐을 가능성을 점검했습니다. 연결 초기화의 저수준 원인까지 확정하지는 않았습니다.

**검증:** [두 번째 실패 원문](../evidence/20261102T170027Z/06_bind.txt)에 run 성공 직후 curl 실패가 기록돼 있습니다. 당시 출력은 `Connection reset by peer`, 즉 상대편에서 연결을 초기화했다는 뜻입니다.

**조치:** 먼저 `/health`가 응답할 때까지 상한을 둔 재시도를 수행한 다음 본문을 검사하도록 수정했습니다. `--retry 10`은 최대 10회 재시도, `--retry-all-errors`는 모든 오류를 재시도 대상으로 처리, `--retry-delay 1`은 재시도 사이 1초 대기, `--max-time 3`은 요청별 최대 3초입니다. `--fail`은 HTTP 오류를 실패로 처리하고 `--silent --show-error`는 진행 표시를 줄이되 오류를 보여 줍니다.

**재검증 결과(실제 출력 발췌):**

```text
$ curl --fail --silent --show-error --retry 10 --retry-all-errors --retry-delay 1 --max-time 3 http://127.0.0.1:18082/health
workshop-ready
curl: (56) Recv failure: Connection reset by peer
exit_code=0
```

위 stderr의 연결 초기화는 재시도 중 발생한 메시지입니다. 마지막에는 `workshop-ready`를 받고 종료 코드 0으로 성공했습니다. 오류 문구가 한 번 나타났다는 것과 최종 요청 실패를 구분합니다.

```text
$ curl --fail --silent --show-error --include http://127.0.0.1:18082/
HTTP/1.1 200 OK
Server: nginx/1.30.6
Date: Mon, 02 Nov 2026 17:02:39 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 3938
Last-Modified: Mon, 02 Nov 2026 17:02:39 GMT
[긴 출력 중략]
exit_code=0
```

최종 HTTP 응답은 `200 OK`이고 종료 코드 0입니다. 원문 본문에서 변경 후 `WORKSHOP_V2`와 기존 COPY 컨테이너의 `WORKSHOP_V1` 유지도 확인했습니다. [최종 마운트·접속 원문](../evidence/20261102T170206Z/06_bind.txt), [검사 통과 목록](../evidence/20261102T170206Z/checks.json).

### 평가 항목 #16: 포트 충돌 진단·해제·대체 실행

포트 오류가 나면 먼저 **어떤 프로그램/컨테이너가 해당 포트를 사용하는지 확인**하고, 본인 실습 서비스일 때만 대상을 지정해 중지합니다. 다음은 절차 안내이며 중지·프로세스 종료 명령을 이번 점검에서 실행한 기록은 아닙니다.

1. **운영체제의 사용 프로세스 확인**

```bash
sudo ss -ltnp '( sport = :18080 )'
```

뜻: 관리 권한으로 TCP 수신 포트와 프로세스를 확인합니다. `-l` 수신 중, `-t` TCP, `-n` 숫자 표시, `-p` 프로세스 표시, `sport = :18080`은 로컬 18080번만 조회합니다. 출력 행의 `users`, 프로그램 이름, `pid`를 확인합니다. 제목 줄만 나오면 해당 시점에 조회된 수신 소켓이 없다는 뜻입니다.

2. **Docker 컨테이너인지 대조**

```bash
sudo docker ps --filter publish=18080 --format 'table {{.Names}}	{{.Ports}}	{{.Status}}'
```

뜻: 실행 중인 컨테이너 가운데 18080 포트에 관련된 항목의 이름·포트 매핑·상태를 표시합니다. `PORTS` 열에서 호스트의 `18080->80/tcp` 매핑을 직접 대조합니다. 필요하면 `sudo docker ps --format 'table {{.Names}}	{{.Ports}}'`로 전체 실행 목록의 매핑을 확인합니다.

3. **본인 실습 컨테이너가 점유한 경우 해제**

아래의 `<...>`는 설명용 자리표시자입니다. 진단 결과로 확인한 실제 이름·PID로 바꿔야 하며 그대로 실행하는 명령이 아닙니다.

```bash
sudo docker stop <확인한_본인_컨테이너명>
sudo ss -ltnp '( sport = :18080 )'
sudo docker ps --filter publish=18080
```

`docker stop`은 이름으로 지정한 컨테이너를 정상 중지합니다. 중지 후 ss와 docker ps를 다시 확인해 점유가 해제됐는지 검증합니다. 컨테이너가 아닌 본인 프로세스라면 아래처럼 정체를 먼저 확인하고 정상 종료를 요청할 수 있습니다.

```bash
ps -p <확인한_PID> -o pid,comm,args
sudo kill -TERM <확인한_본인_PID>
sudo ss -ltnp '( sport = :18080 )'
```

`ps -p`는 해당 PID의 프로그램과 실행 인자를 확인하고, `kill -TERM`은 지정한 본인 프로세스에 정상 종료 신호를 보냅니다. 다른 사람/시스템 서비스나 Docker의 프록시를 임의로 종료하지 않습니다. Docker 서비스는 해당 컨테이너를 중지하는 방법을 우선합니다.

4. **기존 서비스를 유지해야 하면 대체 포트 사용**

```bash
sudo ss -ltnp '( sport = :18090 )'
sudo env WORKSHOP_PORT=18090 WORKSHOP_CONTAINER=jun-workshop-alt-18090 bash scripts/run.sh
curl --fail --silent --show-error --retry 10 --retry-all-errors --retry-delay 1 --max-time 3 http://localhost:18090/health
curl --fail --include http://localhost:18090/
```

`env`로 해당 실행에만 환경 변수를 전달합니다. `WORKSHOP_PORT`는 호스트 포트, `WORKSHOP_CONTAINER`는 새 컨테이너 이름입니다. `bash scripts/run.sh`는 기존 실행 도우미로 이미지를 빌드하고 지정한 포트로 실행합니다. 이미지 안 서버의 80번은 유지합니다. 재현 시 **예상** 결과는 `/health`의 `workshop-ready`와 본문의 `WORKSHOP_V1`, HTTP 200입니다. 이 대체 실행 예시를 실제 새 실행 결과라고 표시하지 않습니다.

**이번 추가 점검의 실제 출력** (2026-11-03T13:36:37.753804+09:00):

```text
$ ss -ltnp '(' sport = :18080 ')'
State Recv-Q Send-Q Local Address:Port Peer Address:PortProcess
exit_code=0

$ ss -ltnp '(' sport = :18090 ')'
State Recv-Q Send-Q Local Address:Port Peer Address:PortProcess
exit_code=0

$ docker ps --filter publish=18080 --format 'table {{.Names}}	{{.Ports}}	{{.Status}}'
NAMES     PORTS     STATUS
exit_code=0
```

해석: 점검 당시 18080·18090은 ss 출력에 제목만 있었고, 18080을 공개하는 실행 중 Docker 컨테이너도 없었습니다. 이번에 새 포트 충돌을 겪었다거나 서비스를 종료했다고 기록하지 않습니다. [현재 포트 진단 전체 로그](../evidence/11_port_diagnostics.txt).
