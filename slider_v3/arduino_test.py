
import serial
import time
 
s = serial.Serial('/dev/ttyACM0', 9600) # Namen ggf. anpassen
#s.open()
print("connection established, waiting")
time.sleep(5) # der Arduino resettet nach einer Seriellen Verbindung, daher muss kurz gewartet werden
print("write")

print("written")
##try:
##    while True:
##        response = s.readline()
##        print(response)
##        
##except KeyboardInterrupt:
##    s.close()






##quit()
### Set up pins as an output
##pi.set_mode(DIR, pigpio.OUTPUT)
###pi.set_mode(STEP, pigpio.OUTPUT)
###Arduino.pinMode(STEP, Arduino.OUTPUT)
##
### Set up input switch
##pi.set_mode(WORK, pigpio.OUTPUT)
##pi.write(WORK, 1)
##
##modus = 0
##
##
##MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
##
##RESOLUTION = {0: (0, 0, 0),
##              1: (1, 0, 0),
##              2: (0, 1, 0),
##              3: (1, 1, 0),
##              4: (0, 0, 1),
##              5: (1, 0, 1)}
##
##
##RESOLUTION = {0: (0, 0, 0),
##              1: (1, 0, 0),
##              2: (0, 1, 0),
##              3: (1, 1, 0),
##              4: (0, 1, 1),
##              5: (1, 1, 1)}
##for i in range(3):
##    pi.write(MODE[i], RESOLUTION[modus][i])
##
##pi.write(DIR,1)
##
#####pi.set_PWM_frequency(STEP, 500)  # 500 pulses per second

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
                data = data + ";"
                s.write(data.encode())
                
                   
                    
                       
                    
                print(data)
        print("keiner verbunden!")
        conn, addr = s.accept()
        print('Got connection from', addr)
        someoneConnected = True

except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping Serial and exiting...")
finally:
    s.close()

