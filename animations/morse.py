import dcfurs
import settings
import time
CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }


class morse:
    def __init__(self, text=None):
        if text:
            self.text = text
        else:
            self.text = settings.banner
        self.dot = 1
        self.interval = 200
        self.dash = 3
        self.letterw = 3
        self.space = 7
        self.frame = 0
        self.frames=[]
        times = []
        for letter in self.text:
            self.morse2time(letter)

    def morse2time(self,letter):
        
        if letter == " ":
            self.frames = self.frames + ([False] * self.space)
        else:
            morse = CODE[letter]
            for dotdash in morse:
                if dotdash == ".":
                    self.frames = self.frames + ([1] * self.dot)
                else:
                    self.frames = self.frames + ([1] * self.dash)
                self.frames = self.frames + ([False] * self.dot)
            self.frames = self.frames + ([False] * self.letterw)
        
        
    def draw(self):
            dcfurs.clear()
            on = self.frames[self.frame]
            for x in range(0,8):
                for y in range(0,24):
                    dcfurs.set_pixel(y, x, on)
            self.frame += 1
            if (self.frame >= len(self.frames)):
                self.frame = 0