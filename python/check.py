# from arabicArduino import LCD,Console, gundul
from arabicArduino.utils import * #gundul, spell, apply_ligatures

def spells(arabic:str):
    a = gundul(arabic)
    print(a)
    print('-'*10)
    a = apply_ligatures(a)

    print('~'*10)
    print(a)

    print('='*10)
    spell(a)

    CGROM = empty_CGROM()
    planes:list = transformA2byte(a, CGROM)        #? not unique, might containing SPACE
    # print('ccgs:', planes)
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


# spells('بِسْمِ اللّٰهِ ')
# spells(' اللهم صَلِّ عَلى مُحَمَّدٍ')
# spells(' صلى الله عليه وسلم‎ ')
# spells(' صلى الله‎ ')
spells(' صلى الله عَلى مُحَمَّدٍ‎ ')

