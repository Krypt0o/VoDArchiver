from flask import Flask , request, abort
import json
import requests
import streamlink_rec
import localtunnel
import param_pass_test

localtunnel.localtunnel()

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook(): 
    if request.method == "POST":
        x = request.json
        h = request.headers
        webhook_value = False
        if "webhook_callback_verification" in h.values():
            webhook_value = True
        if webhook_value == True:
            for code in x:
                v = x['challenge']
            print(v)
            return v, 200
        else:
            if webhook_value == False:
                name_streamer1 = x["event"]
                streamlink_rec.streamer_name = name_streamer1["broadcaster_user_name"]
                if streamlink_rec.streamer_name != "":
                    print(streamlink_rec.streamer_name)
                    print("vor param test")
                    streamlink_rec.dataparse()
                    streamlink_rec.Stream_Rec()
                    return streamlink_rec.streamer_name, 200
                else:
                    abort(400)
    else:
        abort(400)

if __name__ == "__main__":
    app.run(debug = True, port = 8080)