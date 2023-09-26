
// WRITTEN BY EMIN AYYILDIZ

#include <Servo.h>

Servo girisServo;
Servo cikisServo;

int girisServoPin = 9;
int cikisServoPin = 10;

const int girisLedPingreen = 2;
const int girisLedPinred = 3;

const int cikisLedPingreen = 4;
const int cikisLedPinred = 5;

int kapasite = 15;

void setup() {
  Serial.begin(9600);

  girisServo.attach(girisServoPin);
  cikisServo.attach(cikisServoPin);

  pinMode(girisLedPingreen, OUTPUT);
  pinMode(girisLedPinred, OUTPUT);
  pinMode(cikisLedPingreen, OUTPUT);
  pinMode(cikisLedPinred, OUTPUT);

  // Başlangıçta kapıları kapat
  girisServo.write(0);
  cikisServo.write(0);
}

void loop() {
  if (Serial.available()) {
    String komut = Serial.readStringUntil('\n');
    komut.trim();

    if (komut.startsWith("GIRIS_AC")) {
      girisKapiAc();
    }
    else if (komut.startsWith("GIRIS_KAPAT")) {
      girisKapiKapat();
    }
    else if (komut.startsWith("CIKIS_AC")) {
      cikisKapiAc();
    }
    else if (komut.startsWith("CIKIS_KAPAT")) {
      cikisKapiKapat();
    }
  }
}

void girisKapiAc() {
  digitalWrite(girisLedPinred, LOW); 
  for (int derece = 0; derece <= 90; derece++) {
    girisServo.write(derece);
    delay(30); 
    if (derece % 15 == 0) {
      digitalWrite(girisLedPingreen, !digitalRead(girisLedPingreen));
    }
  }
  
  digitalWrite(girisLedPingreen, LOW); 
}

void girisKapiKapat() {
  digitalWrite(girisLedPingreen, LOW); 
  for (int derece = 90; derece >= 0; derece--) {
    girisServo.write(derece);
    delay(30); n gerekirse değeri değiştirin
    if (derece % 15 == 0) {
      digitalWrite(girisLedPinred, !digitalRead(girisLedPinred));
    }
  }
  digitalWrite(girisLedPinred, LOW); 
}

void cikisKapiAc() {
  digitalWrite(cikisLedPinred, LOW); 
  for (int derece = 0; derece <= 90; derece++) {
    cikisServo.write(derece);
    delay(30); 
    if (derece % 15 == 0) {
      digitalWrite(cikisLedPingreen, !digitalRead(cikisLedPingreen));
    }
  }
  
  digitalWrite(cikisLedPingreen, LOW); 
}

void cikisKapiKapat() {

  digitalWrite(cikisLedPingreen, LOW); 
  for (int derece = 90; derece >= 0; derece--) {
    cikisServo.write(derece);
    delay(30); 
    if (derece % 15 == 0) {
      digitalWrite(cikisLedPinred, !digitalRead(cikisLedPinred)); 
    }
  }
  digitalWrite(cikisLedPinred, LOW); 
}
