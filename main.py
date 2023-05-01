from twilio.rest import Client
from keys import auth_token, account_sid

client = Client(account_sid, auth_token)

body = input("Please enter the SMS content: ")
to_number = input("Please enter the recipient phone number: ")

message = client.messages.create(
    body=body,
    from_='+16205071687',
    to=to_number
)
print(message.sid)
