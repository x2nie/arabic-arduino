//YWROBOT
//Compatible with the Arduino IDE 1.0
//Library version:1.1
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#if defined(ARDUINO) && ARDUINO >= 100
#define printByte(args)  write(args);
#else
#define printByte(args)  print(args,BYTE);
#endif

/*uint8_t bell[8]  = {0x4,0xe,0xe,0xe,0x1f,0x0,0x4};
uint8_t note[8]  = {0x2,0x3,0x2,0xe,0x1e,0xc,0x0};
uint8_t clock[8] = {0x0,0xe,0x15,0x17,0x11,0xe,0x0};
uint8_t heart[8] = {0x0,0xa,0x1f,0x1f,0xe,0x4,0x0};
uint8_t duck[8]  = {0x0,0xc,0x1d,0xf,0xf,0x6,0x0};
uint8_t check[8] = {0x0,0x1,0x3,0x16,0x1c,0x8,0x0};
uint8_t cross[8] = {0x0,0x1b,0xe,0x4,0xe,0x1b,0x0};
uint8_t retarrow[8] = {	0x1,0x1,0x5,0x9,0x1f,0x8,0x4};

byte smile[] = {
  B00000,
  B00000,
  B01010,
  B00000,
  B00000,
  B10001,
  B01110,
  B00000
};*/
  
LiquidCrystal_I2C lcd(0x27,20,4);  // set the LCD address to 0x27 for a 16 chars and 2 line display

String inBytes;
String lastBytes;

void setup()
{
  lcd.init();                      // initialize the lcd 
  lcd.backlight();
  
  /*lcd.createChar(0, bell);
  lcd.createChar(1, note);
  lcd.createChar(2, clock);
  lcd.createChar(3, heart);
  lcd.createChar(4, duck);
  lcd.createChar(5, check);
  lcd.createChar(6, cross);
  lcd.createChar(7, retarrow);*/
  lcd.home();
  
  //lcd.print("Hi world...");
  //lcd.setCursor(0, 1);
  //lcd.print("[ ");
  lcd.printByte(0);
  lcd.printByte(1);
  lcd.printByte(2);
  lcd.printByte(3);
  lcd.printByte(4);
  lcd.printByte(5);
  lcd.printByte(6);
  lcd.printByte(7);
  lcd.print(">");
  delay(50);
  //displayKeyCodes();

  Serial.begin(9600);
  //Serial.setTimeout(10);
  //pinMode(LED_BUILTIN,OUTPUT);
  
}

// display all keycodes
void displayKeyCodes(void) {
  uint8_t i = 0;
  while (1) {
    lcd.clear();
    lcd.print("Codes 0x"); lcd.print(i, HEX);
    lcd.print("-0x"); lcd.print(i+15, HEX);
    lcd.setCursor(0, 1);
    for (int j=0; j<16; j++) {
      lcd.printByte(i+j);
    }
    i+=16;
    
    delay(4000);
  }
}

bool ccg(String data) {
  if ( data.length() == 9 ) {
    byte buffer[data.length() + 1];
    data.getBytes(buffer, data.length() + 1);    
    uint8_t index = buffer[0] >> 1;
    byte bytes[8];
    for ( uint8_t i = 0; i < 8; i++ )
      bytes[i] = buffer[1+i] >> 1;
    lcd.createChar(index, bytes);
    return true;
  }
  return false;
}

void gotoxy() {
 if ( Serial.available() >= 2 ) {
    uint8_t x = Serial.read() >> 1;
    uint8_t y = Serial.read() >> 1;
    lcd.setCursor(x, y);
    lcd.print(" ");
    lcd.setCursor(x, y);
 }
}


void writeLn() {
  int incomingByte = Serial.read();
  char buf[20];
  int len = Serial.readBytes(buf, incomingByte);
  lcd.print(buf);
}
void writeAr() {
  if ( Serial.available() >= 1 ) {
    int incomingBytes = Serial.read();
    if ( Serial.available() == incomingBytes ) {
      for ( uint8_t i = 0; i < incomingBytes; i++ ) {
        uint8_t incomingByte = Serial.read() >> 1;
        lcd.printByte(incomingByte);
      }
    }
    lcd.print(" ");
  }
}

String data;
String cmd;
byte buf[16]; 

void loop()
{
  if (Serial.available()>0){
    data = Serial.readStringUntil('\n');
    cmd = data.substring(0,3);
    data = data.substring(3);
    if (cmd == "prn"){
      lcd.print(data);
    }
    else if (cmd == "ccg") {
      ccg(data);
    }

    Serial.println(cmd);
    Serial.println(data);
      
//    lcd.print(cmd);
//    lcd.print("<.");
//    lcd.print(data);

    // if (lastBytes != "goto") {
    // lcd.setCursor(0, 2);
    // lcd.print(" ");
    // lcd.setCursor(0, 2);
    // }
    // lcd.print(inBytes);
    // lastBytes = inBytes;
    
    /*if (inBytes == "on"){
      digitalWrite(LED_BUILTIN,HIGH);
    }
    else if (inBytes == "off"){
      digitalWrite(LED_BUILTIN,LOW);
    }
    if (inBytes == "smile"){
      lcd.createChar(0, smile);
    }
    if (inBytes == "bell"){
      lcd.createChar(0, bell);
    }
    if (inBytes == "clock"){
      lcd.createChar(0, clock);
    }*/
    // if (inBytes == "ccg"){
    //   ccg();
    // }
    // if (inBytes == "goto"){
    //   gotoxy();
    // }
    // if (inBytes == "writeln"){
    //   writeLn();
    // }
    // if (inBytes == "writeAr"){
    //   writeAr();
    // }
  }
}
