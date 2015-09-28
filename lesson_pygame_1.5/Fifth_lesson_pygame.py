# -*- coding: utf-8 -*-
'''https://www.youtube.com/channel/UCBWVx7ngVu5kWQ9CcGT2tEQ'''
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
        
def Intersect(x1, x2, y1, y2, db1, db2):
    if (x1 > x2-db1) and (x1 < x2+db2) and (y1 > y2-db1) and (y1 < y2+db2):
        return 1
    else:
        return 0

''' описание героя ''' 
hero = Sprite(350, 350, 'images/h.png')
''' описание цели '''
zet = Sprite(10, 10, 'images/z.png')
zet.right = False
zet.step = 1
''' описываем стрелу '''
strela = Sprite(-10, 350, 'images/s.png')
strela.push = False

done = True
pygame.key.set_repeat(1,1)
pygame.mouse.set_visible(False)
while done:
    ''' обработчик событий '''
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
            ''' событие - нажатие клавиш '''
        if e.type == pygame.KEYDOWN:
            ''' перемещение героя '''
            if e.key == pygame.K_LEFT:
                if hero.x > 10:
                    hero.x -= 1
            if e.key == pygame.K_RIGHT:
                if hero.x < 350:
                    hero.x += 1
            if e.key == pygame.K_UP:
                if hero.y > 200:
                    hero.y -= 1
            if e.key == pygame.K_DOWN:
                if hero.y < 350:
                    hero.y += 1
            ''' запуск стрелы '''
            if e.key == pygame.K_SPACE:
                if strela.push == False:
                    strela.x = hero.x+15
                    strela.y = hero.y
                    strela.push = True
        ''' событие - движение мыши '''
        if e.type == pygame.MOUSEMOTION:
            m = pygame.mouse.get_pos()
            if m[0] > 10 and m[0] < 350:
                hero.x = m[0]
            if m[1] > 200 and m[1] < 350:
                hero.y = m[1]
        ''' событие - нажатие кнопок мыши '''
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                if strela.push == False:
                    strela.x = hero.x+15
                    strela.y = hero.y
                    strela.push = True
            
            
    ''' заливка экрана '''
    screen.fill((50, 50, 50))
    
    ''' передвижение цели '''        
    if zet.right == True:
        zet.x -= zet.step
        if zet.x < 0:
            zet.right = False
    else:
        zet.x += zet.step
        if zet.x > 350:
            zet.right = True
            
    ''' перемещение стрелы '''
    if strela.y < 0:
        strela.push = False
    
    if strela.push == False:
        strela.y = 350
        strela.x = -10
    else:
        strela.y -= 1
        
    ''' столкновение стрелы и цели '''
    if Intersect(strela.x, zet.x, strela.y, zet.y, 5, 40) == True:
        strela.push = False
        zet.step += 0.2
    
    ''' отрисовка объектов '''
    strela.render()
    zet.render()
    hero.render()
    window.blit(screen, (0,0))
    pygame.display.flip()
    pygame.time.delay(5)