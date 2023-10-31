import requests
import json
import access_token
import used_subs

header = {"Client-ID":access_token.CLIENT_ID, "Authorization":f"Bearer {access_token.get_access_token()}"}

def del_sub():
    r = requests.delete(f"https://api.twitch.tv/helix/eventsub/subscriptions?id={}", headers=header)
    return json.loads(r.text)

print(del_sub())
