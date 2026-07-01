# 상속 vs 조합 판단 + LSP 이해 — OOP 4축 완료

Lesson 04 실습에서 `Stack extends ArrayList`를 is-a/has-a 테스트로 스스로 판별: "Stack은 ArrayList의 일종이
아니니 조합으로 List를 필드로 가져야 한다". 정확한 근거로 올바른 결론. 교사가 실제 JDK 사례(java.util.Stack
extends Vector, Deque 권장)를 면접 무기로 추가 제공.

## Evidence
- is-a/has-a 테스트를 스스로 적용해 상속 부적절 판정
- 조합 리팩토링 방향(private List 필드) 제시
- "무엇을 노출하지 않는가"가 조합의 이득임은 교사가 캡슐화(L02)와 연결

## Implications
- OOP 4대 축(추상화/캡슐화/다형성/상속) + SOLID O·L 완료. 남은 SOLID: S(SRP), I(ISP), D(DIP).
- 다음: Lesson 05에서 S·I·D를 지금까지 예제 위에 통합.
- 그 다음(사용자 핵심 희망): 실제 오픈소스 코드 분석 세션. 후보 — java.util.Stack/Deque, Comparator, Spring
  의 인터페이스 설계 등. 지금까지 배운 렌즈(캡슐화/다형성/OCP/조합)로 읽기.
- 학습자는 판단형 질문에 정확·간결하게 답함. 실습 난도를 조금 더 올려도 됨(리팩토링을 코드로 직접 쓰게).

관련: [[0004-polymorphism-ocp-grasped]]
