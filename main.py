import twt_functions
import time

stream_data = twt_functions.get_streamstatus()

if stream_data['data'] !=[]:
    f= open("title.txt","w+")
    f.write(stream_data['data'][0]['title'])
    f.close()
    twt_functions.dataparse()
    time.sleep(1)
    twt_functions.Stream_Rec()
    twt_functions.Remove_Streams()
else:
    print("Stream Data konnte nicht gefetched werden.")

