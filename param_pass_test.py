import webhook_listener
def dataparse():
    f= open("streamer.txt","w+")
    f.write(webhook_listener.name_streamer)
