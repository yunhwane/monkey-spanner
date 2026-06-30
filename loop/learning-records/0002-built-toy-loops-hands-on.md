# 사용자가 Lesson 01–03 실습을 직접 손으로 수행함

`agents/` 폴더에 사용자가 직접 만든 `loop.py`(L1, verify를 `guess >= 7`로 수정),
`verify.py`(L2), `guard.py`(L3)가 발견됨. 단순 읽기(coverage)가 아니라 실제로 코드를
작성·실행하며 따라온 증거 — fluency를 넘어 storage strength로 가는 신호.

## Implications
- 루프 골격(gather/act/verify/repeat), 가드레일, 검증 신호 개념은 이제 *demonstrated*.
  → GLOSSARY/치트시트의 해당 용어를 신뢰하고 이후 레슨에서 그대로 사용.
- 다음 단계는 장난감 → 실제 업무 전환(Lesson 05)이 확실히 적절. 기초 재설명 불필요.
- pytest 미설치 환경 → 실습 코드는 의존성 없이 돌아가게 유지할 것.
