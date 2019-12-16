import os
from twilio.rest import Client

account_sid = os.environ("Twilio_account_sid")
auth_token = os.environ("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

call = client.calls.creat(
    to=os.environ[""],
    from_="+",
    url="http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)
