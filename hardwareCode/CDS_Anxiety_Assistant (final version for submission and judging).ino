// Libraries needed for anxiety assistant function
#include <IRremote.hpp>

// Pin assignments
const int RECV_PIN = 7;
const int buzzerPin = 6;

const int greenLED = 8;
const int redLED = 9;

IRrecv irrecv(RECV_PIN);
decode_results results;

void setup()
{
  Serial.begin(9600);
  
  Serial.println("Welcome to the ESE Anxiety Asisstant!");
  
  //lcd.begin(16, 2);
  
  //lcd.print("Hello world");
  
  IrReceiver.begin(RECV_PIN, ENABLE_LED_FEEDBACK); // Start the receiver
  
  // Sets up output devices
  pinMode(buzzerPin, OUTPUT);
  
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT); 
  
  // Test for output devices 
  
  digitalWrite(greenLED, HIGH);
  digitalWrite(redLED, HIGH);
  
  digitalWrite(buzzerPin, LOW);
  
  delay(2000);
  
  digitalWrite(greenLED, LOW);
  digitalWrite(redLED, LOW); 
  
  digitalWrite(buzzerPin, LOW);
}


// Beeps buzzer twice for notifications
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

// Below are yes and no responses, as physical buttons were not available to control the yes and no functions on the teachers end
void teacherYesResponse()
{
  digitalWrite(greenLED, HIGH);
  digitalWrite(redLED, LOW);
  beepTwice();
  Serial.println("Mohammad's request has been allowed");
  delay(2500);
  digitalWrite(greenLED, LOW);
}

void teacherNoResponse()
{
  digitalWrite(redLED, HIGH);
  digitalWrite(greenLED, LOW);
  beepTwice();
  Serial.println("Mohammad's request has not been allowed");
  delay(150);
  beepTwice();
  delay(2500);
  digitalWrite(redLED, LOW);
}

// Receives IR sensing from input off remote
void loop() {
  if (IrReceiver.decode()) 
  {
    switch(IrReceiver.decodedIRData.command) // Depending on the integer values that the IR remote returns, it outputs a message
    {
      // Different options for the bathroom, getting help, and reiterating what a teacher just said, will beep twice to notify the teacher
      case 12: // Button 1
        Serial.println("Mohammad would like to go to the washroom");
        beepTwice();
        delay(3000);
        teacherYesResponse();
        break;
        
      case 24: // Button 2 
        Serial.println("Mohammad would like you to come and help");
        beepTwice();
        delay(3000);
        teacherNoResponse();
        break;
        
      case 94: // Button 3
        Serial.println("Mohammad would like you to reiterate what you just said");
        beepTwice();
        delay(150);
        beepTwice();
        delay(3000);
        teacherYesResponse();
        break;
        
      default:
        break;
    }
    
    IrReceiver.resume(); // Enable receiving of the next value
  }
  delay(100);
}