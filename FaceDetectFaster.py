# import the necessary packages
from __future__ import print_function
from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import imutils
import time
import cv2
import sys
import RPi.GPIO as GPIO
from twilio.rest import Client

LEDPIN = 17
TWILIO_ACCOUNT_SID = 'AC75fd9d7e943b776c2c26bc3acb524aee'
TWILIO_AUTH_TOKEN = '06c1c2b77aa4f5854ea6e04b9e7670f3'
TWILIO_NUMBER = '+16305213064'
HOMEOWNER_NUMBER = '4082503360'

def send_sms(to_number, body):
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    twilio_number = TWILIO_NUMBER
    client = Client(account_sid, auth_token)
    client.api.messages.create(to_number,
                           from_=twilio_number,
                           body=body)

def sendTwilioMessage(message):
    print('sending twilio message:')
    send_sms(HOMEOWNER_NUMBER, message)

    #if approved
    return True

def unlockDoor():
    print('unlocking door...')
    GPIO.output(LEDPIN,True)

def main():
    currentlyMonitoring = True
    visitorEntered = True

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDPIN,GPIO.OUT)

    faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt2.xml')
     
    # initialize the camera and stream
    camera = PiCamera()
    camera.resolution = (320, 240)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(320, 240))
    stream = camera.capture_continuous(rawCapture, format="bgr",
            use_video_port=True)
    faceDetected = False

    for (i,f) in enumerate(stream):
        frame = f.array
        frame = imutils.resize(frame, width=400)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        
        # write image of detected face to uploads 
        if not faceDetected:
            for (x, y, w, h) in faces:
                faceDetected = True
                #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if faceDetected:
		print ("Saving face!")
                cv2.imwrite("./uploads/curr.jpg", frame)
            

#        if not currentlyMonitoring and not faceDetected:
#            visitorEntered = True
#            if(sendTwilioMessage('Your visitor has entered the house. Would you like to resume home monitoring?')):
#                currentlyMonitoring = True
#        elif currentlyMonitoring:
#            if faceDetected:
#                if(sendTwilioMessage('Here is a picture of your visitor, would you like to grant access?')):
#                    unlockDoor()
#                    break
#                    currentlyMonitoring = False
#                    visitorEntered = False
#                else:
#                    print('homeowner denied you access')
#            else:
#                GPIO.output(LEDPIN,False)
#        else:
#            print('Waiting for visitor to enter home')

        # check to see if the frame should be displayed to our screen
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        rawCapture.truncate(0)

if __name__ == "__main__":
    main()

    
    
