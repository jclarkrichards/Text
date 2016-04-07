"""Any class that uses text needs to inherit from this class"""
import os
from image_set import grabset
from vectors import Vector2D
from entity import Entity
import numpy as np

class TextBase(object):
    def __init__(self, position, area, phrase=''):
        self.basedir = '' #os.environ['HOME']+'/Documents/MyGames/Text'
        self.sheet = '' #'deluxe8bit.png'
        self.linespace = 2
        self.wordspace = 8
        self.upperframes = []
        self.lowerframes = []
        self.numberframes = []
        self.punctuationframes = []
        self.textdict = {}
        self.position = Vector2D(position)
        self.area = Vector2D(area)
        self.charsize = (8,8)
        self.charlist = []
        self.phraselist = []
        self.loadSheet(self.charsize)
        self.makeDict()
        self.phrase = phrase
        self.spaces = []
        self.textoffset = 0
        self.name = 'text'

    def findABetterName(self, filename):
        with open(filename) as f:
            data = np.array(f.read().split(), dtype=str)
            
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

    def loadSheet(self, charsize):
        '''Load a text sprite sheet and specify the width and height
        of characters on the sheet using CHARSIZE.
        UPPERFRAMES and LOWERFRAMES are always from A to Z (26 characters).
        NUMBERFRAMES always go from 0 to 9.
        PUNCTUATIONFRAMES needs more attention'''
        self.charsize = charsize
        filename = self.basedir+'/'+self.sheet
        self.upperframes = grabset(filename, charsize, num=(1,26))
        self.lowerframes = grabset(filename, charsize, startpos=(0,1),
                                   num=(1,26))
        self.numberframes = grabset(filename, charsize, startpos=(0,2),
                                    num=(1,10))
        self.punctuationframes = grabset(filename, charsize, startpos=(0,3),
                                         num=(1,21))
    
    def replaceSheet(self, newsheet, charsize):
        '''Replace the default text sheet'''
        self.sheet = newsheet
        self.loadSheet(charsize)
        self.makeDict()

    def makeDict(self):
        '''Make a single dictionary of all the charcters frames'''
        self.textdict = {}
        alphaupper = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                      'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        alphalower = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                      'n','o','p','q','r','s','t','u','v','w','x','y','z']
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        punct = ['.',',','!','?','"',':',';','-','+','\'','%','@','#','$',
                 '&','*','(',')','/','\\','=']
        for i in range(len(alphaupper)):
            self.textdict[alphaupper[i]] = self.upperframes[i]
        for i in range(len(alphalower)):
            self.textdict[alphalower[i]] = self.lowerframes[i]
        for i in range(len(numbers)):
            self.textdict[numbers[i]] = self.numberframes[i]
        for i in range(len(punct)):
            self.textdict[punct[i]] = self.punctuationframes[i]

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



