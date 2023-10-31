import requests
import json


CLIENT_ID     = "e15idce1efo9icb9xqfzkkt67zyola"
CLIENT_SECRET = "vi70jlbbl4bkg7a8g7q2ch8uq3gpnd"


def get_access_token():
    x = requests.post(f"https://id.twitch.tv/oauth2/token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&grant_type=client_credentials")

    return json.loads(x.text)["access_token"]

print(get_access_token())