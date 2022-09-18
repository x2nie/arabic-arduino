from serial import Serial
DEBUG = 1

class LCD:
    def __init__(self, ser:Serial) -> None:
        self.ser = ser

    def send(self, s):
        if DEBUG: print('   send->', s.encode())
        self.ser.write(s.encode())

    def ccg(self, index, chars):
        self.send('ccg\n')
        while len(chars) < 8: chars += [0]
        chars = chars[:8]
        data = [index] + chars
        data = ''.join( [chr( (i << 1)+1 ) for i in data] )
        self.send(data)
