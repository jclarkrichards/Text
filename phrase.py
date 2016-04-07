from base import Text
from vectors import Vector2D

class PhraseHandler(object):
    def __init__(self, phrase):
        self.phrase = phrase
        self.phraseList = []
        
    def setPhrase(self, lookup):
        '''Get all of the character images to construct the phrase'''
        for letter in self.phrase:
            try:
                self.phraseList.append(lookup[letter])
            except KeyError:
                pass
            
    def setPosition(self, position):
        '''Set the position relative to the first letter'''
        for i, letter in enumerate(self.phraseList):
            letter.setPosition((position[0]+letter.size[0]*i, position[1]))
            
    def setScale(self, scale):
        '''Make the letters bigger or smaller'''
        for letter in self.phraseList:
            newSize = (letter.size[0]*scale, letter.size[1]*scale)
            pygame.transform.scale(letter, newSize)
    
    def print(self, screen):
        '''Print the phrase onto the screen'''
        for letter in self.phraseList:
            letter.render(screen)
