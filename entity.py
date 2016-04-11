import pygame
from vectors import Vector2D

class Character(object):
    def __init__(self, surfaceObj):
        self.image = surfaceObj
        self.position = Vector2D()
        self.size = self.image.get_size()
        self.alive = True
        
    def update(self, dt):
        pass
    
    def setPosition(self, position):
        '''position can be a tuple or a list in (x,y) format'''
        self.position = Vector2D(tuple(position))
        
    def setPositionManual(self, position, offsetx, offsety):
        self.position = position + Vector2D(size[0]*offsetx, size[1]*offsety)

    def setSize(self):
        self.size = self.image.get_size()
        
    def render(self, screen):
        if self.alive:
            screen.blit(self.image, self.position.toTuple())
    
