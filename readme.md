Twitch VoD Archiver

    Scripted Check for Onlinestatus of Twitch Channel
    Scripted Livestream Output into Local File of specified Twitch Channel
    Scripted Youtube upload of File to Archive Channel

    This Script was created to workaround the Problem that most Streamers use 2 different tracks for their stream
    and their VOD this script will live Record the Stream with all the sounds and music you wouldnt be 
    able to hear in the twitch VOD.

Installation

    Download Git Repo
    Install Streamlink (https://streamlink.github.io/index.html)
    Install Google API Module
        pip install --upgrade google-api-python-client
        pip install --upgrade google-auth-oauthlib google-auth-httplib2
        pip install oauth2client
        

Usage

    -Create your own Twitch app for Oauth2 Credentials via https://dev.twitch.tv/console/apps
        -insert Client-ID and Client-Secret into twt_functions.py
    -Specify Twitch Channel in twt_functions.py under broadcaster_name
    -Create new Project via https://console.cloud.google.com/
        -Create new Google app for Oauth2 Credentials
            -insert Client-ID and Secret from new Google App into client-secrets.json

    execute scriptstart.sh

    The script will now check the previously specified Twitch channel for Online State every 5 Minutes,
    if the Twtich Channel is online the script will extreact the title of the stream from the api response.
    The script also creates 2 textfiles, 1 with the name of the broadcaster and another with the stream title.
    Now the new_test.sh script will be called and will start to Live Record the Twitch Stream and output it into a file
    After the twitch Stream has ended, the Youtube Upload Script is called.
    You can change the paramters of the script call in new_test.sh to your liking.
    After the Upload Script is called the terminal will output a google link so it knows where to upload the video, 
    open the link in your browser an choose your channel.
    After that you will get a token, copy the token and input it into your terminal
    Now the Youtube Video will be uploaded

    !!IMPORTANT!!
    The Youtube Video will be set to Private, 
    if you want to upload unlisted or public Youtube Videos you have to go through a YouTube Audit to approve your API Projekt
    (https://support.google.com/youtube/contact/yt_api_form)
