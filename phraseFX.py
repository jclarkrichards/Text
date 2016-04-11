import numpy as np

class ReadOut(object):
    def __init__(self, speed):
        self.timer = 0
        self.counter = 0
        self.phraseIndex = 0
        self.numCharacters = 1
        self.setSpeed(speed)

    def update(self, dt, phrase):
        if self.phraseIndex < len(phrase):
            self.counter += dt
            if self.counter >= self.timer:
                for i in range(self.numCharacters):
                    phrase[self.phraseIndex].alive = True
                    self.phraseIndex += 1
                    if self.phraseIndex >= len(phrase):
                        break
                self.counter = 0

    def setSpeed(self, speed):
        '''How fast to read out the characters'''
        if speed > 0:
            self.timer = 1.0/speed
        self.numCharacters = int(np.ceil(.03*speed))
        #.03 is 1/framesPerSec
