import requests

TOKEN = "8980796473:AAFY1OC7fRiJVfwp6lPdiv3qgm5Y35RoiXo"
CHAT_ID = "6067033565"

try:
    r = requests.get("https://xoso-api.vercel.app/api/mb", timeout=10)

    msg = f"STATUS={r.status_code}\n\n{r.text[:1000]}"

except Exception as e:
    msg = str(e)

requests.get(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    params={
        "chat_id": CHAT_ID,
        "text": msg
    }
)
