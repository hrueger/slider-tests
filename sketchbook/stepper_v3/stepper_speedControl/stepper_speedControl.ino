#include <Stepper.h>

//const int stepsPerRevolution = 512;
//Stepper myStepper(stepsPerRevolution, 11, 0);            

//int stepCount = 0;  // number of steps the motor has taken
//int motorSpeed = 0;
int time = 650;
byte[] message;

void setup() {
  // nothing to do inside the setup
  pinMode(11, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  //time = time - (time / 10);
  digitalWrite(11, HIGH); // sets the digital pin 13 on
  delayMicroseconds(300);            // waits for a second
  digitalWrite(11, LOW);  // sets the digital pin 13 off
  delayMicroseconds(time);            // waits for a second
  // read the sensor value:
  if (Serial.available()) {
        byte nr = Serial.read();
        Serial.print("Folgender char wurde empfangen: ");
        Serial.println(nr, DEC);
    }
    
  // map it to a range from 0 to 100:
  //int motorSpeed = map(sensorReading, 0, 1023, 0, 100);
  /*motorSpeed += 1;
  if (motorSpeed > 100) {
    motorSpeed = 100;
  }
  // set the motor speed:
  if (motorSpeed > 0) {
    myStepper.setSpeed(motorSpeed);
    // step 1/100 of a revolution:
    myStepper.step(1);
  }*/
  
  
}


