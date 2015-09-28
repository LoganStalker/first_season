# -*- coding: utf-8 -*-
#
import pygame

window = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Hello, pygame!')
screen = pygame.Surface((400, 400))

img = pygame.image.load('images/h.png')
img.set_colorkey((0,0,0))

done = True
angle = 0
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
    
    screen.fill((50,50,50))
    window.blit(screen, (0,0))
    pygame.display.flip()
    pygame.time.delay(5)