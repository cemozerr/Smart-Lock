from matrix_keypad import RPi_GPIO
import time
import RPi.GPIO as GPIO

DOORPIN = 2

kp = RPi_GPIO.keypad()

def unlockDoor():
    print('unlocking door...')
    GPIO.output(DOORPIN,True)
    time.sleep(5)
    print('locking door...')
    GPIO.output(DOORPIN,False)

def getDigit():
    digitPressed = None
    while digitPressed == None:
        digitPressed = kp.getKey()
    return digitPressed

password = "3145"
digits = ""

GPIO.setmode(GPIO.BCM)
GPIO.setup(DOORPIN,GPIO.OUT)

while(1):
    digitPressed = getDigit()
    if(digitPressed == '*'):
        digits = ""
    elif(digitPressed == "#"):
        if(digits == password):
            print "Password valid!"
            unlockDoor()
        else:
            print "Invalid password!"    
        digits = ""
    else:
        digits = digits + str(digitPressed)
    print digits
    time.sleep(0.5)
