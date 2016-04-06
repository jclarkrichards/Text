import pygame

def grabset(filename, dim, startpos=(0,0), num=(1,1)):
    '''Grab a set of tiles from the images in FILENAME
    DIM is the dimensions of tiles to grab in a tuple
    STARTPOS is the (x,y) coordinate from top left of sheet
    NUM is how many rows and columns the images to use span'''
    sheet = pygame.image.load(filename).convert_alpha()
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
