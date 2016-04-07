"""Any class that uses text needs to inherit from this class"""
import os
from image_set import SpriteHandler
from vectors import Vector2D
from entity import Entity
import numpy as np

class TextBase(object):
    def __init__(self, sheet, txtfile, charsize):
        self.sheet = sheet #'deluxe8bit.png'
        self.txtfile = txtfile
        self.charsize = charsize
        self.imageChars = []
        self.textChars = []
        self.loadSheet()
        #self.linespace = 2
        #self.wordspace = 8
        self.textdict = {}
        #self.position = Vector2D(position)
        #self.area = Vector2D(area)
        #self.charlist = []
        #self.phraselist = []
        #self.loadSheet(self.charsize)
        #self.makeDict()
        #self.phrase = phrase
        #self.spaces = []
        #self.textoffset = 0
        #self.name = 'text'
        
    """
    def setTextMap(self):
        '''Open the txt file that maps the text to the image sheet'''
        with open(self.txtfile) as f:
            self.textChars = np.array(f.read().split(), dtype=str)
        self.textChars = list(self.textChars)
    """    
    def getRowNums(self):
        rowNums = []
        self.textChars = []
        with open(self.txtfile) as f:
            thisline = list(np.array(f.readline().split(), dtype=str))
            self.textChars += thisline
            rowNums.append(len(thisline))
        return rowNums
        
    def loadSheet(self):
        '''Load the character sheet'''
        rowNums = self.getRowNums()
        sheet = SpriteHandler(self.sheet)
        w, h = self.charsize
        self.imageChars = sheet.grabAll(w, h, rowNums)
        self.mapCharacters()
        
    def mapCharacters(self):
        '''Map the image characters to the text characters'''
        self.textDict = {}
        if len(self.textChars) != len(self.imageChars):
            return "textChars and imageChars do not match!"
        for i, char in enumerate(self.textChars):
            self.textDict[char] = Entity(self.imageChar[i])
            
            
            
    def useUpperCase(self):
        '''Use only uppercase letters'''
        self.phrase = self.phrase.upper()

    def setPhrase(self, phrase):
        '''Set the phrase to print to screen'''
        self.phrase = phrase

    def updatePhrase(self, newphrase):
        '''Update the phrase with a new phrase'''
        self.phrase = str(newphrase)
        self.parsePhrase()
        self.interpret()
    
    def replaceSheet(self, newsheet, charsize):
        '''Replace the default text sheet'''
        self.sheet = newsheet
        self.loadSheet(charsize)
        self.makeDict()

    def interpret(self):
        '''Interpret a string into their corresponding character images.
        Determine the x,y position of each character.'''
        self.charlist = []
        maxrows = int(self.area.y / (self.charsize[1]+self.linespace))
        if maxrows < 1:
            maxrows = 1
        w, h = self.charsize
        row = 0
        while row < maxrows:
            try:
                thisphrase = self.phraselist[0]
            except IndexError:
                row = maxrows
            else:
                for j in range(len(thisphrase)):
                    pos = (j*w+self.position.x+self.textoffset,
                           row*(self.linespace+h)+self.position.y)
                    try:
                        image = self.textdict[thisphrase[j]]
                    except:
                        self.spaces.append((pos[0]-self.position.x) / w)
                    else:
                        self.charlist.append(AbstractEntity((w,h),image=image,
                                                            startpos=pos))
                self.phraselist.remove(thisphrase)
            row += 1

    def parsePhrase(self):
        '''Split the phrase into multiple lines if it exceeds MAXWIDTH.'''
        dx,dy = self.charsize
        width, height = self.area.toTuple()
        wordlist = self.phrase.split(' ')
        while len(wordlist) > 0:
            n = 0
            templist = []
            nextline = False
            while not nextline and len(wordlist) > 0:
                word = wordlist[0]
                n += len(word)*dx
                if n > width:
                    nextline = True
                else:
                    templist.append(word)
                    wordlist.remove(word)
                    n += self.wordspace
            self.phraselist.append(" ".join(templist))

    def fromTextFile(self, filename, thisline):
        '''Get a phrase from a text file.  Assume that each phrase
        is on a different line in the file'''
        indx = 0
        with open(filename, "r") as f:
            for line in f:
                if indx == thisline:
                    self.phrase = line
                    self.phrase.strip('\n')
                    break
                indx += 1



