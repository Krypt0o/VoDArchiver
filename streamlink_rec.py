import subprocess

import optparse

streamer_name = ""

def dataparse():
      
      f= open("streamer.txt","w+")
      f.write(streamer_name)


def Stream_Rec():
        p = subprocess.Popen(["powershell.exe", 
              "D:\\Twitch_Rec_Dev\\new_test.ps1"], 
              stdin=None, 
              stdout=None, 
              stderr=None, 
              close_fds=True)
