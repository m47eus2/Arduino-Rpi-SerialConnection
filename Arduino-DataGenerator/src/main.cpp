#include <Arduino.h>

// put function declarations here:
void serialLogging();

void setup() {
  Serial.begin(115200);
  randomSeed(analogRead(A0));
}

void loop() {
  serialLogging();
  delay(1000);
}

void serialLogging(){
  //Irms measurments
  Serial.print(">Irms0:");
  Serial.println(random(61));
  Serial.print(">Irms1:");
  Serial.println(random(61));
  Serial.print(">Irms2:");
  Serial.println(random(61));
  Serial.print(">Irms3:");
  Serial.println(random(61));
  Serial.print(">Irms4:");
  Serial.println(random(61));
  Serial.print(">Irms5:");
  Serial.println(random(61));
  Serial.print(">Irms6:");
  Serial.println(random(61));
  Serial.print(">Irms7:");
  Serial.println(random(61));
  Serial.print(">Irms8:");
  Serial.println(random(61));
  Serial.print(">Irms9:");
  Serial.println(random(61));

  //Combinatoins values
  Serial.print(">a:");
  Serial.println(random(61));
  Serial.print(">b:");
  Serial.println(random(61));
  Serial.print(">c:");
  Serial.println(random(61));
  Serial.print(">ab:");
  Serial.println(random(61));
  Serial.print(">ac:");
  Serial.println(random(61));
  Serial.print(">bc:");
  Serial.println(random(61));
  Serial.print(">abc:");
  Serial.println(random(61));

  //Combinatoins couters
  Serial.print(">a-counter:");
  Serial.println(random(10));
  Serial.print(">b-counter:");
  Serial.println(random(10));
  Serial.print(">c-counter:");
  Serial.println(random(10));
  Serial.print(">ab-counter:");
  Serial.println(random(10));
  Serial.print(">ac-counter:");
  Serial.println(random(10));
  Serial.print(">bc-counter:");
  Serial.println(random(10));
  Serial.print(">abc-counter:");
  Serial.println(random(10));
  Serial.print(">switching-counter:");
  Serial.println(random(10));

  //Phases sum
  Serial.print(">phase-0:");
  Serial.println(random(61));
  Serial.print(">phase-1:");
  Serial.println(random(61));
  Serial.print(">phase-2:");
  Serial.println(random(61));

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