#include <IRremote.hpp>
int RECV_PIN = 7;
IRrecv irrecv(RECV_PIN);
decode_results results;
void setup()
{
Serial.begin(9600);
IrReceiver.begin(RECV_PIN, ENABLE_LED_FEEDBACK); // Start the receiver
}
void loop() {
if (IrReceiver.decode()) {
Serial.println(results.value, HEX); // Print "old" raw data
/* USE NEW 3.x FUNCTIONS */
IrReceiver.printIRResultShort(&Serial); // Print complete received data in one line
IrReceiver.printIRSendUsage(&Serial); // Print the statement required to send this data
IrReceiver.resume(); // Enable receiving of the next value
}
delay(100);
}
