# SOLID & 클린코드 — 잘 읽히는 코드 (Java)

"추상(抽象)"을 뿌리로 클린코드·객체지향·SOLID를 코드 레벨에서 하나씩 익히는 학습 워크스페이스.
지저분한 Java 코드를 단계적으로 리팩토링하며 원칙에 이름을 붙이고, 마지막엔 실제 JDK 오픈소스를 렌즈로 읽는다.

## 레슨 (`lessons/`)

| # | 주제 | 핵심 |
|---|------|------|
| 01 | 추상 | 세부를 함수 이름 뒤로 — 한 함수 한 수준의 추상화 (Extract Method) |
| 02 | 캡슐화 | 데이터+로직을 객체 뒤로 — Tell, Don't Ask / Feature Envy |
| 03 | 다형성 | if/switch 분기 제거 → 개방-폐쇄 원칙(OCP) |
| 04 | 상속 vs 조합 | is-a / has-a, 리스코프 치환 원칙(LSP), "상속보다 조합" |
| 05 | SOLID 완성 | 단일 책임(S)·인터페이스 분리(I)·의존성 역전(D) |
| 06 | 실전 오픈소스 분석 | `java.util.Comparator`(전략 패턴·조합) vs `Stack`(상속 실수) |

각 레슨은 자체 완결형 HTML. `assets/style.css`(공통 스타일)와 `assets/quiz.js`(즉시 채점 퀴즈)를 공유한다.

## 폴더

- `lessons/` — 레슨(HTML). 브라우저로 열면 됨
- `reference/glossary.html` — 코스 용어집
- `assets/` — 공통 스타일시트·퀴즈 위젯
- `MISSION.md` / `RESOURCES.md` — 학습 목표와 검증된 참고 자료
- `learning-records/` — 학습 진행 기록(ADR 형식)

## 참고 자료
Robert C. Martin, *Clean Code* / *Clean Architecture* · Joshua Bloch, *Effective Java* (Item 18) ·
[Refactoring Guru](https://refactoring.guru/) · [Baeldung — SOLID](https://www.baeldung.com/solid-principles) ·
[Oracle Java API](https://docs.oracle.com/en/java/javase/17/docs/api/)
