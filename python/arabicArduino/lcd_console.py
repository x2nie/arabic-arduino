from .utils import *
from typing import List
from .lcd_serial import LCD

__all__ = ['Console']

class Console(LCD):
    def __init__(self, ser=None) -> None:
        self.ROM = [None]*8

    def send_cmd(self, cmd:str, data):        
        if cmd == 'prn':
            print(data)
        elif cmd == 'ccg':
            print('ROM:',self.ROM)
            self.ROM[data[0]] = data[1:]
        elif cmd == 'prA':
            w = data[0]
            data = data[1:w+1]
            LROM = [self.ROM[i] if i != ord(' ') else ' ' for i in data]
            for L in range(8):
                s = ''
                for c in range(len(LROM)):
                    # if self.ROM[c]:
                    if LROM[c]:
                        r = LROM[c]
                        if r == ' ':
                            s += '    '
                            continue
                        for x in range(5):
                            if r[L] & (1 << (4-x)) != 0:
                                s += '1'
                            else:
                                s += '0'
                        s += ' '
                print(s.replace('0','░░').replace('1','██'))


    def send_cmdSafe(self, cmd:str, data:List):
        self.send_cmd(cmd, data)

    def send(self, s:bytearray):
        pass

    def ccg(self, index:int, chars:List[int], asleep:float=0.5):
        super().ccg(index, chars, 0)
