import access_token
import requests
import json

CLIENT_ID     = "e15idce1efo9icb9xqfzkkt67zyola"
CLIENT_SECRET = "vi70jlbbl4bkg7a8g7q2ch8uq3gpnd"

header    = {"Client-ID": CLIENT_ID, "Authorization": f"Bearer {access_token.get_access_token()}"}

def sub_del():
    d = requests.delete("https://api.twitch.tv/helix/eventsub/subscriptions?id=38719911-7838-4015-beb2-e28d01daf28a", headers=header)
    
    return json.loads(r.text)

sub_del()


