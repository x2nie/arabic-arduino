from .utils import *
from typing import List
from .lcd_serial import LCD

__all__ = ['Console']

class Console(LCD):
    def __init__(self, ser) -> None:
        self.ROM = []

    def send(self, s:bytearray):
        pass

    def send_cmd(self, cmd:str, data):
        raw = cmd.encode()
        if not isinstance(data, bytearray):
            data = bytearray(data)
        self.send(raw + data + '\n'.encode())

    def send_cmdSafe(self, cmd:str, data:List):
        self.send_cmd(cmd, data)