from vectors import Vector2D
from phrase import PhraseHandler

class TextBox(object):
    def __init__(self, lines, charsPerLine):
        self.charPerLine = charsPerLine
        self.lines = lines
        self.position = Vector2D()
        self.width = 0
        self.height = 0
        self.phrase = ''
        self.charsize = (0, 0)
        
    def update(self, dt):
        pass
    
    def setDimensions(self):
        '''dimensions based on characters width and height'''
        pass
    
    def setPosition(self, position):
        self.position = Vector2D(position)
        
    def setPhrase(self, phrase, table):
        '''The phrase is a string. table maps the characters'''
        self.phrase = PhraseHandler(phrase)
        self.phrase.mapPhrase(table)
        self.charsize = self.phrase[0].get_size()
        
    def scaleCharacters(self, scale):
        '''Set dimensions of characters.  Changes dimensions of box'''
        self.phrase.setScale(scale)
        self.setDimensions()
        
    def render(self, screen):
        pass
        
