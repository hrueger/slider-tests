from time import sleep
import RPi.GPIO as GPIO

DIR = 20   # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 48   # Steps per Revolution (360 / 7.5)
WORK = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(WORK, GPIO.OUT)
GPIO.output(DIR, CW)
GPIO.output(WORK, 1)

step_count = SPR*1000
delay = .0208

print("starting!")

#Microstepping Start
MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {1: (0, 0, 0),
              2: (1, 0, 0),
              4: (0, 1, 0),
              8: (1, 1, 0),
              16: (0, 0, 1),
              32: (1, 0, 1)}
currentMode = 1
speed = 0.02

GPIO.output(MODE, RESOLUTION[currentMode])


step_count = SPR * currentMode
#delay = .0208 / currentMode
delay = speed / currentMode
# microstepping end



for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR, CCW)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

GPIO.output(WORK, 0)
GPIO.cleanup()
print("finished!")
