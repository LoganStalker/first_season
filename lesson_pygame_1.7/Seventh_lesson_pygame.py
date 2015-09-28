# -*- coding: utf-8 -*-
'''https://www.youtube.com/channel/UCBWVx7ngVu5kWQ9CcGT2tEQ'''
import pygame, sys

''' окно '''
window = pygame.display.set_mode((400, 430))
pygame.display.set_caption('Hello, pygame!')
''' холст '''
screen = pygame.Surface((400, 400))
''' строка состояния '''
info_string = pygame.Surface((400, 30))
''' области движения '''
hero_area = pygame.Surface((380, 190))
zet_area = pygame.Surface((380, 40))

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

class Menu:
    def __init__(self, punkts = [120, 140, u'Game', (250, 250, 30), (250, 30, 250), 0]):
        self.punkts = punkts
    def render(self, screen, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                screen.blit(font.render(i[2], 1, i[4]), (i[0], i[1]-30))
            else:
                screen.blit(font.render(i[2], 1, i[3]), (i[0], i[1]-30))
    def menu(self):
        done = True
        pygame.mouse.set_visible(True)
        pygame.key.set_repeat(0,0)
        font_menu = pygame.font.Font('fonts/Purisa.otf', 50)
        punkt = 0
        while done:
            info_string.fill((0, 100, 200))
            screen.fill((0, 100, 200))
            
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0]>i[0] and mp[0]<i[0]+155 and mp[1]>i[1] and mp[1]<i[1]+50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)
            
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        if punkt == 0:
                            done = False
                        if punkt == 1:
                            sys.exit()
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts)-1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    if punkt == 1:
                        sys.exit()
            
            window.blit(info_string, (0, 0))
            window.blit(screen, (0, 30))
            pygame.display.update()

''' шрифты '''
pygame.font.init()
speed_font = pygame.font.Font(None, 32)
inf_font = pygame.font.Font(None, 32)
label_font = pygame.font.Font('fonts/OpenDyslexicAlta-Bold.otf', 30)

''' описание героя ''' 
hero = Sprite(350, 350, 'images/h.png')
''' описание цели '''
zet = Sprite(10, 10, 'images/z.png')
zet.right = False

zet.step = 1
''' описываем стрелу '''
strela = Sprite(-10, 350, 'images/s.png')
strela.push = False

''' создаем меню '''
punkts = [(120, 140, u'Game', (250, 250, 30), (250, 30, 250), 0),
          (130, 210, u'Quit', (250, 250, 30), (250, 30, 250), 1)]
game = Menu(punkts)
game.menu()

''' подготовка к запуску игры '''
done = True
pygame.key.set_repeat(1,1)
pygame.mouse.set_visible(False)
enumerator = 0
arrow_color = 255

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
            ''' пауза '''
            if e.key == pygame.K_ESCAPE:
                game.menu()
                pygame.key.set_repeat(1,1)
                pygame.mouse.set_visible(False)
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
            
            
    ''' заливка '''
    screen.fill((50, 50, 50))
    info_string.fill((45, 80, 40))
    hero_area.fill((70, 70, 70))
    zet_area.fill((70, 70, 70))
    ''' изменение цвета названия '''
    arrow_color += 0.1
    if arrow_color > 254:
        arrow_color = 100
    
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
        enumerator -= 1
    
    if strela.push == False:
        strela.y = 350
        strela.x = 400
    else:
        strela.y -= 1
        
    ''' столкновение стрелы и цели '''
    if Intersect(strela.x, zet.x, strela.y, zet.y, 5, 40) == True:
        strela.push = False
        zet.step += 0.2
        enumerator += 1
    
    ''' отрисовка объектов '''
    screen.blit(hero_area, (10, 200))
    screen.blit(zet_area, (10, 10))
    strela.render()
    zet.render()
    hero.render()
    ''' отрисовка шрифтов '''
    info_string.blit(inf_font.render(u'Счет: '+str(enumerator), 1, (0, 250, 200)), (10, 0))
    info_string.blit(label_font.render(u'ARROW', 1, (0, arrow_color, 0)), (125, -10))
    info_string.blit(speed_font.render(u'Spd: '+str(zet.step), 1, (210, 120, 200)), (310, 5))
    ''' отображение холста на экран '''
    window.blit(info_string, (0, 0))
    window.blit(screen, (0, 30))
    pygame.display.flip()
    pygame.time.delay(5)