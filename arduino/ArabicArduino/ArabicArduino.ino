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

uint8_t bell[8]  = {0x4,0xe,0xe,0xe,0x1f,0x0,0x4};
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
};
  
LiquidCrystal_I2C lcd(0x27,20,4);  // set the LCD address to 0x27 for a 16 chars and 2 line display

String inBytes;

void setup()
{
  lcd.init();                      // initialize the lcd 
  lcd.backlight();
  
  lcd.createChar(0, bell);
  lcd.createChar(1, note);
  lcd.createChar(2, clock);
  lcd.createChar(3, heart);
  lcd.createChar(4, duck);
  lcd.createChar(5, check);
  lcd.createChar(6, cross);
  lcd.createChar(7, retarrow);
  lcd.home();
  
  lcd.print("Hello world...");
  lcd.setCursor(0, 1);
  lcd.print(" i ");
  lcd.printByte(3);
  lcd.printByte(4);
  lcd.printByte(5);
  lcd.printByte(6);
  lcd.printByte(7);
  lcd.printByte(1);
  lcd.printByte(0);
  lcd.print(" arduinos!");
  delay(5000);
  //displayKeyCodes();

  Serial.begin(9600);
  pinMode(LED_BUILTIN,OUTPUT);
  
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

void ccg() {
  //if ( Serial.available() == 9 )
  //{
    uint8_t index = Serial.read() >> 1;
    byte bytes[8];
    for ( uint8_t i = 0; i < 8; i++ )
      bytes[i] = Serial.read() >> 1;
    lcd.createChar(index, bytes);
  //}
}

void loop()
{
  if (Serial.available()>0){
    inBytes = Serial.readStringUntil('\n');
    lcd.setCursor(0, 3);
    lcd.print("       ");
    lcd.setCursor(0, 3);
    lcd.print(inBytes);
    
    if (inBytes == "on"){
      digitalWrite(LED_BUILTIN,HIGH);
    }
    if (inBytes == "off"){
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
    }
    if (inBytes == "ccg"){
      ccg();
    }
    
        
  }
}
