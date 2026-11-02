# 실제 문제 해결 기록

두 사례 모두 새 제출 프로젝트의 실행 검증 중 실제 발생한 오류입니다. 지원 도구가 발견·해결한 사항으로 기록하며, 사용자가 직접 겪었다고 표현하지 않습니다. 의도적으로 만든 폴더 Permission denied 실험은 이 두 건에 포함하지 않았습니다.

## 1 빌드는 성공했지만 바탕 이미지 태그 조회 실패

문제: 첫 검증 실행에서 커스텀 이미지 build는 종료 코드 0이었지만 뒤이은 기본 이미지 조회는 종료 코드 1이었습니다.

```text
$ docker image inspect nginx:stable-alpine
[]
Error response from daemon: No such image: nginx:stable-alpine
exit_code=1
```

원인 가설: 검증 스크립트가 FROM 이미지의 빌드용 해석·캐시 사용과 엔진의 이름 있는 이미지 등록을 같은 것으로 가정했습니다. 커스텀 이미지 제작 성공만으로 원래 기본 태그의 inspect 가능 여부까지 보장하지 않습니다.

확인: [첫 실패의 빌드·조회 로그](../evidence/20261102T165758Z/04_build.txt)에서 커스텀 이미지 조회 성공과 기본 태그 조회 실패를 함께 확인했습니다.

해결: 검증에서 `docker pull nginx:stable-alpine`을 명시적으로 수행한 후 제작·조회하도록 수정했습니다.

```bash
docker pull nginx:stable-alpine
docker build -t jun-workshop:<실행별태그> .
docker image inspect nginx:stable-alpine
```

위 `<실행별태그>`는 설명 표기입니다. 실제 실행 태그와 결과는 [성공한 재검증 로그](../evidence/20261102T170206Z/04_build.txt)에 있습니다. pull·build·inspect가 모두 종료 코드 0으로 끝났습니다.

## 2 컨테이너 생성 직후 HTTP 연결 초기화

문제: 마운트 컨테이너 run은 성공했지만 즉시 실행한 curl이 종료 코드 56으로 실패했습니다.

```text
$ curl --fail --silent --show-error --include http://127.0.0.1:18082/
curl: (56) Recv failure: Connection reset by peer
exit_code=56
```

원인 가설: 컨테이너 생성 성공을 웹 서버의 요청 수신 준비 완료로 바로 간주했습니다. 기동 과정에서 너무 이르게 요청했을 가능성을 확인 대상으로 삼았습니다. 특정 내부 프로세스의 저수준 원인까지 단정하지 않습니다.

확인: [두 번째 실행의 실패 원문](../evidence/20261102T170027Z/06_bind.txt)에는 run 성공과 curl 실패가 연속 기록돼 있습니다.

해결: 실제 `/health` 응답을 재시도 가능한 curl로 확인한 다음 페이지 본문 검증을 수행하도록 변경했습니다.

```bash
curl --fail --silent --show-error --retry 10 \
  --retry-all-errors --retry-delay 1 --max-time 3 \
  http://127.0.0.1:18082/health
```

결과: [최종 마운트 검증](../evidence/20261102T170206Z/06_bind.txt)에서 준비 상태와 HTTP 요청이 모두 성공했고, V1에서 V2로의 변경 및 기존 COPY 컨테이너의 V1 유지도 확인했습니다. 재시도 상한이 있어 준비되지 않은 서비스를 무한 대기하지 않습니다.
