# Notes

## 사용자 프로필
- 언어: 한국어
- 수준: Claude Code 등 에이전트 도구 사용 경험 O, 루프 직접 구현 X ("써본 사용자")
- 학습 선호: **직접 만들며 배우기** — 레슨마다 작은 실습/실행 가능한 코드 포함할 것
- 목표: 자기 에이전트/자동화 직접 제작

## 교수 방침
- 레슨은 짧게, 한 번에 하나의 win. 워킹메모리 작게 유지.
- 코드 예시는 Python 의사코드/실제 실행 가능한 작은 스니펫 위주.
- 매 레슨 검증(verify) 개념 강조 — 미션 성공 기준의 핵심.

## 진행 상황
- 0001 에이전트 루프 (완료, coverage)
- 0002 검증 신호 설계 objective vs subjective (완료, coverage)
- 0003 종료 조건 & 가드레일, no-progress 감지 (완료, coverage)
- 0004 진짜 에이전트 = claude CLI를 model()로 (완료, coverage). 사용자가 CLI 사용 가능 여부를
  먼저 물어봄 → "이미 쓰는 도구를 루프에 끼운다"는 핵심을 스스로 연결함. 좋은 신호.

## 환경 사실
- claude CLI v2.1.196 설치됨 (/Users/jeonyh/.local/bin/claude). 헤드리스 -p 가능.
- --max-turns 플래그 이 버전엔 없음 → 바깥 루프 가드레일로 통제 (Lesson 03과 연결).

- 0004 demonstrated: 사용자가 agent_loop.py 실행 → solution.py add() 채워짐 (첫 진짜 에이전트 성공)
- 0005 모니터링 루프 (로그/모니터링 선택). 새 개념: 완수형 vs 모니터링 루프, LLM 게이팅, 스케줄러(/loop, cron)

- 0006 알림 & 상태 기억(중복 방지): seen.json durable memory, fingerprint 정규화, notify() 교체. 두 번 실행으로 검증됨.

## 다음에 가르칠 후보 (ZPD)
- 0007: 전체 합치기 + 안정성 (try/except, 재시도, 부분 실패 처리)
- 0008: --output-format json 파싱으로 정밀 분기 / 도구 정의

## 미확인 (demonstrated 대기)
- 사용자가 자기 실제 로그 패턴/임계값을 monitor.py에 적용하면 → 모니터링 루프 demonstrated + LR 추가

## ⚠️ 교수 메모
- 3개 레슨 연속 빠르게 진행 중(coverage만, demonstrated 아직 없음).
  Lesson 04 전에 사용자 실제 업무 1개를 끌어내서 "장난감 → 진짜 루프"로 전환 권장.
  계속 advance만 하면 fluency illusion 위험. 실제 적용 = storage strength.

## 미확인 (demonstrated 대기)
- 사용자가 자기 업무의 객관적 검증 신호를 말하면 → GLOSSARY 승격 + 학습기록 추가
