def model(state):
    guess = state["last"] + 1
    return guess

def verify(guess):
    return guess >= 7

state = {"last": 0}

for step in range(10):                  # 4. REPEAT (+ 무한루프 가드: 최대 10회)
    guess = model(state)                # 1+2. GATHER 상태 → ACT 행동
    print(f"step {step}: tried {guess}")
    if verify(guess):                   # 3. VERIFY
        print("✅ 목표 달성, 루프 종료")
        break
    state["last"] = guess               # 피드백을 다음 회차 컨텍스트로
else:
    print("⛔ 10회 안에 못 풂 — 가드레일 작동")