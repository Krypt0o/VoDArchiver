import requests
import json
import time
import subprocess
import os, shutil

#twitch Client-id und Secret
secret = ""
Client_ID = ""
broadcaster_name = "Streamername"
global res

def get_token():
    body = {"client_id": Client_ID, "client_secret": secret, "grant_type": "client_credentials"}
    response = requests.post("https://id.twitch.tv/oauth2/token", data=body)
    token_json = response.json()
    auth_token = token_json['access_token']
    global headers
    headers =  { "Client-ID": Client_ID ,"Authorization": "Bearer "+auth_token}
    return auth_token
        
        
def get_broadcaster_id():
    get_token()
    respo = requests.get("https://api.twitch.tv/helix/users?login="+broadcaster_name, headers=headers)
    resp = respo.json()
    broadcaster_id = resp['data'][0]['id']
    return broadcaster_id

def get_streamstatus():
    get_token()
    broadcaster_id = get_broadcaster_id()
    res = {'data': [], 'pagination': {}}
    while res['data']==[]:
        resp=requests.get(f"https://api.twitch.tv/helix/streams?user_id={broadcaster_id}", headers=headers)
        res = resp.json()
        if res['data']==[]:
            print("Stream Not Availble, 5m Sleep")
            time.sleep(300)
    print("API Request Succesfull")
    return res

def dataparse():
      print("create streamer.txt")
      f= open("streamer.txt","w+")
      f.write(broadcaster_name)


def Stream_Rec():
    print("call bash script")
    subprocess.call(["bash","/root/VoDArchiver/new_test.sh"])

def Remove_Streams():
    if os.path.isdir(broadcaster_name):
        shutil.rmtree(broadcaster_name)
