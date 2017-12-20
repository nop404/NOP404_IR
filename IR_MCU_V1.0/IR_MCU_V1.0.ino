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
  // initialize serial:
  Serial.begin(115200);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}


  unsigned long  ircode_reverse(unsigned long src)
    {
        //printf("%08X\n",src);
          Serial.println("----xxxxxxxxx----");
        Serial.print(src,HEX);
        src=((src>>1)&0x55555555)|((src&0x55555555)<<1);
        src=((src>>2)&0x33333333)|((src&0x33333333)<<2);
        src=((src>>4)&0x0F0F0F0F)|((src&0x0F0F0F0F)<<4);
        src=((src>>8)&0x00FF00FF)|((src&0x00FF00FF)<<8);
        src=(src>>16)|(src<<16);
       
        src= (((src & 0xff000000) >> 24) | ((src & 0x00ff0000) >> 8) | ((src & 0x0000ff00) << 8) | ((src & 0x000000ff) << 24));
        Serial.println("------------");
        Serial.print(src,HEX);
        src=(src<<8)+(0xFF-(src&0xFF));
         Serial.println("........");
        Serial.print(src,HEX);
        return src;
    }
    
void loop() {
  unsigned char i;
  unsigned char datalen;
  unsigned long  remotecode;
  unsigned long  temp;
  // print the string when a newline arrives:
  if (stringComplete) {
 
   // Serial.println(inputString);

  //  String2Hex((&inputString);
    // clear the string:
    //Serial.println(inputString.length());
    datalen=inputString.length()-1;
   Serial.println(datalen);
    for(i=0;i<datalen;i++)
    {
     if(inputString[i]>='a')
     {
     temp=(inputString[i]-'a'+10);
        Serial.println(temp);
        remotecode+=(temp<<((datalen-1-i)*4));
      }else if(inputString[i]>='A')
      {
       temp=(inputString[i]-'A'+10);
        Serial.println(temp);
        remotecode+=(temp<<((datalen-1-i)*4));
        }
       else
       {
       temp=(inputString[i]-'0');
       remotecode+=(temp<<((datalen-1-i)*4));
        }
    }

   //remotecode=0x00FD00FF;
   //Serial.println(remotecode);
 
   
   irsend.sendNEC(ircode_reverse(remotecode),32);
    remotecode=0;
    inputString = "";
   
    stringComplete = false;
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
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
