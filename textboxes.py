from vectors import Vector2D
from phrase import PhraseHandler

class TextBox(object):
    def __init__(self, lines, charsPerLine):
        self.charPerLine = charsPerLine
        self.lines = lines
        self.position = Vector2D()
        self.phrase = ''
        
    def update(self, dt):
        pass
    
    def setPosition(self, position):
        self.position = Vector2D(position)
        
    def setPhrase(self, phrase, table):
        '''The phrase is a string. table maps the characters'''
        self.phrase = PhraseHandler(phrase)
        self.phrase.mapPhrase(table)
        
    def scaleCharacters(self, scale):
        self.phrase.setScale(scale)
        
    def render(self, screen):
        pass
        
