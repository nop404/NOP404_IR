/*
  Serial Event example

  When new serial data arrives, this sketch adds it to a String.
  When a newline is received, the loop prints the string and clears it.

  A good test for this is to try it with a GPS receiver that sends out
  NMEA 0183 sentences.

  NOTE: The serialEvent() feature is not available on the Leonardo, Micro, or
  other ATmega32U4 based boards.

  created 9 May 2011
  by Tom Igoe

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/SerialEvent
*/
#include <IRremote.h>
String inputString = "";         // a String to hold incoming data
boolean stringComplete = false;  // whether the string is complete
IRsend irsend;
void setup() {
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
  pinMode(A5, INPUT);
  pinMode(A6, INPUT);
  pinMode(A7, INPUT);

  // initialize serial:
  Serial.begin(115200);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}


unsigned long  ircode_reverse(unsigned long src)
{
  //printf("%08X\n",src);
  Serial.println("----xxxxxxxxx----");
  Serial.print(src, HEX);
  src = ((src >> 1) & 0x55555555) | ((src & 0x55555555) << 1);
  src = ((src >> 2) & 0x33333333) | ((src & 0x33333333) << 2);
  src = ((src >> 4) & 0x0F0F0F0F) | ((src & 0x0F0F0F0F) << 4);
  src = ((src >> 8) & 0x00FF00FF) | ((src & 0x00FF00FF) << 8);
  src = (src >> 16) | (src << 16);

  src = (((src & 0xff000000) >> 24) | ((src & 0x00ff0000) >> 8) | ((src & 0x0000ff00) << 8) | ((src & 0x000000ff) << 24));
  Serial.println("------------");
  Serial.print(src, HEX);
  src = (src << 8) + (0xFF - (src & 0xFF));
  Serial.println("........");
  Serial.print(src, HEX);
  return src;
}

void loop() {
  unsigned char i;
  unsigned char datalen;
  unsigned long  remotecode;
  unsigned long  temp;
  // print the string when a newline arrives:
  if (stringComplete) {
    if (inputString.length() == 2)
    {
      Serial.println(inputString);
      pinMode(A0, INPUT);
      pinMode(A1, INPUT);
      pinMode(A2, INPUT);
      pinMode(A3, INPUT);
      pinMode(A4, INPUT);
      pinMode(A5, INPUT);
      pinMode(6, INPUT);
      pinMode(7, INPUT);
      switch (inputString[0]) {
        case '0':
          pinMode(7, OUTPUT);
          digitalWrite(7, LOW);
          Serial.println("K0");
          break;
        case '1':
          pinMode(6, OUTPUT);
          digitalWrite(6, LOW);
          Serial.println("K1");
          break;

        case '2':
          pinMode(A5, OUTPUT);
          digitalWrite(A5, LOW);
          Serial.println("K2");
          break;
        case '3':
          pinMode(A4, OUTPUT);
          digitalWrite(A4, LOW);
          Serial.println("K3");
          break;
        case '4':
          pinMode(A3, OUTPUT);
          digitalWrite(A3, LOW);
          Serial.println("K4");
          break;
        case '5':
          pinMode(A2, OUTPUT);
          digitalWrite(A2, LOW);
          Serial.println("K5");
          break;
        case '6':
          pinMode(A1, OUTPUT);
          digitalWrite(A1, LOW);
          Serial.println("K6");
          break;
        case '7':
          pinMode(A0, OUTPUT);
          digitalWrite(A0, LOW);
          Serial.println("NULL");
          break;
        default:
          pinMode(A0, INPUT);
          pinMode(A1, INPUT);
          pinMode(A2, INPUT);
          pinMode(A3, INPUT);
          pinMode(A4, INPUT);
          pinMode(A5, INPUT);
          pinMode(6, INPUT);
          pinMode(7, INPUT);
          break;
      }
       delay(500);
          pinMode(A0, INPUT);
          pinMode(A1, INPUT);
          pinMode(A2, INPUT);
          pinMode(A3, INPUT);
          pinMode(A4, INPUT);
          pinMode(A5, INPUT);
          pinMode(6, INPUT);
          pinMode(7, INPUT);
          
      inputString = "";
      stringComplete = false;
    }
    else if (inputString.length()==7)
    {
      datalen = inputString.length() - 1;
      Serial.println(datalen);
      for (i = 0; i < datalen; i++)
      {
        if (inputString[i] >= 'a')
        {
          temp = (inputString[i] - 'a' + 10);
          Serial.println(temp);
          remotecode += (temp << ((datalen - 1 - i) * 4));
        } else if (inputString[i] >= 'A')
        {
          temp = (inputString[i] - 'A' + 10);
          Serial.println(temp);
          remotecode += (temp << ((datalen - 1 - i) * 4));
        }
        else
        {
          temp = (inputString[i] - '0');
          remotecode += (temp << ((datalen - 1 - i) * 4));
        }
      }

      irsend.sendNEC(ircode_reverse(remotecode), 32);
      remotecode = 0;
      inputString = "";

      stringComplete = false;
    }else {
       remotecode = 0;
      inputString = "";
       Serial.println("Data Error");
        stringComplete = false;
      }
  }
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/


void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
     Serial.println(inputString);
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
