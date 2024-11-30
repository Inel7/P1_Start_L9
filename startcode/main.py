import pygame, sys
from pygame.locals import QUIT

pygame.init()
venster = pygame.display.set_mode((1000, 500))
venster.fill((255,255,255))
color = (0,0,0)
radius = 1
w = 0
x = 0
c = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed() == (True,True,True):
            venster.fill((255,255,255))#reset
        if pygame.mouse.get_pressed() == (True,False,False):
            pygame.draw.circle(venster,color,pygame.mouse.get_pos(),radius)#penseel
        if pygame.mouse.get_pressed() == (False,False,True):
            pygame.draw.circle(venster,(255,255,255),pygame.mouse.get_pos(),radius)#gom
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255,0,0)#rood
            if event.key == pygame.K_b:
                color = (0,0,255)#blauw
            if event.key == pygame.K_g:
                color = (0,255,0)#groen
            if event.key == pygame.K_z:
                color = (0,0,0)#zwart
            if event.key == pygame.K_UP:
                radius = radius + 1
            if event.key == pygame.K_DOWN:
                radius = radius - 1
            if event.key == pygame.K_s:
                pygame.image.save(venster,"tekening"+".jpg")
            if event.key == pygame.K_w:
                w = w + 10
            if event.key == pygame.K_x:
                x = x + 10
            if event.key == pygame.K_c:
                 c = c + 10
            if event.key == pygame.K_o:
                color = (w,x,c)
    pygame.display.update()
