import subprocess
import webhook_listener
import optparse

streamer_name = webhook_listener.name_streamer

def stream_rec():
    p = subprocess.Popen(["powershell.exe", 
              "D:\\Marvin\\Documents\\Emiru.ps1"], 
              stdin=None, 
              stdout=None, 
              stderr=None, 
              close_fds=True)