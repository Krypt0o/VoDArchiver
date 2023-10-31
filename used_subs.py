import access_token
import requests
import json
CLIENT_ID     = "e15idce1efo9icb9xqfzkkt67zyola"
CLIENT_SECRET = "vi70jlbbl4bkg7a8g7q2ch8uq3gpnd"



header    = {"Client-ID": CLIENT_ID, "Authorization": f"Bearer {access_token.get_access_token()}"}

def total_sub():
    r = requests.get("https://api.twitch.tv/helix/eventsub/subscriptions", headers=header)
    return json.loads(r.text)

req = total_sub()
    
name_streamer1 = req["data"]
sub_total = name_streamer1["total"]
print(sub_total)
    


    


print(total_sub())

