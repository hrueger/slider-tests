from time import sleep
import pigpio

DIR = 20     # Direction GPIO Pin
STEP = 21    # Step GPIO Pin
WORK = 16

# Connect to pigpiod daemon
pi = pigpio.pi()

# Set up pins as an output
pi.set_mode(DIR, pigpio.OUTPUT)
pi.set_mode(STEP, pigpio.OUTPUT)

# Set up input switch
pi.set_mode(WORK, pigpio.OUTPUT)
pi.write(WORK, 1)

modus = 8


MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
RESOLUTION = {1: (0, 0, 0),
              2: (1, 0, 0),
              4: (0, 1, 0),
              8: (1, 1, 0),
              16: (0, 0, 1),
              32: (1, 0, 1)}
for i in range(3):
    pi.write(MODE[i], RESOLUTION[modus][i])

pi.write(DIR,1)

# Set duty cycle and frequency
pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
pi.set_PWM_frequency(STEP, 500)  # 500 pulses per second

try:
    while True:
        #pi.write(DIR, pi.read(SWITCH))  # Set direction
        sleep(.5)

except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:
    pi.set_PWM_dutycycle(STEP, 0)  # PWM off
    pi.write(WORK, 0)
    pi.stop()



