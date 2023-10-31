import requests
import json
import access_token

header = {"Client-ID":access_token.CLIENT_ID, "Authorization":f"bearer {access_token.get_access_token()}"}


requests.delete("https://api.twitch.tv/helix/eventsub/subscriptions?id=5f8ce72d-a7c6-42bd-9451-061b602293e3", headers=header)
