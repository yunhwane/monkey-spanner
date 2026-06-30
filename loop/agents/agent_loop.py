import subprocess


def claude(prompt):                          # model() = 진짜 에이전트 (Claude CLI)
    subprocess.run([
        "claude", "-p", prompt,
        "--allowedTools", "Edit", "Read",
        "--permission-mode", "acceptEdits",
    ])


def verify():                                # VERIFY = 객관적 신호 (Lesson 02)
    # pytest 없이 바로 실행되도록 테스트 함수를 직접 호출 → assert 통과면 exit 0.
    # 실무에선 보통 ["python3","-m","pytest","-q"] 로 교체. (ponytail: pytest 미설치 회피)
    r = subprocess.run(["python3", "-c", "from test_add import test_add; test_add()"])
    return r.returncode == 0                 # exit 0 = 통과


msg = "solution.py의 add() 함수를 구현해서 test_add.py가 통과하게 해줘."
for step in range(5):                          # 가드레일 (Lesson 03)
    print(f"\n=== step {step} ===")
    claude(msg)                                # GATHER + ACT
    if verify():                               # VERIFY
        print("✅ 테스트 통과 — 종료")
        break
    msg = "테스트가 아직 실패해. pytest 출력을 보고 add()를 고쳐줘."  # 피드백 (Lesson 01)
else:
    print("⛔ 5회 내 실패 — 가드레일 작동")
