private_ligatures = {
  "VARIATION SELECTOR-17" : { 'name':
  '''ALEF WITH LAM INITIAL FORM''',
    "unicode": '\U000e0100',
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
  "VARIATION SELECTOR-18" : { 'name':
  '''YEH WITH ALEF INITIAL FORM''',
    "unicode": '\U000e0101',
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
  "VARIATION SELECTOR-19" : { 'name':
  '''REH WITH ALEF''',
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
}


# preparing for string replace() later on LCD class
for key in private_ligatures:
  l = private_ligatures[key]
  l['composed'] = ''.join(l['compose'])