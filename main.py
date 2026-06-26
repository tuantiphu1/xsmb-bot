import requests
from datetime import datetime

TOKEN = "8980796473:AAFY1OC7fRiJVfwp6lPdiv3qgm5Y35RoiXo"
CHAT_ID = "6067033565"

# API xổ số
data = requests.get("https://xoso-api.vercel.app/api/mb").json()

db = data["data"]["special_prize"]

today = datetime.now().strftime("%d/%m/%Y")

msg = f"🎯 XSMB {today}\n\nGiải đặc biệt: {db}"

requests.get(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    params={
        "chat_id": CHAT_ID,
        "text": msg
    }
)
