import os
import requests
from TikTokLive import TikTokLiveClient
from TikTokLive.events import CommentEvent

N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "PASTE_N8N_WEBHOOK_URL_HERE")
TIKTOK_USERNAME = os.getenv("TIKTOK_USERNAME", "@YOUR_TIKTOK_USERNAME")

if "PASTE_" in N8N_WEBHOOK_URL or "YOUR_" in TIKTOK_USERNAME:
    raise SystemExit("Set N8N_WEBHOOK_URL and TIKTOK_USERNAME before running.")

client = TikTokLiveClient(unique_id=TIKTOK_USERNAME)

@client.on(CommentEvent)
async def on_comment(event: CommentEvent):
    payload = {
        "user_id": event.user.unique_id,
        "nickname": event.user.nickname,
        "comment": event.comment,
        "room_id": str(client.room_id or "")
    }
    try:
        response = requests.post(N8N_WEBHOOK_URL, json=payload, timeout=10)
        print(response.status_code, payload)
    except requests.RequestException as exc:
        print("n8n request failed:", exc)

if __name__ == "__main__":
    print(f"Listening to {TIKTOK_USERNAME}...")
    client.run()
