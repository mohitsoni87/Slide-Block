import pygame as pg
from pygame.locals import *
import time
pg.init()
gamedisp = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
pg.display.set_caption('Slide Block')
dot = pg.image.load('object.jpg')
rec = pg.image.load('rec.png')
gamedisp.fill((255, 255, 255))
c = 1
s = 'UR'
x = 400
y = 300
white = (255, 255, 255)
black = (0, 0, 0)
st = 'r'
rx, ry = 304.5, 586
gamedisp.blit(rec, (rx, ry))

def text_objects(text, style):
      surface = style.render(text, True, black)
      return surface, surface.get_rect()
    
def Text_Formatting(text, font_size):
      style = pg.font.Font('freesansbold.ttf', font_size)
      Text, TextRect = text_objects(text, style)
      return Text, TextRect
    
def crash():
    gamedisp.blit(rec, (rx, ry))
    gamedisp.blit(dot, (x, y))
    time.sleep(1)
    main(400, 300, 304.5, 586, 1, 'UR')
    
def Disk(rx, ry):
    gamedisp.fill(white)
    gamedisp.blit(rec, (rx, ry))


def Ball(x, y, x_start, x_end):
    if(y >= 546):
        if(x > x_end):
            crash()
        elif(x + 40 < x_start):
            crash()
        else:
            gamedisp.blit(dot, (x, y))
    else:
        gamedisp.blit(dot, (x, y))

def main(x, y, rx, ry, c, s):
    while(c):
        for event in pg.event.get():
            if(event.type == pg.QUIT):
                c = 0
                break
            if(event.type == KEYDOWN):
                if(event.key == K_RIGHT):
                    rx += 50
                    if(rx + 191 > 800):
                        rx = 800 - 191
                if(event.key == K_LEFT):
                    rx -= 50
                    if(rx < 0):
                        rx = 0
        if(s == 'UR'):
            x += 4
            y -= 4
            if(x > 760):
                s = 'UL'
            elif(y < 0):
                s = 'DR'
        if(s == 'UL'):
            x -= 4
            y -= 4
            if(x < 0):
                s = 'UR'
            elif(y < 0):
                s = 'DL'
        if(s == 'DR'):
            x += 4
            y += 4
            if(x > 760):
                s = 'DL'
            elif(y > 546):
                s = 'UR'
        if(s == 'DL'):
            x -= 4
            y += 4
            if(x < 0):
                s = 'DR'
            elif(y > 546):
                s = 'UL'
        Disk(rx, ry)
        x_start, x_end = rx, rx + 191.5
        Ball(x, y, x_start, x_end)
        pg.display.update()
        clock.tick(60)

main(400, 300, 304.5, 586, 1, 'UR')
pg.quit()
