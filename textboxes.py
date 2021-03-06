from vectors import Vector2D
from phrase import PhraseHandler

class TextBox(object):
    def __init__(self, lines, charPerLine):
        self.charPerLine = charPerLine
        self.lines = lines
        self.position = Vector2D()
        self.width = 0
        self.height = 0
        self.phrase = None
        #self.phraseStr = ''
        self.charsize = (0, 0)
        
    def update(self, dt):
        self.phrase.update(dt)
    
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
        
    def setPhrase(self, phrase, table, scale):
        '''The input phrase is a string. table is the dictionary'''
        #self.phraseStr = phrase
        self.phrase = PhraseHandler(phrase)
        self.phrase.mapPhrase(table) #self.phrase.phraseList
        self.charsize = self.phrase.phraseList[0].size
        self.setDimensions()
        self.scaleCharacters(scale)
        self.setCharPositions(phrase)
        
    def scaleCharacters(self, scale):
        '''Set dimensions of characters.  Changes dimensions of box'''
        self.phrase.setScale(scale)
        self.charsize = self.phrase.phraseList[0].size
        self.setDimensions()
        
    def setCharPositions(self, phrase):
        words = phrase.split()
        line = 0
        col = 0
        numChars = 0
        index = 0
        offsetX = 0 #0 for first word, 1 otherwise
        offsetY = 0 #1 for first word, 0 otherwise
        
        for iword, word in enumerate(words):
            if numChars+len(word)+offsetX <= self.charPerLine:
                numChars += len(word)+offsetX
            else:
                numChars = len(word)
                line += 1
                offsetY = 1
                col = 0

            for i in range(index+offsetY, len(word)+index+offsetX):
                self.phrase.phraseList[i].setPosition(self.position, col, line)
                col += 1
                
            offsetX = 1
            offsetY = 0
            index = i+1

    def readoutCharacters(self, speed):
        self.phrase.readoutCharacters(speed)
        
    def render(self, screen):
        self.phrase.render(screen)
        
