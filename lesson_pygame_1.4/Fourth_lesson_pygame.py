# -*- coding: utf-8 -*-
#https://www.youtube.com/channel/UCBWVx7ngVu5kWQ9CcGT2tEQ
import pygame

window = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Hello, pygame!')
screen = pygame.Surface((400, 400))

class Sprite:
    def __init__(self,xpos,ypos,filename):
        self.x=xpos
        self.y=ypos
        self.bitmap=pygame.image.load(filename)
        self.bitmap.set_colorkey((0,0,0))
    def render(self):
        screen.blit(self.bitmap,(self.x,self.y))
        
def Intersect(x1, x2, y1, y2):
    if (x1 > x2-40) and (x1 < x2+40) and (y1 > y2-40) and (y1 < y2+40):
        return 1
    else:
        return 0

hero = Sprite(350, 200, 'images/h.png')
hero.up = True
zet = Sprite(10, 200, 'images/z.png')
zet.up = False

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
    
    screen.fill((50, 50, 50))
    
    if hero.up == True:
        hero.x -= 1
        if hero.x == 0:
            hero.up = False
    else:
        hero.x += 1
        if hero.x == 350:
            hero.up = True
            
    if zet.up == True:
        zet.x -= 1
        if zet.x == 0:
            zet.up = False
    else:
        zet.x += 1
        if zet.x == 350:
            zet.up = True
            
    if Intersect(zet.x, hero.x, zet.y, hero.y) == True:
            hero.up = False
            zet.up = True
    
    zet.render()
    hero.render()
    window.blit(screen, (0,0))
    pygame.display.flip()
    pygame.time.delay(5)