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
}


# preparing for string replace() later on LCD class
for key in private_ligatures:
  l = private_ligatures[key]
  l['composed'] = ''.join(l['compose'])