ligatures = {
  "ARABIC LIGATURE LAM WITH ALEF MAKSURA ISOLATED FORM" : {
    "unicode": '\uFC43',
    "compose": [' ','ل', 'ى', ' '],
    "preview": "ﱃ",
    "plane": [
      0b00001,
      0b00001,
      0b00001,
      0b00001,
      0b11101,
      0b10111,
      0b10000,
      0b11111,
    ],
  },
  "ARABIC LIGATURE LAM WITH ALEF MAKSURA FINAL FORM" : {
    "unicode": '\uFC86',
    "compose": ['ل', 'ى', ' '],
    "preview": "ﲆ",
    "plane": [
      0b00001,
      0b00001,
      0b00001,
      0b00001,
      0b11101,
      0b10111,
      0b10000,
      0b11111,
    ],
  },
  "ARABIC LIGATURE LAM WITH YEH FINAL FORM" : {
    "unicode": '\uFC87',
    "compose": ['ل', 'ي', ' '],
    "preview": "ﲇ",
    "plane": [
      0b00001,
      0b00001,
      0b00001,
      0b00001,
      0b11101,
      0b10111,
      0b10000,
      0b11011,
    ],
  },
  "ARABIC LIGATURE ALLAH ISOLATED FORM" : {
    "compose": [' ', 'ا', 'ل', 'ل', 'ه', ' '],
    "preview": "ﷲ",
    "unicode": '\uFDF2',
    "plane": [
      0b00000,0b10001,
      0b00000,0b11001,
      0b00000,0b00001,
      0b00001,0b10101,
      0b00111,0b10101,
      0b00101,0b10101,
      0b00111,0b11101,
      0b00000,0b00000,
    ],
    "plane-alt-2": [
      0b00001,0b00010,
      0b00011,0b00010,
      0b00000,0b00010,
      0b00101,0b01010,
      0b11101,0b01010,
      0b10101,0b01010,
      0b11111,0b11010,
      0b00000,0b00000,
    ],
    "plane-alt-1": [
      0b00001,0b00010, 
      0b00011,0b00010, 
      0b00000,0b00010, 
      0b00101,0b01010, 
      0b11101,0b01010, 
      0b10101,0b01010, 
      0b11111,0b11010, 
      0b00000,0b00000, 
    ],
  },
  "ARABIC LIGATURE MOHAMMAD ISOLATED FORM" : {
    "compose": [' ', 'م','ح','م','د', ' '],
    "preview": "ﷴ",
    "unicode": '\uFDF4',
    "plane": [
      0b00101,0b11100,
      0b00101,0b10100,
      0b00111,0b11100,
      0b00100,0b10000,
      0b00111,0b11100,
      0b00101,0b00100,
      0b00111,0b11100,
      0b00000,0b00000,
    ],
    "plane-alt-1": [
      0b01011,0b00000,
      0b01010,0b01110 ,
      0b01010,0b01010 ,
      0b01110,0b01110 ,
      0b01000,0b00100 ,
      0b01110,0b11111 ,
      0b01010,0b00001 ,
      0b01111,0b11111 ,
    ],
  },
  "ARABIC LIGATURE LAM WITH HEH INITIAL FORM" : {
    "compose": [' ','ل', 'ه'],
    "preview": "ﳍ",
    "unicode": '\uFCCD',
    "plane": [
      0b00001,
      0b00001,
      0b00001,
      0b11101,
      0b10101,
      0b11111,
      0b10100,
      0b11100
    ],
  },
  "ARABIC LIGATURE YEH WITH MEEM FINAL FORM" : {
    "compose": ['ي', 'م', ' '],
    "preview": "󠄀ﲓ",
    "unicode": '\uFC93',
    "plane": [
      0b00000,
      0b00000,
      0b00000,
      0b11101,
      0b10101,
      0b11111,
      0b10000,
      0b10101,
    ],
    "plane-alt-1": [
      0b00000,
      0b00000,
      0b00000,
      0b11111,
      0b10101,
      0b11101,
      0b10000,
      0b10101,
    ],
  }, 
  "ARABIC LIGATURE LAM WITH ALEF ISOLATED FORM" : {
    "compose": [ 'ل',  'ا',   ' '],
    "preview": "󠄀ﻻ",
    "unicode": '\uFEFB',
    "plane": [
      0b01010,
      0b01010,
      0b01110,
      0b00100,
      0b01110,
      0b01010,
      0b01110,
      0b00000,
    ],
   
  },
}


# preparing for string replace() later on LCD class
for key in ligatures:
  l = ligatures[key]
  l['composed'] = ''.join(l['compose'])