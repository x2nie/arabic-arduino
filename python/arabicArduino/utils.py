import math
from typing import Dict, List
import unicodedata

from .arabic_letters import individual_letters
from .arabic_ligatures import ligatures
from .arabic_private_ligatures import private_ligatures
from .dotmatrix_2x3 import char_2x3

#? merge ligatures
ligatures.update(private_ligatures)
breakers = [' ']
for name,letter in individual_letters.items():
    if letter.get('breaker'):
        breakers.append(unicodedata.lookup(name))

for name,lig in ligatures.items():
    if lig.get('breaker'):
        breakers.append(lig['unicode'])
    elif lig['composed'][-1] != ' ':
        if lig['composed'][-1] in breakers:
            breakers.append(lig['unicode'])
print('breakers:', breakers)

# https://www.compart.com/en/unicode/block/U+FE70
# FIRST_HARAKAH = 0xFE70 
# LAST_HARAKAH = 0xFE7F 
FIRST_ARABIC = 0x0621   #* = 1569 HAMZAH
LAST_ARABIC = 0x064A    #* = 1610 YEH
WHITE_LIST = [
    0x0671, #* ALEF WASLA

]

def spell(words:str):
    for s in words:
        name = unicodedata.name(s)
        if name.startswith('VARIATION '):
            s = ' '
            lig = private_ligatures.get(name)
            if lig and isinstance(lig, dict):
                name = lig.get('name', name)
        print('\t', s, name)

def gundul(arabic_str:str)->str:
    # print('  *** A 1:',FIRST_ARABIC)
    # print('  *** A n:',LAST_ARABIC)
    ret = ''
    for c in arabic_str:
        # print('  *** C:',ord(c), '[%s]' % unicodedata.name(c) , '@',c ,'>>',ret)
        # if ord(c) < FIRST_HARAKAH or ord(c) > LAST_HARAKAH:
        if (FIRST_ARABIC <= ord(c) <= LAST_ARABIC) or ord(c) in WHITE_LIST:
            ret += c
        elif c == ' ':
            ret += c
    return ret


def get_plane(unicodeName:str, expectedPosition:str)->List[int]:
    "Return an ccg plane (byteArray)"
    initialExpected = expectedPosition
    position = expectedPosition
    block = individual_letters.get(unicodeName,None)
    # breaker = False
    if not block:
        return (None)
    # breaker = block.get('breaker', False)
    while True:
        space = ' ~> ' if initialExpected != position else ''
        # print('\t\t %s unicodeName:' % space, unicodeName, 'expectedPosition:',expectedPosition)
        plane = block.get(position)
        if plane is None: 
            if position != 'isolated':
                position = 'isolated'
            else:
                # isolated should never be empty
                # empty = no char
                break
        elif isinstance(plane, str):
            position = plane
        elif isinstance(plane, list):
            break
        else:
            raise Exception('unknown plane:', str(plane))
    return plane
    # return (plane, breaker)

def get_ligature_plane(unicodeName:str)->list:
    lig = ligatures[unicodeName]
    plane = lig['plane']
    return plane

def split_if_multiple(plane:list)->List[List[int]]:
    if len(plane) <= 8:
        return [plane]
    else:
        count = len(plane) // 8 #? integer division
        planes = [[] for i in range(count)]
        # planes = [[]] * count
        for y in range(8):
            for x in range(count):
                planes[x].append( plane[ y * count +x ] )
        planes.reverse() #? RTL (right to left)
        return planes


def apply_breaked_ligatures(arabic_str:str, lig:dict)-> str:
# def apply_breaked_ligatures(arabic_str:str, pattern:str, unicode_char: str)-> str:
    "apply when ligature.pattern starts with a space | breaker"
    pattern=lig['composed']
    unicode_char = lig['unicode']
    match = pattern.lstrip()
    start = 0
    pos = arabic_str.find( match, start )
    while pos >= 0:
        # print('# apply_breaked_ligatures:', [repr(m) for m in match], '@', lig.get('name'))
        # print(' >before',arabic_str, '. >match:', match)
        count = len(match)
        #? replace chars with a ligature
        #? we can't use a simple str.replace() here because 
        #? arabic ligature is aware of space (initial, final)
        if arabic_str[pos -1 ] in breakers:
            if match.endswith(' '):
                count -= 1
            # print('  @pos:',pos, 'count:',count, 'replacement:', unicode_char)
            # print('  $', repr(arabic_str[:pos]), '$', repr(arabic_str[pos+count:]) )
            arabic_str = arabic_str[:pos] + unicode_char + arabic_str[pos+count:]

            # print(' =>after:', arabic_str, '\n')
        pos = arabic_str.find( match, pos+1 )
    return arabic_str

def apply_continued_ligatures(arabic_str:str, pattern:str, unicode_char: str)-> str:
    "apply when ligature.pattern is NOT (starts with a space | breaker)"
    match = pattern.lstrip('+ ')
    start = 0
    pos = arabic_str.find( match, start )
    while pos >= 0:
        # print('# apply_continued_ligatures')
        # print(' >before',arabic_str, '. >match:', match)
        count = len(match)
        #? replace chars with a ligature
        #? we can't use a simple str.replace() here because 
        #? arabic ligature is aware of space (initial, final)
        if not arabic_str[pos -1 ] in breakers:
            if match.endswith(' '):
                count -= 1
            # print('  @pos:',pos, 'count:',count, 'replacement:', unicode_char)
            # print('  $', repr(arabic_str[:pos]), '$', repr(arabic_str[pos+count:]) )
            arabic_str = arabic_str[:pos] + unicode_char + arabic_str[pos+count:]

            # print(' =>after:', arabic_str, '\n')
        pos = arabic_str.find( match, pos+1 )
    return arabic_str

def apply_middle_ligatures(arabic_str:str, pattern:str, unicode_char: str)-> str:
    "apply when ligature.pattern requests as middle"
    match = pattern.strip('+ ')
    count = len(match)
    start = 0
    pos = arabic_str.find( match, start )
    while pos >= 0:
        # print('# apply_middle_ligatures')
        # print(' >before',arabic_str, '. >match:', match)
        #? replace chars with a ligature
        #? we can't use a simple str.replace() here because 
        #? arabic ligature is aware of space (initial, final)
        if arabic_str[pos -1 ] not in breakers and arabic_str[pos + count ] != ' ':
            # print('  @pos:',pos, 'count:',count, 'replacement:', unicode_char)
            # print('  $', repr(arabic_str[:pos]), '$', repr(arabic_str[pos+count:]) )
            arabic_str = arabic_str[:pos] + unicode_char + arabic_str[pos+count:]

            # print(' =>after:', arabic_str, '\n')
        pos = arabic_str.find( match, pos+1 )
    return arabic_str


def apply_ligatures(arabic_str:str)-> str:
    arabic_str = ' %s ' % arabic_str.strip()    #? ligature need trailing & prefix
    for lig in ligatures.values():
        match:str = lig['composed']
        initial_form = match.startswith(' ')
        final_form = match.endswith(' ')
        medial_form = not initial_form and not final_form
        isolated_form = initial_form and final_form
        force_continue_form = match.startswith('+')
        force_midle_form = force_continue_form and match.endswith('+')
        if initial_form or isolated_form:
            # arabic_str = apply_breaked_ligatures(arabic_str, match, lig['unicode'])
            arabic_str = apply_breaked_ligatures(arabic_str, lig)
        elif force_midle_form:
            arabic_str = apply_middle_ligatures(arabic_str, match, lig['unicode'])
        elif force_continue_form:
            arabic_str = apply_continued_ligatures(arabic_str, match, lig['unicode'])
        else:
            pos = arabic_str.find( match )
            while  pos >= 0:
                # print('# apply_ligatures!!')
                # print(' >before',arabic_str, '. >match:', match)
                count = len(match)
                #? replace chars with a ligature
                #? we can't use a simple str.replace() here because 
                #? arabic ligature is aware of space (initial, final)
                if match.startswith(' '):
                    pos += 1
                    count -= 1
                if match.endswith(' '):
                    count -= 1
                # print('  @pos:',pos, 'count:',count, 'replacement:', lig['unicode'])
                # print('  $', repr(arabic_str[:pos]), '$', repr(arabic_str[pos+count:]) )
                arabic_str = arabic_str[:pos] + lig['unicode'] + arabic_str[pos+count:]

                # print(' =>after:', arabic_str, '\n')
                pos = arabic_str.find( match, pos +1 )

    arabic_str = arabic_str.replace('  ',' ')    
    return arabic_str

def empty_CGROM()->list:
    CGROM = []
    for i in range(8):
        CGROM.append({ 
            'active': False, 
            'plane': [],
        })
    return CGROM

def transformA2PlanesRTL(arabic_str:str)->List[List[int]]:
    "convert arabic string into list of cgrom"
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
                    if i < len(word) -1:
                        position = 'initial'
                    else:
                        position = 'isolated'
                    first = False
                # elif c == ' ':
                #     ret.append(' ')
                #     first = True
                #     continue
                elif i==len(word)-1:
                    position = 'final'
                else:
                    position = 'medial'
                ccg = get_plane(uName, expectedPosition= position)
                # ret.append(ccg)
                ret.extend(split_if_multiple(ccg))

                # if breaker:         #? back to initial form
                #     first = True
            elif uName in ligatures:
                plane = get_ligature_plane(uName)
                planes = split_if_multiple(plane)
                ret.extend(planes)
                first = False
            # if uName == 'ARABIC LETTER ALEF':
            if c in breakers:
                first = True
    return ret

def build_CGROM(planes:List[List[int]], CGROM:List[Dict])->List[int]:
    result = []
    pendingPlanes:List[List[int]] = []
    available = [cgrom['plane'] for cgrom in CGROM]     #? shadow for quick `in` operation
    for i,request_plane in enumerate(planes):
        if request_plane in available:
            index = available.index(request_plane)
            result.append(index)
            CGROM[index]['active'] = True
        elif isinstance(request_plane, str):
            # result.append(str(request_plane))
            result.append(ord(request_plane)) #? chr number of current char
        elif request_plane in pendingPlanes:
            pendingIndex = pendingPlanes.index(request_plane)
            result.append(str(pendingIndex))
        else:
            #? insert new plan to CGROM
            #* find empty slot
            #* find an empty slot
            for o,cgrom in enumerate(CGROM):
                if len(cgrom['plane']) != 0: 
                    continue
                cgrom['active'] = True  #? mark as `used`
                cgrom['plane'] = request_plane
                available[o] = request_plane
                result.append(o)
                break
            else:
                #* if not meet any empty slot, reuse non active, but should be later
                if request_plane in pendingPlanes:
                    pendingIndex = pendingPlanes.index(request_plane)
                else:
                    pendingPlanes.append(request_plane)
                    pendingIndex = pendingPlanes.index(request_plane)
                result.append(str(pendingIndex)) 
                # if cgrom['charindex'] is None:
    #? resolve pending planes
    print('PENDING:', pendingPlanes )
    for i,pending_plane in enumerate(pendingPlanes):
        #? insert new plan to CGROM
        #* find a non-actice plane
        for o,cgrom in enumerate(CGROM):
            if cgrom['active'] == True: 
                continue
            cgrom['active'] = True  #? mark as `used`
            cgrom['plane'] = pending_plane
            # result.append(o)
            replacing = str(i)  #? pending chr
            replacement = o     #? cgrom index
            for r,res in enumerate(result):
                if res == replacing:
                    result[r] = replacement
            break
        else:
            replacing = str(i)  #? pending chr
            for r,res in enumerate(result):
                if res == replacing:
                    result[r] = 'not-enough-for:'+replacing

    return result


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
        print(s.replace('0','??????').replace('1','??????'))


def print_LR_2x3(planes:list):
    "print planes from left to right with 2x3 dot per-char"
    rows_count = math.ceil(8.0/3.0)*3   #* should be 9
    
    #* draw bitmap
    rows = [0] * rows_count
    for x in range(len(planes)):
        #? SHL
        for y in range(rows_count):
            rows[y] = rows[y] << 6

        p = planes[x]
        if isinstance(p, list):
            while len(p) < rows_count:
                p.append(0)
        if not isinstance(p, list):
            pass
        else:
            #? draw.
            for y in range(rows_count):
                rows[y] += p[y]




        # print('-'*20)
        # for yy in range(rows_count): 
        #     print(bin(rows[yy]))
        # print('='*20)
        # print()


    # for yy in range(rows_count): 
    #     print(bin(rows[yy]))

    bitmap_width = len(planes) * (5+1)  #? 1 = gap between lcd char
    for yy in range(0,rows_count,3): #*[0,3,6]
        s = ''
        for xx in range(bitmap_width-2, -2,-2):
            n = 0
            for y in range(3):
                n += ((rows[yy+y] >> (xx)) & 0b11) << (y*2)
                # print(bin(n),'=',n,'> ', char_2x3[n])
            s += char_2x3[n][1]
            # print('^^^^^ xx:',xx,' n:',n, char_2x3[n])
        # print(s)
        print(repr(s))
        # break 

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

