from typing import List
import unicodedata
from .arabic_letters import individual_letters

# https://www.compart.com/en/unicode/block/U+FE70
# FIRST_HARAKAH = 0xFE70 
# LAST_HARAKAH = 0xFE7F 
FIRST_ARABIC = 0x0621 #HAMZAH
LAST_ARABIC = 0x064A #YEH



def gundul(arabic_str:str)->str:
    print('  *** A 1:',FIRST_ARABIC)
    print('  *** A n:',LAST_ARABIC)
    ret = ''
    for c in arabic_str:
        print('  *** C:',ord(c), '@',c ,'>>',ret)
        # if ord(c) < FIRST_HARAKAH or ord(c) > LAST_HARAKAH:
        if FIRST_ARABIC <= ord(c) <= LAST_ARABIC:
            ret += c
    return ret


def get_plane(unicodeName:str, expectedPosition:str)->List[int]:
    "Return an ccg plane (byteArray)"
    block = individual_letters.get(unicodeName,None)
    if not block:
        return None
    while True:
        plane = block.get(expectedPosition)
        if plane is None: 
            if expectedPosition != 'isolated':
                expectedPosition = 'isolated'
            else:
                # isolated should never be empty
                # empty = no char
                break
        elif isinstance(plane, str):
            expectedPosition = plane
        elif isinstance(plane, list):
            break
        else:
            raise Exception('unknown plane:', str(plane))
    return plane


def ccgs(arabic_str:str)->list:
    ret = []
    for i,c in enumerate(arabic_str):
        uName = unicodedata.name(c)
        if len(arabic_str) == 1:
            position = 'isolated'
        elif i==0:
            position = 'initial'
        elif i==len(arabic_str)-1:
            position = 'final'
        else:
            position = 'medial'
        ccg = get_plane(uName, position)
        ret.append(ccg)
    return ret

