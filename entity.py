import pygame
from vectors import Vector2D

class Character(object):
    def __init__(self, surfaceObj):
        self.image = surfaceObj
        self.position = Vector2D() 
        self.size = self.image.get_size()
        
    def update(self, dt):
        pass
    
    def render(self, screen):
        screen.blit(self.image, self.position.toTuple())
    
