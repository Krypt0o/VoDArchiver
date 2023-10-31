import subprocess

def localtunnel():
    p = subprocess.Popen(["powershell.exe", 
            "D:\\Twitch_Rec_Dev\\localtunnel.ps1"])