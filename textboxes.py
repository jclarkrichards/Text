from vectors import Vector2D

class TextBox(object):
    def __init__(self, lines, charsPerLine):
        self.charPerLine = charsPerLine
        self.lines = lines
        self.position = Vector2D()
        self.phrase = ''
        
    def setPosition(self, position):
        self.position = Vector2D(position)
        
    def setPhrase(self, phrase, table):
        '''The phrase is a string. table maps the characters'''
        self.phrase = phrase
        
