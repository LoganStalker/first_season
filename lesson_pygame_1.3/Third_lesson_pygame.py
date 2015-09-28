# -*- coding: utf-8 -*-
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

hero = Sprite(350, 350, 'images/h.png')
hero.go_right = True
hero.go_down = True
zet = Sprite(10, 10, 'images/z.png')
zet.go_right = True
zet.step = 1
zet.size = 40
strela = Sprite(-10, 350, 'images/s.png')
strela.push = False

def Intersect(x1, x2, y1, y2,db1,db2):
    if (x1 > x2-db1) and (x1 < x2+db2) and (y1 > y2-db1) and (y1 < y2+db2/2):
        return 1
    else:
        return 0

def resize(obj, size):
    return pygame.transform.scale(obj, (size, size))

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                strela.x = hero.x+15
                strela.push = True
    
    screen.fill((50,50,50))
    
    if hero.go_right == True:
        hero.x += 1
        if hero.x > 350:
            hero.go_right = False
    else:
        hero.x -= 1
        if hero.x < 10:
            hero.go_right = True
    
    if zet.go_right == True:
        zet.x += zet.step
        if zet.x > 350:
            zet.go_right = False
    else:
        zet.x -= zet.step
        if zet.x < 10:
            zet.go_right = True
    
    if Intersect(strela.x, zet.x, strela.y, zet.y, 5, zet.size) == True:
        zet.size -= 5
        zet.step += 0.2
        zet.bitmap = resize(zet.bitmap, zet.size)
        strela.push = False
    
    if strela.y < 0:
        strela.push = False
    
    if strela.push == False:
        strela.y = 350
        strela.x = -10
    else: 
        strela.y -= 1
    
    zet.render()
    strela.render()
    hero.render()
    window.blit(screen, (0,0))
    pygame.display.flip()
    pygame.time.delay(5)