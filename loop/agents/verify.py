import subprocess

def model(state):                 # 나중에 진짜 LLM으로 교체
    return state["v"] + 1         # "이번엔 이 값이 답일 것" 이라고 제안

def verify(candidate):            # ★ 객관적 신호: 환경이 판단하게 한다
    code = f"assert {candidate} % 3 == 0 and {candidate} > 0"
    r = subprocess.run(["python3", "-c", code])
    return r.returncode == 0      # exit 0 = 통과. 모델은 여기 개입 못 함.

state = {"v": 0}
for step in range(12):                       # 가드레일
    cand = model(state)
    print(f"step {step}: proposing {cand}")
    if verify(cand):                         # VERIFY = 사실 확인
        print(f"✅ {cand} 통과 (exit code 0)")
        break
    state["v"] = cand                        # 실패 → 피드백 → 다음 회차
else:
    print("⛔ 가드레일 작동")