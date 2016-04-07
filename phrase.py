from base import Text
from vectors import Vector2D

class PhraseHandler(object):
    def __init__(self, phrase):
        self.phrase = phrase
        self.phraseList = []
        
    def setPhrase(self, lookup):
        for letter in self.phrase:
            try:
                self.phraseList.append(lookup[letter])
            except KeyError:
                pass
            
    def format(self, position=(0,0)):
        '''Format the phrase'''
        pass
    
    def print(self, screen):
        '''Print the phrase onto the screen'''
        pass
