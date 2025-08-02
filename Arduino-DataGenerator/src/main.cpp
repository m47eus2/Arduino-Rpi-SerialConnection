#include <Arduino.h>

// put function declarations here:
void serialLogging();

void setup() {
  Serial.begin(115200);
  randomSeed(analogRead(A0));
}

void loop() {
  serialLogging();
  delay(3000);
}

void serialLogging(){
  //Irms measurments
  Serial.print(">Irms0:");
  Serial.println(random(61));
 
  //Combinatoins values
  Serial.print(">a:");
  Serial.println(random(61));
  Serial.print(">b:");
  Serial.println(random(61));
  Serial.print(">c:");
  Serial.println(random(61));

  //Receivers total consumption
  Serial.print(">a-total:");
  Serial.println(30+random(31));
  Serial.print(">b-total:");
  Serial.println(30+random(31));
  Serial.print(">c-total:");
  Serial.println(30+random(31));

  //Connected receivers
  Serial.print(">a-state:");
  Serial.println(random(2));
  Serial.print(">b-state:");
  Serial.println(random(2));
  Serial.print(">c-state:");
  Serial.println(random(2));

  //Connected boilers
  Serial.print(">b0:");
  Serial.println(random(4));
  Serial.print(">b1:");
  Serial.println(random(4));
}