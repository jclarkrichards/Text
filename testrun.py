import pygame
from pygame.locals import *
from base import Text
from phrase import PhraseHandler

pygame.init()
screen = pygame.display.set_mode((500,500), 0, 32)
background = pygame.surface.Surface((500,500)).convert()
background.fill((0,0,0))
clock = pygame.time.Clock()
txt = Text('deluxefont8px.png', 'text_map.txt', (8,8))
phrase = PhraseHandler("Jonathan Richards")
phrase.mapPhrase(txt.textDict)
#phrase.setScale(3)
phrase.setPosition((10,200))
phrase.readoutCharacters(15)

while True:
    dt = clock.tick(30)/1000.0
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    phrase.update(dt)
    screen.blit(background, (0,0))
    phrase.render(screen)
    
    pygame.display.update()
