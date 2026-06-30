def model(state):
    return min(state["v"] + 1, 5)     # 일부러 5에 막히는 가짜 에이전트 (목표=8)

def score(candidate):                 # 진전을 '점수'로 잰다 (pass/fail보다 풍부한 신호)
    return candidate                  # 높을수록 목표에 가까움

state, best, stale = {"v": 0}, -1, 0
for step in range(50):                         # 가드레일 ①: 절대 상한
    cand = model(state)
    s = score(cand)
    print(f"step {step}: score {s}  (best {best}, stale {stale})")
    if s >= 8:
        print("✅ 성공 종료"); break
    if s > best:
        best, stale = s, 0                     # 진전 있음 → 카운터 리셋
    else:
        stale += 1                             # 진전 없음 → 누적
    if stale >= 3:                             # 가드레일 ②: 무진전 감지
        print(f"⛔ 3회 연속 무진전 (best={best}) — 조기 포기"); break
    state["v"] = cand