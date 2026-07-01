# Tell, Don't Ask / 캡슐화를 스스로 적용함

Lesson 02 실습에서 ask 스타일(`order.getStatus().equals("PAID") && !order.getShippedFlag()`)을
tell 스타일로 스스로 전환. 판단(isReadyToShip)과 상태 변경(markShipped) 로직을 모두 Order 안으로 옮김.
캡슐화의 "행동을 노출한다" 개념이 적용 단계에 도달.

## Evidence
- readyToShip() 판단 메서드 + shipped() 상태변경 메서드로 정확히 분리
- 미세 격차: boolean 네이밍(is/can 접두사), 상태변경 동사(mark~) 관례는 상기시켜줄 것

## Implications
- 캡슐화 기초 완료. 반복보다 진행.
- 다음: 다형성 — if/else if 분기(grade == VIP ...)를 객체가 스스로 골라 행동하게. 캡슐화의 자연스러운 다음 수순.
- 네이밍 감각(질문 vs 명령)이 자라는 중. 앞으로도 이름 짓기 피드백을 계속 줄 것.

관련: [[0002-applies-extract-method]]
