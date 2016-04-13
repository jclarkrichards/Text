"""Left justify text"""

class LeftJust(object):
    def __init__(self):
        pass
    
    '''
    words = phrase.split()
        line = 0
        col = 0
        numChars = 0
        index = 0
        offsetX = 0 #0 for first word, 1 otherwise
        offsetY = 0 #1 for first word, 0 otherwise
        charlist = []
        
        for iword, word in enumerate(words):
            if numChars+len(word)+offsetX <= self.charPerLine:
                numChars += len(word)+offsetX
            else:
                numChars = len(word)
                line += 1
                offsetY = 1
                col = 0
                if line >= self.lines:
                    line = 0
                    self.phrase.phraseArray.append(charlist)
                    charlist = []

            for i in range(index+offsetY, len(word)+index+offsetX):
                self.phrase.phraseList[i].setPosition(self.position, col, line)
                charlist.append(self.phrase.phraseList[i])
                col += 1
            
            offsetX = 1
            offsetY = 0
            index = i+1
        self.phrase.phraseArray.append(charlist)
        self.phrase.phraseList = self.phrase.phraseArray[self.iphrase]
    '''
