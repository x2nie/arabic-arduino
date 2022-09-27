from typing import List
import unicodedata
from .arabic_letters import individual_letters
from .arabic_ligatures import ligatures

# https://www.compart.com/en/unicode/block/U+FE70
# FIRST_HARAKAH = 0xFE70 
# LAST_HARAKAH = 0xFE7F 
FIRST_ARABIC = 0x0621 #HAMZAH
LAST_ARABIC = 0x064A #YEH

def spell(words:str):
    for s in words:
        print('\t', s, unicodedata.name(s))

def gundul(arabic_str:str)->str:
    print('  *** A 1:',FIRST_ARABIC)
    print('  *** A n:',LAST_ARABIC)
    ret = ''
    for c in arabic_str:
        print('  *** C:',ord(c), '@',c ,'>>',ret)
        # if ord(c) < FIRST_HARAKAH or ord(c) > LAST_HARAKAH:
        if FIRST_ARABIC <= ord(c) <= LAST_ARABIC:
            ret += c
        elif c == ' ':
            ret += c
    return ret


def get_plane(unicodeName:str, expectedPosition:str)->List[int]:
    "Return an ccg plane (byteArray)"
    initialExpected = expectedPosition
    block = individual_letters.get(unicodeName,None)
    if not block:
        return None
    while True:
        space = ' ~> ' if initialExpected != expectedPosition else ''
        print('\t\t %s unicodeName:' % space, unicodeName, 'expectedPosition:',expectedPosition)
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

def get_ligature_plane(unicodeName:str)->list:
    lig = ligatures[unicodeName]
    plane = lig['plane']
    if len(plane) <= 8:
        return [plane]
    else:
        count = len(plane) // 8 #? integer division
        planes = [[] for i in range(count)]
        for y in range(8):
            for x in range(count):
                planes[x].append( plane[ y * count +x ] )
        planes.reverse() #? RTL (right to left)
        return planes


def apply_ligatures(arabic_str:str)-> str:
    arabic_str = ' %s ' % arabic_str.strip()    #? ligature need trailing & prefix
    for lig in ligatures.values():
        match = lig['composed']
        while True:
            pos = arabic_str.find( match )
            if pos >= 0:
                print(' >before',arabic_str, '. >match:', match)
                count = len(match)
                #? replace chars with a ligature
                #? we can't use a simple str.replace() here because 
                #? arabic ligature is aware of space (initial, final)
                if match.startswith(' '):
                    pos += 1
                    count -= 1
                if match.endswith(' '):
                    count -= 1
                print('  @pos:',pos, 'count:',count, 'replacement:', lig['preview'])
                print('  $', repr(arabic_str[:pos]), '$', repr(arabic_str[pos+count:]) )
                arabic_str = arabic_str[:pos] + lig['preview'] + arabic_str[pos+count:]

                print(' =>after:', arabic_str, '\n')
            else:
                break
        
    return arabic_str

def empty_CGROM()->list:
    CGROM = []
    for i in range(8):
        CGROM.append({ 
            'charindex': None, 
            'plane': None,
        })
    return CGROM

def transformA2byte(arabic_str:str, CGROM:list)->list:
    "convert arabic string to byte-of-cgrom-index"
    arabic_str = arabic_str.strip()
    ret = []
    arabic_str = arabic_str.strip()
    words = arabic_str.split(' ')
    for iw,word in enumerate(words):
        if iw > 0:
            ret.append(' ')
        first = True
        for i,c in enumerate(word):
            uName = unicodedata.name(c)
            if uName in individual_letters:
                if len(word) == 1:
                    position = 'isolated'
                # elif i==0:
                elif first:
                    position = 'initial'
                    first = False
                elif c == ' ':
                    ret.append(' ')
                    first = True
                    continue
                elif i==len(word)-1:
                    position = 'final'
                else:
                    position = 'medial'
                ccg = get_plane(uName, position)
                ret.append(ccg)
            elif uName in ligatures:
                planes = get_ligature_plane(uName)
                ret.extend(planes)
            if uName == 'ARABIC LETTER ALEF':
                first = True
    return ret

def print_2x2(planes:list):
    LROM = planes #[self.ROM[i] if i != ord(' ') else ' ' for i in planes]
    for L in range(8):
        s = ''
        for c in range(len(LROM)):
            # if self.ROM[c]:
            if LROM[c]:
                r = LROM[c]
                if r == ' ':
                    # s += '          '
                    s += '00000  '
                    continue
                for x in range(5):
                    if r[L] & (1 << (4-x)) != 0:
                        s += '1'
                    else:
                        s += '0'
                s += '  '
        print(s.replace('0','░░').replace('1','██'))

def ccgs(arabic_str:str)->list:
    ret = []
    arabic_str = arabic_str.strip()
    words = arabic_str.split(' ')
    for iw,word in enumerate(words):
        if iw > 0:
            ret.append(' ')
        first = True
        for i,c in enumerate(word):
            uName = unicodedata.name(c)
            if len(word) == 1:
                position = 'isolated'
            # elif i==0:
            elif first:
                position = 'initial'
                first = False
            elif c == ' ':
                ret.append(' ')
                first = True
                continue
            elif i==len(word)-1:
                position = 'final'
            else:
                position = 'medial'
            ccg = get_plane(uName, position)
            ret.append(ccg)
            if uName == 'ARABIC LETTER ALEF':
                first = True
    return ret

