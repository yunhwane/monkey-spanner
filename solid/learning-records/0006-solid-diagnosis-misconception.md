# SOLID 진단 시 원칙 오적용 교정 — "적용 조건" 감각

Lesson 05 실습에서 OrderService를 진단. DIP는 정확히 잡았으나(new MySqlDatabase), 두 가지 오적용:
(1) csv 포맷/파일쓰기를 LSP로 진단 — 상속이 없어 LSP는 적용 불가, (2) mail.send를 다형성으로 진단 —
타입 분기가 없어 다형성 위반 아님. 실제로는 ②③④가 모두 같은 병(SRP: 한 메서드에 검증/저장/리포트/메일
네 책임)이었고 DIP가 겹친 것. "각 줄을 다른 원칙에 배정"하는 습관을 교정.

## Evidence
- DIP 정확 진단 (구체 의존)
- 캡슐화(Tell-Don't-Ask) 진단은 일리 있음
- 오개념: LSP=상속/치환 상황에서만, 다형성 위반=타입 분기(if/switch) 있을 때만 — "적용 조건" 미보유

## Implications
- 교정한 규칙 두 개(면접 중요): "부모/자식 없으면 LSP 제외", "타입 분기 없으면 다형성 위반 제외".
- SRP를 "지배적 진단"으로 먼저 보는 습관(각 줄이 바뀌는 이유를 묻기) 강화 필요.
- 다음(Lesson 06 오픈소스 분석)에서 이 "적용 조건" 감각을 실제 코드로 재확인 — Comparator(다형성/함수형 인터페이스),
  Deque vs Stack(상속 실수/LSP) 등 각 원칙이 "실제로 성립하는" 사례로 보강.
- 이 기록은 오개념 교정이라 향후 관련 주제(디자인 패턴)에서 재점검 지점.

관련: [[0004-polymorphism-ocp-grasped]], [[0005-inheritance-vs-composition-grasped]]
