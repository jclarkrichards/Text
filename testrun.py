import pygame
from pygame.locals import *
from base import Text
from phrase import PhraseHandler

pygame.init()
screen = pygame.display.set_mode((500,500), 0, 32)
background = pygame.surface.Surface((500,500)).convert()
background.fill((0,0,0))

txt = Text()
phrase = PhraseHandler()
phrase.setPhrase("Hello World!")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
            
    phrase.print(screen)
    
    pygame.display.update()
