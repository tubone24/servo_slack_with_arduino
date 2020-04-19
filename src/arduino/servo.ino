#include <Servo.h>

const int SERVO_PIN = 9; //set Servo control pin number

int receiveByte = 0;
String bufferStr = "";

Servo servo; //declare Servo object

void setup() {
  servo.attach(SERVO_PIN);
  servo.write(90);
  Serial.begin(9600);
}

void loop() {
  // Receive PC serial comm
  bufferStr = "";
  while (Serial.available() > 0) {
    receiveByte = Serial.read();
    bufferStr.concat((char)receiveByte);
  }
  if (bufferStr.length() > 0) {
    servo.write(bufferStr.toInt());
  }
  delay(1000);
}
