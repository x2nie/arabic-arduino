# from arabicArduino import LCD,Console, gundul
from arabicArduino.utils import gundul, spell, apply_ligatures

def spells(arabic:str):
    a = gundul(arabic)
    print(a)
    print('-'*10)
    a = apply_ligatures(a)

    print('~'*10)
    print(a)
    
    print('='*10)
    spell(a)


# spells('بِسْمِ اللّٰهِ ')
# spells(' اللهم صَلِّ عَلى مُحَمَّدٍ')
# spells(' صلى الله عليه وسلم‎ ')
spells(' صلى الله‎ ')

