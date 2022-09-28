# from arabicArduino import LCD,Console, gundul
from arabicArduino.utils import * #gundul, spell, apply_ligatures
from arabicArduino.lcd_console import Console

def spells(arabic:str):
    a = gundul(arabic)
    print(a)
    print('-'*10)
    a = apply_ligatures(a)

    print('~'*10)
    print(a)

    print('='*10)
    spell(a)

    planes:List[List[int]] = transformA2PlanesRTL(a)        #? not unique, might containing SPACE

    CGROM = empty_CGROM()
    # #? make unique:
    # chars:List[int] = []
    # txt = []                #? chr 0..7
    # for p in planes:
    #     if p in chars:
    #         txt.append(chars.index(p))
    #     elif p == ' ':
    #         txt.append(0x20)
    #     else:
    #         chars.append(p)
    #         txt.append(chars.index(p))
    for p in planes:
        print(repr(p))
    planes.reverse()
    print_2x2(planes)


def spells2(arabic:str):
    a = gundul(arabic)
    print(a)
    print('-'*10)
    a = apply_ligatures(a)

    print('~'*10)
    print(a)

    print('='*10)
    spell(a)

    planes:List[List[int]] = transformA2PlanesRTL(a)        #? not unique, might containing SPACE
    for p in planes:
        print(repr(p))

    CGROM = empty_CGROM()
    # #? make unique:
    strA = build_CGROM(planes, CGROM)
    print('strA', '~'*10)
    print(strA)
    print('CGROM', '~'*10)
    print(CGROM)

    lcd = Console()
    for i,cc in enumerate(CGROM):
        if cc['active']:
            lcd.ccg(i, cc['plane'])

    print('writeArabic:',strA)
    lcd.writeArabic(strA)
    # planes.reverse()
    # print_2x2(planes)


# spells('بِسْمِ اللّٰهِ ')
# spells(' اللهم صَلِّ عَلى مُحَمَّدٍ')
# spells(' صلى الله عليه وسلم‎ ')
# spells(' صلى الله‎ ')

# spells(' صلى الله عَلى مُحَمَّدٍ‎ ')
# ░░░░██░░██  ██████░░░░  ░░░░░░░░░░  ░░░░░░░░██  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░  ██░░░░░░██  ░░░░░░░░░░  ░░░░░░░░██  ░░░░░░░░░░  
# ░░░░██░░██  ██░░██░░░░  ░░░░░░░░░░  ░░░░░░░░██  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░  ████░░░░██  ░░░░░░░░░░  ░░░░░░░░██  ░░░░░░░░░░  
# ░░░░██████  ██████░░░░  ░░░░░░░░░░  ░░░░░░░░██  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░██  ░░░░░░░░░░  ░░░░░░░░██  ░░██░░░░░░  
# ░░░░██░░░░  ██░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░██  ░░░░██████  ░░░░░░░░░░  ░░░░░░░░██  ██░░██░░██  ░░░░░░░░░░  ░░░░░░░░██  ░░████████  
# ░░░░██████  ██████░░░░  ░░░░░░░░░░  ██████░░██  ░░░░██░░░░  ░░░░░░░░░░  ░░░░██████  ██░░██░░██  ░░░░░░░░░░  ██████░░██  ░░██░░░░██  
# ░░░░██░░██  ░░░░██░░░░  ░░░░░░░░░░  ██░░██████  ██████████  ░░░░░░░░░░  ░░░░██░░██  ██░░██░░██  ░░░░░░░░░░  ██░░██████  ██████████  
# ░░░░██████  ██████░░░░  ░░░░░░░░░░  ██░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░██████  ██████░░██  ░░░░░░░░░░  ██░░░░░░░░  ░░░░░░░░░░  
# ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░  ██████████  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░  ██████████  ░░░░░░░░░░  


# spells2(' صلى الله عَلى مُحَمَّدٍ‎ ')
spells2(' اللهم صَلِّ عَلى مُحَمَّدٍ')