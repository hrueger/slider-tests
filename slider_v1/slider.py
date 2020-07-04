from time import sleep
import RPi.GPIO as GPIO
from threading import Thread
import time
import sys


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Verwendete Pins am Rapberry Pi
A=4
B=17
C=23
D=24
#time = 0.005
#time = 0.0009 ### kleinste Zeit, am schnellsten
time = 1000

MinIn = 0
MaxIn = 10
MaxOut = 0.0009
MinOut = 0.05

MinToWantIn = 7.5

# Pins aus Ausgänge definieren
GPIO.setup(A,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
GPIO.setup(C,GPIO.OUT)
GPIO.setup(D,GPIO.OUT)
GPIO.output(A, False)
GPIO.output(B, False)
GPIO.output(C, False)
GPIO.output(D, False)

# Schritte 1 - 8 festlegen
def Step1(time):
    GPIO.output(D, True)
    sleep (time)
    GPIO.output(D, False)

def Step2(time):
    GPIO.output(D, True)
    GPIO.output(C, True)
    sleep (time)
    GPIO.output(D, False)
    GPIO.output(C, False)

def Step3(time):
    GPIO.output(C, True)
    sleep (time)
    GPIO.output(C, False)

def Step4(time):
    GPIO.output(B, True)
    GPIO.output(C, True)
    sleep (time)
    GPIO.output(B, False)
    GPIO.output(C, False)

def Step5(time):
    GPIO.output(B, True)
    sleep (time)
    GPIO.output(B, False)

def Step6(time):
    GPIO.output(A, True)
    GPIO.output(B, True)
    sleep (time)
    GPIO.output(A, False)
    GPIO.output(B, False)

def Step7(time):
    GPIO.output(A, True)
    sleep (time)
    GPIO.output(A, False)

def Step8(time):
    GPIO.output(D, True)
    GPIO.output(A, True)
    sleep (time)
    GPIO.output(D, False)
    GPIO.output(A, False)


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


def threadDrive(self):
    global time
    while True:
        #print("looping!")
        if time < 1000:
            #print("rotating with sleep for "+str(time))
            
            Step1(time)
        if time < 1000:
            Step2(time)
        if time < 1000:
            Step3(time)
        if time < 1000:
            Step4(time)
        if time < 1000:
            Step5(time)
        if time < 1000:
            Step6(time)
        if time < 1000:
            Step7(time)
        if time < 1000:
            Step8(time)
        else:
            #print("sleeping")
            sleep(0.2)
        

def threadUpdate(self):
    global time
    lastspeed = 0
    while True:
        with open("/var/www/html/sliderspeed") as f:
            
            try:
                value = f.read()
                #print(value)
                speed = float(value)
            except Exception as e:
                #print("Fehler: "+str(lastspeed))
                speed = lastspeed

                
            if speed == MinToWantIn:
                #print("speed = 0")
                time = 1000
            else:
                #print("speed != 0")
                time = translate(speed, MinIn, MaxIn, MinOut, MaxOut)
            lastspeed = speed
        
#GPIO.cleanup()


threadDrive = Thread( target=threadDrive, args=("Thread-1", ) )
threadUpdate = Thread( target=threadUpdate, args=("Thread-2", ) )
try:
    threadDrive.start()
    threadUpdate.start()

    threadDrive.join()
    threadUpdate.join()
except (Exception):
    sys.exit()
