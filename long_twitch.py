import requests
import json

Streamer_name = input("For which Streamer do you want to create a Subscription: ")
CLIENT_ID = input("Enter your Client ID: ")
SECRET_ID = input("Enter your Secret ID: ")
Streamer_ID = input("Enter the ID of the Streamer you want to Subscribe to: ")

def get_access_token():
    x = requests.post(f"https://id.twitch.tv/oauth2/token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&grant_type=client_credentials")

    return json.loads(x.text)["access_token"]

header = {"Client-ID": CLIENT_ID, "Authorization":F"bearer {get_access_token()}"}

def subscription_create():
    s = requests.post("https://api.twitch.tv/helix/eventsub/subscriptions")