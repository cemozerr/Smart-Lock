from flask import Flask, request, send_from_directory
from twilio.twiml.messaging_response import Message, MessagingResponse
import RPi.GPIO as GPIO


app = Flask(__name__)
LEDPIN = 2

def unlockDoor():
    print('unlocking door...')
    GPIO.output(LEDPIN,True)

def lockDoor():
    print("locking door...")
    GPIO.output(LEDPIN,False)

@app.route('/uploads/<filename>', methods=['GET', 'POST'])
def uploaded_file(filename):
    return send_from_directory('/home/pi/Desktop/Smart-Lock/uploads',filename)

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body'].strip()
 
    print(message_body)
    if (message_body == "Yes" or message_body == "yes" or message_body == "y"):
	unlockDoor()

    if (message_body == "No" or message_body == "no" or message_body == "n"):
        lockDoor()        

    return message_body



if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDPIN,GPIO.OUT)
    app.run(port=7777, debug=True)

