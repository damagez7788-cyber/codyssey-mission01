"use strict";
const notes = {
  terminal: "파일의 x는 실행, 폴더의 x는 안으로 들어가거나 경로를 통과하는 권한입니다. 644와 755는 소유자·그룹·그 밖의 사용자 순서로 읽습니다.",
  docker: "이미지는 실행 틀, 컨테이너는 그 틀로 만든 실행 환경입니다. 바인드 마운트는 지정한 폴더를 연결하고, 볼륨은 Docker가 관리하는 별도 저장 공간입니다.",
  git: "파일 저장 → add로 변경 선택 → commit으로 로컬 이력 생성 → push로 원격 전송. commit만으로 GitHub에 업로드되지는 않습니다."
};
for (const button of document.querySelectorAll("[data-note]")) {
  button.addEventListener("click", () => {
    document.getElementById("note-text").textContent = notes[button.dataset.note];
  });
}
