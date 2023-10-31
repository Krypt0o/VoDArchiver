import requests
import json
import access_token
import used_subs


streamer = input("Streamer Name eingeben: ")

CLIENT_ID     = "e15idce1efo9icb9xqfzkkt67zyola"
CLIENT_SECRET = "vi70jlbbl4bkg7a8g7q2ch8uq3gpnd"

header    = {"Client-ID": CLIENT_ID, "Authorization": f"Bearer {access_token.get_access_token()}"}

def emi_streamer_id():
    r = requests.get(f"https://api.twitch.tv/helix/users?login={streamer}", headers=header)
    return json.loads(r.text)["data"]

print(emi_streamer_id())
