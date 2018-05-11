from twilio.rest import Client

TWILIO_ACCOUNT_SID = 'AC75fd9d7e943b776c2c26bc3acb524aee'
TWILIO_AUTH_TOKEN = '06c1c2b77aa4f5854ea6e04b9e7670f3'
TWILIO_NUMBER = '+16305213064'

def send_sms(to_number, body):
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    twilio_number = TWILIO_NUMBER
    client = Client(account_sid, auth_token)
    client.api.messages.create(to_number,
                           from_=twilio_number,
                           body=body)


send_sms(2245321001, 'abc')
