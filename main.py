import requests
import re

TOKEN = "8980796473:AAFY1OC7fRiJVfwp6lPdiv3qgm5Y35RoiXo"
CHAT_ID = "6067033565"

url = "https://xoso.com.vn/xsmb-xo-so-mien-bac.html"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

# Tìm giải đặc biệt 5 số
match = re.search(r'jackpot[^>]*>\s*([0-9]{5})', html)

if match:
    db = match.group(1)
else:
    db = "Không lấy được kết quả"

msg = f"🎯 Giải đặc biệt XSMB hôm nay:\n{db}"

requests.get(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    params={
        "chat_id": CHAT_ID,
        "text": msg
    }
)
