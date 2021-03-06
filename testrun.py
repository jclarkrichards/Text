import pygame
from pygame.locals import *
from base import Text
from phrase import PhraseHandler
from textboxes import TextBox

pygame.init()
screen = pygame.display.set_mode((500,500), 0, 32)
background = pygame.surface.Surface((500,500)).convert()
background.fill((0,0,0))
clock = pygame.time.Clock()
txt = Text('deluxefont8px.png', 'text_map.txt', (8,8))

box = TextBox(3, 25)
box.setPosition((50,100))
box.setPhrase("Jonathan Richards is my name. I am the most awesomest person in the entire world! I mean seriously now. Is there anybody better than me?", txt.textDict, 2)
#box.scaleCharacters(2)
box.readoutCharacters(15)

while True:
    dt = clock.tick(30)/1000.0
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    box.update(dt)
    #phrase.update(dt)
    screen.blit(background, (0,0))
    #phrase.render(screen)
    box.render(screen)
    
    pygame.display.update()
