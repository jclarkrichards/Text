
import pygame
 
class SpriteHandler(object):
    def __init__(self, filename):
        self.filename = filename
        self.sheet = None
        self.frame = None
        self.frameset = []
        
    def load(self):
        '''Load a sprite sheet for use'''
        self.sheet = pygame.image.load(self.filename).convert_alpha()
        
    def grabSingle(self, scale, clip):
        '''Grab a single frame from the sheet.
        clip=(x,y,width,height) of image to clip'''
        #self.sheet.set_clip(pygame.Rect(clip))
        #return self.sheet.subsurface(self.sheet.get_clip()) #can I scale this?
        frame = pygame.Surface(clip[2:])
        frame.blit(self.sheet, (0,0), clip)
        return pygame.transform.scale(frame, (clip[2]*scale, clip[3]*scale))
    
    def grabSet(filename, dim, startpos=(0,0), num=(1,1)):
        '''Grab a set of images from FILENAME
        DIM is the dimensions of images to grab in a tuple
        STARTPOS is the (x,y) coordinate from top left of sheet
        NUM is how many rows and columns the images to use span'''
        #sheet = pygame.image.load(filename).convert_alpha()
        sheetx, sheety = startpos
        w, h = dim
        sheetx *= w
        sheety *= h
        row, column = num
        frameset = []
        for i in range(row):
            for j in range(column):
                sheet.set_clip(pygame.Rect(sheetx+w*j, sheety+h*i, w, h))
                frameset.append(sheet.subsurface(sheet.get_clip()))
 
        return frameset
