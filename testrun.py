import pygame
from pygame.locals import *
from base import Text
from phrase import PhraseHandler

pygame.init()
screen = pygame.display.set_mode((500,500), 0, 32)
background = pygame.surface.Surface((500,500)).convert()
background.fill((0,0,0))

txt = Text(spritesheet, 'text_map.txt', (16,16))
phrase = PhraseHandler("Hello World!")
phrase.mapPhrase(txt.textDict)
phrase.setPosition((100,100))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
            
    screen.blit(background, (0,0))
    phrase.print(screen)
    
    pygame.display.update()
