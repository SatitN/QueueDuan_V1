import os, requests
from flask import Blueprint, request

notify_bp = Blueprint("notify", __name__)
LINE_TOKEN = os.getenv("LINE_NOTIFY_TOKEN")

def send_notify(msg):
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {LINE_TOKEN}"}
    data = {"message": msg}
    requests.post(url, headers=headers, data=data)

@notify_bp.route("/", methods=["POST"])
def notify_now():
    msg = request.json.get("message", "Hello from QueueDuan!")
    send_notify(msg)
    return {"status": "sent"}

@notify_bp.route("/summary", methods=["GET"])
def daily_summary():
    # ใช้ utils ไปดึงข้อมูลแล้วสรุปเป็น string
    from utils import get_summary_text
    send_notify(get_summary_text())
    return {"status": "summary_sent"}
