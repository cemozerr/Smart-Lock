from flask import Flask, request, send_from_directory
from twilio.twiml.messaging_response import Message, MessagingResponse

app = Flask(__name__)

@app.route('/uploads/<filename>', methods=['GET', 'POST'])
def uploaded_file(filename):
    return send_from_directory('/Users/CemosBeast/Desktop/Projects/IoT/uploads',filename)

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
 
    resp = MessagingResponse() 
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    return str(resp)

if __name__ == "__main__":
    app.run(port=7777, debug=True)

