import re
import json
import hashlib
import subprocess  # noqa: F401  (실무에서 Slack/메일 전송 시 사용)
from pathlib import Path

LOG = "app.log"
SEEN = Path("seen.json")          # ★ 틱 사이를 잇는 durable memory (DB 대신 파일 하나)


def errors():
    try:
        text = open(LOG).read()
    except FileNotFoundError:
        return []
    return re.findall(r"^.*ERROR.*$", text, re.M)


def fingerprint(line):            # 같은 '종류'의 에러를 같게 본다: 숫자/타임스탬프 제거 후 해시
    norm = re.sub(r"\d+", "#", line)
    return hashlib.sha1(norm.encode()).hexdigest()[:10]


def load_seen():
    return set(json.loads(SEEN.read_text())) if SEEN.exists() else set()


def save_seen(seen):
    SEEN.write_text(json.dumps(sorted(seen)))


def notify(msg):                  # 알림 채널 — 지금은 출력+파일, 실무선 Slack/메일로 교체
    print("🔔 ALERT:", msg)
    with open("alerts.log", "a") as f:
        f.write(msg + "\n")
    # 실무 예시 (Slack incoming webhook):
    # subprocess.run(["curl", "-sX", "POST", "-H", "Content-type: application/json",
    #                 "-d", json.dumps({"text": msg}), SLACK_WEBHOOK_URL])


def tick():
    seen = load_seen()
    new = [e for e in errors() if fingerprint(e) not in seen]
    if not new:
        print("✅ 새 에러 없음 (이미 본 에러는 무시)")
        return
    for e in new:
        notify(e.strip())
        seen.add(fingerprint(e))
    save_seen(seen)               # 기억 저장 → 다음 틱부터 같은 에러는 알리지 않음


if __name__ == "__main__":
    tick()
