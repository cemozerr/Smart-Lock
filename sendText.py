from twilio.rest import Client
import requests

TWILIO_ACCOUNT_SID = 'AC75fd9d7e943b776c2c26bc3acb524aee'
TWILIO_AUTH_TOKEN = '06c1c2b77aa4f5854ea6e04b9e7670f3'
TWILIO_NUMBER = '+16305213064'


def send_sms(to_number, body, filename):
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    twilio_number = TWILIO_NUMBER
    client = Client(account_sid, auth_token)

    # retreive ngrok public url
    r = requests.get('http://127.0.0.1:4040/api/tunnels')
    r = r.json()
    public_url = r['tunnels'][0]['public_url']
    media_url = public_url + '/uploads/' + filename

    client.api.messages.create(to_number,
                           from_=twilio_number,
                           body=body,
                           media_url=media_url)

send_sms(4082503360, 'test', 'cat.jpg')
