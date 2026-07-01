# Extract Method / 한 함수 한 수준을 스스로 적용함

Lesson 01 실습에서 `register` 메서드를 스스로 리팩토링. 검증·비밀번호 해싱·유저 생성·환영 발송의
네 덩어리를 정확히 식별하고 각각을 이름 있는 메서드로 추출했다. "어느 줄이 주변보다 낮은 수준인가"를
스스로 판별 — 단순 노출이 아니라 적용 단계에 도달.

## Evidence
- validation 두 줄 → validate(form) 로 묶음 (정확)
- sha256+SALT → encode 계열 메서드로 추출, "값을 돌려주는 세부"임을 이해
- createUser / sendWelcome 도 독립 식별

## Implications
- Extract Method 기초는 완료. 반복 연습보다 **다음 수준으로 진행**해도 됨.
- 남은 미세 격차: Java 네이밍 관례(동사 먼저)는 상기시켜줄 것. encode 철자 등 사소.
- 다음: 캡슐화 — 함수 뒤가 아니라 *객체* 뒤로 데이터+로직 감추기. `user.getGrade().equals("VIP")` → `user.isVip()`.

관련: [[0001-starting-point]]
