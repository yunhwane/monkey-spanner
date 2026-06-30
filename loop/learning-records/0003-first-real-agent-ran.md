# 사용자가 첫 진짜 에이전트 루프를 성공적으로 실행함

Lesson 04 실습을 직접 돌려 `agents/solution.py`의 `add()`가 `return a + b`로 채워짐 →
사용자가 만든 루프가 claude CLI(model)를 호출하고 verify(객관적 신호)로 종료하는 전 과정을
실제로 작동시킴. 미션의 핵심("내 에이전트 만들기") 1차 달성.

## Implications
- 완수형 루프(model=CLI, verify=객관적, 가드레일)는 demonstrated. 재설명 불필요.
- 사용자 관심 = 로그/모니터링 → 모니터링 루프(시간 기반 + LLM 게이팅)로 확장(Lesson 05).
- 다음 자연스러운 확장: 알림 전송 + 상태 기억으로 중복 알림 방지(Lesson 06 후보).
