import pygame
from base import Text
from vectors import Vector2D
from entity import Character

class PhraseHandler(object):
    def __init__(self, phrase):
        self.phrase = phrase
        self.phraseList = []
        
    def updatePhrase(self, phrase):
        '''Set a new phrase to use'''
        pass
    
    def mapPhrase(self, lookup):
        '''Get all of the character images to construct the phrase'''
        print self.phrase
        for letter in self.phrase:
            try:
                self.phraseList.append(Character(lookup[letter]))
            except KeyError:
                #self.phraseList.append(Character(None))
            
    def setPosition(self, position):
        '''Set the position relative to the first letter'''
        for i, letter in enumerate(self.phraseList):
            letter.setPosition((position[0]+letter.size[0]*i, position[1]))
            
    def setScale(self, scale):
        '''Make the letters bigger or smaller'''
        for letter in self.phraseList:
            print letter.size[0]*scale, letter.size[1]*scale
            newSize = (letter.size[0]*scale, letter.size[1]*scale)
            letter.image = pygame.transform.scale(letter.image, newSize)
            letter.setSize()
    
    def render(self, screen):
        '''Print the phrase onto the screen'''
        for letter in self.phraseList:
            letter.render(screen)
