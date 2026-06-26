import requests

TOKEN = "8980796473:AAFY1OC7fRiJVfwp6lPdiv3qgm5Y35RoiXo"
CHAT_ID = "6067033565"

msg = "Test gửi Telegram"

requests.get(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    params={
        "chat_id": CHAT_ID,
        "text": msg
    }
)
