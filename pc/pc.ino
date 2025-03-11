#define red 9 
#define yelow 7
#define green 5
#define buttonPin 11
bool buttonState = false;
void setup() {
  Serial3.begin(9600);
  Serial.begin(9600);
  pinMode(11,INPUT_PULLUP);
  pinMode(9,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(5,OUTPUT);
  digitalWrite(5,1);
  digitalWrite(7,1);
  digitalWrite(9,1);
  delay(1000);
  digitalWrite(5,0);
  digitalWrite(7,0);
  digitalWrite(9,0);
}

void loop() {
  if (digitalRead(buttonPin) == LOW && !buttonState) { 
    buttonState = true;
    Serial3.println("B:1#"); 
    delay(500); 
  } else if (digitalRead(buttonPin) == HIGH && buttonState) { 
    buttonState = false;
    Serial3.println("B:0#"); 
    delay(500); 
  }
  
  if (Serial3.available() > 0) {
    String response = Serial3.readStringUntil('\n');
    response.trim();
    if (response == "whating") {
      digitalWrite(red, HIGH);
      digitalWrite(yelow, LOW);
      digitalWrite(green, LOW);
    } else if (response == "worck") {
      digitalWrite(red, LOW);
      digitalWrite(yelow, HIGH);
      digitalWrite(green, LOW);
    } else if (response == "done") {
      digitalWrite(red, LOW);
      digitalWrite(yelow, LOW);
      digitalWrite(green, HIGH);
    } 
  }
}
