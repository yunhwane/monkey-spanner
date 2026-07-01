# 실제 JDK 코드를 원칙 렌즈로 정확히 읽어냄 — 미션 핵심 목표 달성

Lesson 06 실습에서 실제 `employees.sort(comparing().thenComparing(...))` 한 줄을 분석: 전략 패턴/주입, thenComparing=조합,
sort 불변=OCP를 정확히 짚음. 결정적으로 L05의 오적용(원칙 남발)과 달리 이번엔 "실제로 성립하는 것만" 선별 —
"적용 조건" 감각이 자리 잡았음을 증명.

## Evidence
- 세 원칙(전략/DIP, 조합, OCP)을 정확·간결하게 매핑
- L06 misconception(LR-0006) 대비 뚜렷한 개선: 과적용 없음
- 교사가 보강: 전략패턴=DIP 동일장면, 중첩 조합(reverseOrder), OCP를 "인자 교체"로 설명

## Implications
- 미션 3목표(설명/진단·리팩토링/오픈소스 분석) 모두 최소 1회 달성. 코스 1차 아크 완료.
- 지금까지 6개 레슨을 한 세션에 몰아서 진행 → **저장 강도(storage strength)를 위해 간격 복습 필요**.
  다음 세션은 새 진도보다 인터리빙 복습 퀴즈(L01~L06 혼합)를 먼저 권장.
- 향후 방향 후보: (a) 디자인 패턴을 SOLID 레시피로, (b) Spring 등 실제 프로젝트 리딩, (c) 면접 모의 Q&A.
- 학습자 특성: 개념→코드 전이 빠름, 판단형 질문 강함. 난도 상향 여지 있음.

관련: [[0006-solid-diagnosis-misconception]]
