import requests
import json

url = "https://a2a3-109-192-194-188.ngrok.io"

data = {
        "challenge": "pogchamp-kappa-360noscope-vohiyo",
    "subscription": {
        "id": "f1c2a387-161a-49f9-a165-0f21d7a4e1c4",
        "status": "webhook_callback_verification_pending",
        "type": "channel.follow",
        "version": "1",
        "cost": 1,
        "condition": {
                "broadcaster_user_id": "12826"
        },
        "transport": {
            "method": "webhook",
            "callback": "https://example.com/webhooks/callback"
        },
        "created_at": "2019-11-16T10:11:12.123Z"
    }

}

r = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})