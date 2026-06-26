import requests

TOKEN = "8980796473:AAFY1OC7fRiJVfwp6lPdiv3qgm5Y35RoiXo"
CHAT_ID = "6067033565"

r = requests.get(
    f"https://api.telegram.org/bot8980796473:AAFY1OC7fRiJVfwp6lPdiv3qgm5Y35RoiXo/sendMessage",
    params={
        "chat_id": CHAT_ID,
        "text": "DEBUG"
    }
)

print(r.text)
