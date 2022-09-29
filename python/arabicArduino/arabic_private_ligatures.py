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
    "plane-old": [
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
  "REH WITH ALEF":{
    "unicode": '\U000e0102',
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
   "ALEF WITH LAM MIDDLE FORM":{
    "unicode": '\U000e0103',
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
    "unicode": '\U000e0104',
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
}


# preparing for string replace() later on LCD class
for i,name in enumerate(temporary_ligatures):
  lig = temporary_ligatures[name]
  lig['name'] = name
  lig['unicode'] = chr(UNICODE_START+i)
  lig['composed'] = ''.join(lig['compose'])
  key = 'VARIATION SELECTOR-%s' % (SELECTOR_START + i)
  private_ligatures[key] = lig