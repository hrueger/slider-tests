from time import sleep
import pigpio

DIR = 20     # Direction GPIO Pin
STEP = 21    # Step GPIO Pin
WORK = 16
SLEEP = 12

# Connect to pigpiod daemon
pi = pigpio.pi()

# Set up pins as an output
pi.set_mode(DIR, pigpio.OUTPUT)
pi.set_mode(STEP, pigpio.OUTPUT)

# Set up input switch
pi.set_mode(WORK, pigpio.OUTPUT)
pi.write(WORK, 1)

modus = 0


MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins

RESOLUTION = {0: (0, 0, 0),
              1: (1, 0, 0),
              2: (0, 1, 0),
              3: (1, 1, 0),
              4: (0, 0, 1),
              5: (1, 0, 1)}


RESOLUTION = {0: (0, 0, 0),
              1: (1, 0, 0),
              2: (0, 1, 0),
              3: (1, 1, 0),
              4: (0, 1, 1),
              5: (1, 1, 1)}
for i in range(3):
    pi.write(MODE[i], RESOLUTION[modus][i])

pi.write(DIR,1)

### Set duty cycle and frequency
pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
###pi.set_PWM_frequency(STEP, 500)  # 500 pulses per second

import socket               # Import socket module

s = socket.socket()         # Create a socket object
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = "0.0.0.0"#socket.gethostname() # Get local machine name
port = 5000                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(1)

someoneConnected = False



try:
    while True:
        while someoneConnected:
            data = conn.recv(1024)
            if data:
                data = data.decode("utf-8") 
                #print("no data")
                data = data.split("\n",1)[0]
                if data == "DISCONNECT":
                    conn.close()
                    someoneConnected = False
                if data.startswith("speed:"):
                    speed = data[len("speed:"):]
                    speed = int(speed)
                    if (speed):
                        pi.set_PWM_frequency(STEP, speed*10)
                if data.startswith("status:"):
                    if data == "status:drive":
                        pi.write(WORK,1)
                        pi.write(SLEEP,1)
                    if data == "status:hold":
                        pi.write(WORK,0)
                        pi.write(SLEEP,1)
                    if data == "status:sleep":
                        pi.write(WORK,0)
                        pi.write(SLEEP,0)
                if data.startswith("Microstepping:"):
                    modus = data[len("Microstepping:"):]
                    print("Set Mode to:")
                    modus = int(modus)
                    
                    for i in range(3):
                        pi.write(MODE[i], RESOLUTION[modus][i])
                   
                    
                       
                    
                print(data)
        print("keiner verbunden!")
        conn, addr = s.accept()
        print('Got connection from', addr)
        someoneConnected = True

except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:
    pi.set_PWM_dutycycle(STEP, 0)  # PWM off
    pi.write(WORK, 0)
    pi.stop()



