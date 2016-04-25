import pygame
from pygame.locals import *
from textboxes import TextBox

pygame.init()
screen = pygame.display.set_mode((500,500), 0, 32)
background = pygame.surface.Surface((500,500)).convert()
background.fill((0,0,0))
clock = pygame.time.Clock()

box = TextBox(2, 25)
box.setFont('deluxefont8px.png', 'text_map.txt', (8,8))
box.setPosition((80,300))
phrase = None

while True:
    print box.active
    dt = clock.tick(30)/1000.0
    key_held = pygame.key.get_pressed()
    if key_held[K_SPACE]:
        box.increaseSpeed()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                box.readoutCharacters(phrase, 15, 2)
            if event.key == K_a:
                phrase = "This is another phrase that I want to print out to the screen so that I can test to see if my awesome program works as I intend for it to work."
            if event.key == K_s:
                phrase = "Joseph!!! WAKE UP!!! You need to go down to the farm and help your poor poor father who is just slaving away at sowing his seeds! SOW YOUR SEEDS JOSEPH you fucking douche bag of a person!!!"
                
        elif event.type == KEYUP:
            if event.key == K_SPACE:
                box.resetSpeed()
        
    if box.phrase:
        box.update(dt)
    screen.blit(background, (0,0))
    if box.phrase:
        box.render(screen)
    pygame.display.update()
