import os
from twilio.rest import Client

account_sid = os.environ("Twilio_account_sid")
auth_token = os.environ("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

call = client.calls.creat(
    to=os.environ["8007827282"],
    from_="+16137022431",
    url="http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)