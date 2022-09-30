private_ligatures = {}
SELECTOR_START = 17   #? first use of UNICODE-NAME
UNICODE_START = 0x000e0100

temporary_ligatures = {
  "ALEF WITH LAM INITIAL FORM": {
    "compose": [' ', 'ا', 'ل'],
    "plane": [
      0b01010,
      0b01010,
      0b01010,
      0b01010,
      0b01010,
      0b11010,
      0b00000,
      0b00000,
    ],
  },  
  "ALEF WITH YEH WITH ALEF INITIAL FORM": {
    "breaker": True,
    "compose": [' ', 'ا',  'ي', 'ا' ],
    "plane": [
      0b10001,
      0b10001,
      0b10001,
      0b10101,
      0b10101,
      0b11101,
      0b00000,
      0b10100,
    ],
  }, 
  "YEH WITH ALEF ISOLATED FORM" : {
    "breaker": True,
    "compose": [' ', 'ي', 'ا' ],
    "plane": [
      0b01000,
      0b01000,
      0b01000,
      0b01001,
      0b01001,
      0b01111,
      0b00000,
      0b01010,
    ],
  },
  "YEH WITH NOON ISOLATED FORM" : {
    "compose": [' ', 'ي', 'ن', ' '],
    "preview": "󠄀ﲔ",
    "plane": [
      0b00000,0b00000,
      0b00000,0b00000,
      0b00000,0b00000,
      0b00100,0b00100,
      0b10001,0b11100,
      0b10001,0b00000,
      0b11111,0b10100,
      0b00000,0b00000,
    ],
    "plane-alt-3": [
      0b00000,0b00000,
      0b00000,0b00000,
      0b00000,0b00000,
      0b00100,0b00100,
      0b10001,0b11100,
      0b10001,0b00000,
      0b11111,0b00000,
      0b00000,0b10100,
    ],
    "plane-alt-2": [
      0b00000,0b00000,
      0b00000,0b00000,
      0b00000,0b00000,
      0b00100,0b00100,
      0b10001,0b00100,
      0b10001,0b11100,
      0b11111,0b00000,
      0b00000,0b10100,
    ],
    "plane-alt-1": [
      0b00000,0b00000,
      0b00000,0b00000,
      0b00000,0b00000,
      0b00100,0b00100,
      0b10001,0b00100,
      0b10001,0b11100,
      0b11111,0b00000,
      0b00000,0b01010,
    ],

  },
 
  "REH WITH ALEF":{
    "compose": ['ر', 'ا' ],
    "plane": [
      0b10000,
      0b10000,
      0b10000,
      0b10000,
      0b10001,
      0b10010,
      0b00010,
      0b01100,
    ],
  },  
  "ALEF WITH LAM WITH ALEF INITIAL FORM":{
    "compose": [' ', 'ا', "󠄀ﻻ"],
    "plane": [
      0b10101,
      0b10101,
      0b11101,
      0b01001,
      0b11101,
      0b10101,
      0b11101,
      0b00000,
    ],
  },  
  "ALEF WITH LAM MIDDLE FORM":{
    "compose": ['ا', 'ل'],
    "plane": [
      0b01010,
      0b01010,
      0b01010,
      0b01010,
      0b01010,
      0b11011,
      0b00000,
      0b00000,
    ],
  },  
  "NOON WITH ALEF INITIAL FORM":{
    "compose": [' ','ن' 'ا'],
    "plane": [
      0b10000,
      0b10000,
      0b10010,
      0b10000,
      0b10010,
      0b11110,
      0b00000,
      0b00000,
    ],
  },  
  "MEEM WITH ALEF INITIAL FORM":{
    "compose": [' ', 'م', 'ا'],
    "plane": [
      0b10000,
      0b10000,
      0b10000,
      0b10111,
      0b10101,
      0b11111,
      0b00000,
      0b00000,
    ],
  },  
  "MEEM WITH ALEF MEDIAL FORM":{
    "compose": ['+','م', 'ا'],
    "plane": [
      0b10000,
      0b10000,
      0b10000,
      0b10000,
      0b10111,
      0b11101,
      0b00111,
      0b00000,
    ],
  },  
  "MEEM WITH ALEF ANY FORM":{
    "compose": ['م', 'ا'],
    "plane": [
      0b10000,
      0b10000,
      0b10000,
      0b10111,
      0b10101,
      0b11111,
      0b00000,
      0b00000,
    ],
  },  
  "BEH WITH ALEF INITIAL FORM":{
    "compose": [' ', 'ب', 'ا'],
    "plane": [
      0b10000,
      0b10000,
      0b10000,
      0b10100,
      0b10100,
      0b11100,
      0b00000,
      0b00100,
    ],
  },  
  "BEH WITH LAM INITIAL FORM":{
    "compose": ['+', 'ب', 'ل', '+'],
    "plane": [
      0b01000,
      0b01000,
      0b01000,
      0b01000,
      0b01010,
      0b11111,
      0b00000,
      0b00010,
    ],
  },  
  "ALEF WITH WAW INITIAL FORM":{
    "compose": [' ', 'ا', 'و'],
    "plane": [
      0b00001,
      0b00001,
      0b00001,
      0b11101,
      0b10101,
      0b11101,
      0b00100,
      0b11100,
    ],
  },  
  "FEH WITH YEH ISOLATED FORM":{
    "compose": [' ', 'ف', 'ي', ' '],
    "plane": [
      0b10000,
      0b00111,
      0b00101,
      0b00111,
      0b00001,
      0b11111,
      0b10000,
      0b11111,
    ],
  },  
}


# preparing for string replace() later on LCD class
for i,name in enumerate(temporary_ligatures):
  lig = temporary_ligatures[name]
  lig['name'] = name
  lig['unicode'] = chr(UNICODE_START+i)
  lig['composed'] = ''.join(lig['compose'])
  key = 'VARIATION SELECTOR-%s' % (SELECTOR_START + i)
  private_ligatures[key] = lig