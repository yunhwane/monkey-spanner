import re
import subprocess

LOG = "app.log"
THRESHOLD = 3            # 가드레일: 이 이상이면 사람/에이전트 개입


def count_errors():                       # 싼 검증: LLM 없이 정규식만 (Lesson 02)
    try:
        text = open(LOG).read()
    except FileNotFoundError:
        return 0
    return len(re.findall(r"ERROR", text))


def investigate():                        # 비싼 단계: 필요할 때만 진짜 에이전트 호출
    subprocess.run([
        "claude", "-p",
        f"{LOG}의 ERROR 로그들을 읽고 원인과 대응을 3줄로 요약해줘.",
        "--allowedTools", "Read",
        "--permission-mode", "acceptEdits",
    ])


def tick():                               # 루프의 '한 박자' (cron/interval이 주기적으로 호출)
    n = count_errors()
    print(f"ERROR {n}건 (임계값 {THRESHOLD})")
    if n >= THRESHOLD:                    # 객관적 신호로 분기
        print("⚠️ 임계값 초과 — Claude에게 조사 요청")
        investigate()
    else:
        print("✅ 정상")


if __name__ == "__main__":
    tick()                                # 한 번만 실행 (스케줄러가 반복을 담당)
