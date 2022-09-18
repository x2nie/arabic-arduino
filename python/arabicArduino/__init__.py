from time import sleep
from serial import Serial
from .utils import *
from typing import List

DEBUG = 1

class LCD:
    def __init__(self, ser:Serial) -> None:
        self.ser = ser

    def send(self, s:str):
        if DEBUG: print('   send->', s.encode())
        self.ser.write(s.encode())

    def cmd(self, s:str):
        self.send(s.strip() + '\n')

    def ccg(self, index:int, chars:List[int]):
        "set a custom char new graphic"
        self.cmd('ccg')
        while len(chars) < 8: chars += [0]
        chars = chars[:8]
        data = [index] + chars
        data = ''.join( [chr( (i << 1)+1 ) for i in data] )
        self.send(data)

    def gotoxy(self, x:int, y:int):
        self.cmd('goto')
        self.send(chr(x) + chr(y))
    
    def writeln(self, s:str):
        self.cmd('writeln')
        self.send(chr(len(s)))
        self.send(s)

    def writeArabic(self, arabic_str:str):
        self.cmd('writeAr')
        self.send(chr(len(arabic_str)))
        self.send(arabic_str)

    def displayA(self, arabicWord: str):
        s = gundul(arabicWord)
        planes:list = ccgs(s)        #? not unique
        print('ccgs:', planes)
        #? make unique:
        chars:List[int] = []
        txt = ''                #? chr 0..7
        for p in planes:
            if p in chars:
                txt += chr(chars.index(p))
            else:
                chars.append(p)
                txt += chr(chars.index(p))
        for i,c in enumerate(chars):
            self.ccg(i,c)
            sleep(0.2)

        self.gotoxy(0,0)
        self.writeArabic(txt)

