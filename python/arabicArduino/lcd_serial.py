from time import sleep
from serial import Serial
from .utils import *
from typing import List

__all__ = ['LCD']

DEBUG = 1

class LCD:
    def __init__(self, ser:Serial) -> None:
        self.ser = ser
        self._init_cgrom()
        
    def _init_cgrom(self):
        self.CGROM = empty_CGROM()

    def send(self, s:bytearray):
        if DEBUG: print('   send->', s)
        self.ser.write(s)

    def send_cmd(self, cmd:str, data):
        raw = cmd.encode()
        if not isinstance(data, bytearray):
            data = bytearray(data)
        self.send(raw + data + '\n'.encode())

    def send_cmdSafe(self, cmd:str, data:List):
        data = [(i << 1)+1 for i in data]
        self.send_cmd(cmd, data)

    # def _cmd(self, s:str):
    #     self.send(s.strip() + '\n')

    def ccg(self, index:int, chars:List[int], asleep:float=0.5):
        "set a custom char new graphic"
        while len(chars) < 8: chars += [0]
        chars = chars[:8]
        data = [index] + chars
        # data = [(i << 1)+1 for i in data] 
        self.send_cmdSafe('ccg', data)
        sleep(asleep)

    def gotoxy(self, x:int, y:int):
        # self.cmd('goto')
        # self.send(chr((x<<1) + 1) + chr((y << 1) + 1))
        # self.send_cmd('@xy', [(x<<1) + 1, (y << 1) + 1])
        self.send_cmdSafe('@xy', [x,y])
        sleep(0.5)
    
    def writeln(self, s:str):
        # self.cmd('writeln')
        # self.send(chr(len(s)))
        self.send_cmd('prn', s.encode())

    def writeArabic(self, arabic_ints:List[int]):
        # self.cmd('writeAr')
        # self.send(chr(len(arabic_str)))
        # self.send(arabic_str)
        # data = ''.join([ chr( (ord(i)<<1)+1 ) for i in arabic_str ])
        arabic_ints.reverse()
        data = [len(arabic_ints)] + arabic_ints
        # data = [(i << 1)+1 for i in data] 
        # self.send_cmd('prA', data)
        self.send_cmdSafe('prA', data)

    def displayA(self, arabicWord: str):
        arabicWord = arabicWord.strip()
        s = gundul(arabicWord)
        print('gunduL', ' '.join([repr(a) for a in s]))
        planes:list = ccgs(s)        #? not unique, might containing SPACE
        print('ccgs:', planes)
        #? make unique:
        chars:List[int] = []
        txt = []                #? chr 0..7
        for p in planes:
            if p in chars:
                txt.append(chars.index(p))
            elif p == ' ':
                txt.append(0x20)
            else:
                chars.append(p)
                txt.append(chars.index(p))
        

        for i,c in enumerate(chars):
            self.ccg(i,c)
            # sleep(0.2)

        # self.gotoxy(0,0)
        sleep(2)
        print('writing Arabic:', txt)
        self.writeArabic(txt)

