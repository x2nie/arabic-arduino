# from arabicArduino import LCD,Console, gundul
from arabicArduino.utils import gundul, spell, apply_ligatures

a = gundul('بِسْمِ اللّٰهِ ')
print(a)
print('-'*10)
a = apply_ligatures(a)
print('='*10)
spell(a)
