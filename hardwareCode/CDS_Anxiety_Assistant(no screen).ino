#include <IRremote.hpp>

const int RECV_PIN = 7;
const int buzzerPin = 6;

const int greenLED = 3;
const int redLED = 2;

IRrecv irrecv(RECV_PIN);
decode_results results;

void setup()
{
  Serial.begin(9600);
  IrReceiver.begin(RECV_PIN, ENABLE_LED_FEEDBACK); // Start the receiver
  
  pinMode(buzzerPin, OUTPUT);
  
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT); 
  
  digitalWrite(greenLED, HIGH);
  digitalWrite(redLED, HIGH);
  
  delay(1000);
  
  digitalWrite(greenLED, LOW);
  digitalWrite(redLED, LOW); 
}

void beepTwice()
{
  digitalWrite(buzzerPin, HIGH);
  delay(150);
  digitalWrite(buzzerPin, LOW);
  delay(150);
  digitalWrite(buzzerPin, HIGH);
  delay(150);
  digitalWrite(buzzerPin, LOW);
}

void teacherYesResponse()
{
  digitalWrite(greenLED, HIGH);
  digitalWrite(redLED, LOW);
  beepTwice();
  delay(2500);
  digitalWrite(greenLED, LOW);
}

void teacherNoResponse() // Given that buttons were not available, this is the response for when the teacher says no
{
  digitalWrite(redLED, HIGH);
  digitalWrite(greenLED, LOW);
  beepTwice();
  delay(150);
  beepTwice();
  delay(2500);
  digitalWrite(redLED, LOW);
}

void loop() {
  if (IrReceiver.decode()) 
  {
    switch(IrReceiver.decodedIRData.command) // Depending on the integer values that the IR remote returns, it outputs a message
    {
      // Different options for the bathroom, getting help, and reiterating what a teacher just said, will beep twice to notify the teacher
      case 12:
        Serial.println("Mohammad would like to go to the washroom");
        beepTwice();
        delay(5000);
        teacherYesResponse();
        break;
      case 24:
        Serial.println("Mohammad would like you to come and help");
        beepTwice();
        break;
      case 94:
        Serial.println("Mohammad would like you to reiterate what you just said");
        beepTwice();
        delay(150);
        beepTwice();
        delay(5000);
        teacherNoResponse();
        break;
      default:
        break;
    }
    
    IrReceiver.resume(); // Enable receiving of the next value
  }
  delay(100);
}