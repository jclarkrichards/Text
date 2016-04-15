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

box = TextBox(2, 25)
box.setPosition((80,300))
box.setPhrase("Joseph!!! WAKE UP!!! You need to go down to the farm and help your poor poor father who is just slaving away at sowing his seeds! SOW YOUR SEEDS JOSEPH!!!", txt.textDict, 2)
box.readoutCharacters(15)

while True:
    dt = clock.tick(30)/1000.0
    key_held = pygame.key.get_pressed()
    if key_held[K_SPACE]:
        box.increaseSpeed()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                box.nextPhrase()
        elif event.type == KEYUP:
            if event.key == K_SPACE:
                box.resetSpeed()
        
        
    box.update(dt)
    screen.blit(background, (0,0))
    box.render(screen)
    pygame.display.update()
