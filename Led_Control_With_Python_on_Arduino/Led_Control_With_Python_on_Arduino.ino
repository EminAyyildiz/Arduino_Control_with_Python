int LED1_PIN = 5;
int LED2_PIN = 6;
int LED3_PIN = 7;

void setup() {
  pinMode(LED1_PIN, OUTPUT);
  pinMode(LED2_PIN, OUTPUT);
  pinMode(LED3_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') {
      digitalWrite(LED1_PIN, HIGH);
    } else if (command == '2') {
      digitalWrite(LED1_PIN, LOW);
    } else if (command == '3') {
      digitalWrite(LED2_PIN, HIGH);
    } else if (command == '4') {
      digitalWrite(LED2_PIN, LOW);
    } else if (command == '5') {
      digitalWrite(LED3_PIN, HIGH);
    } else if (command == '6') {
      digitalWrite(LED3_PIN, LOW);
    }
  }
}
