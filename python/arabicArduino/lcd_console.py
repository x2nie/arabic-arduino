from .utils import *
from typing import List
from .lcd_serial import LCD

__all__ = ['Console']

class Console(LCD):
    def __init__(self, ser=None) -> None:
        self.ROM = [None]*8

    def send(self, s:bytearray):
        pass

    def send_cmd(self, cmd:str, data):        
        if cmd == 'prn':
            print(data)
        elif cmd == 'ccg':
            print('ROM:',self.ROM)
            self.ROM[data[0]] = data[1:]
        elif cmd == 'prA':
            for l in range(8):
                s = ''
                for c in range(8):
                    if self.ROM[c]:
                        r = self.ROM[c]
                        for x in range(5):
                            if r[l] & (1 << x) != 0:
                                s += '1'
                            else:
                                s += '0'
                print(s.replace('0','░').replace('1','█'))


    def send_cmdSafe(self, cmd:str, data:List):
        self.send_cmd(cmd, data)