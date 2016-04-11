from vectors import Vector2D
from phrase import PhraseHandler

class TextBox(object):
    def __init__(self, lines, charsPerLine):
        self.charPerLine = charsPerLine
        self.lines = lines
        self.position = Vector2D()
        self.width = 0
        self.height = 0
        self.phrase = None
        self.charsize = (0, 0)
        
    def update(self, dt):
        pass
    
    def setDimensions(self):
        '''dimensions based on characters width and height'''
        self.width = self.charPerLine*self.charsize[0]
        self.height = self.lines*self.charsize[1]
    
    def setPosition(self, position):
        dp = Vector2D(position) - self.position
        self.position = Vector2D(position)
        if self.phrase:
            for letter in self.phrase.phraseList:
                letter.position += dp
        
    def setPhrase(self, phrase, table):
        '''The input phrase is a string. table is the dictionary'''
        self.phrase = PhraseHandler(phrase)
        self.phrase.mapPhrase(table) #self.phrase.phraseList
        self.charsize = self.phrase[0].size()
        self.setDimensions()
        self.setCharPositions()
        
    def scaleCharacters(self, scale):
        '''Set dimensions of characters.  Changes dimensions of box'''
        self.phrase.setScale(scale)
        self.charsize = self.phrase[0].size()
        self.setDimensions()
        
    def setCharPositions(self):
        pass
        
    def render(self, screen):
        pass
        
