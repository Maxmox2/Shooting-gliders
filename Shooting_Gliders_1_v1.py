#!/usr/bin/python3

from pygame import mixer
import pygame

mixer.init()
pygame.init()
windowSize = [800,500]
screen = pygame.display.set_mode(windowSize)
noire = pygame.color.Color('#000000')
pygame.display.set_caption('Gliders')

picture = pygame.image.load('Shooting_Gliders_Goa_4.png')
picture2 = pygame.image.load('Shooting_Gliders_Hum_2.png')
shoot_droit = pygame.image.load('Shooting_Gliders_Tirs_Goa_4.png')
shoot_gauch = pygame.image.load('Shooting_Gliders_Tirs_Goa_2.png')
pygame.display.set_icon(picture)

xp1 = 20
yp1 = 250
xp2 = 720
yp2 = 250
finished = False
pou1 = 20
pou2 =  720

# musique

boume = pygame.mixer.Sound("bonme.mp3")
mixer.music.load('dam dim.wav')
mixer.music.set_volume(1)
mixer.music.play()

# main game loop

while not finished:
    screen.fill(noire)
    # bordure
    if yp1 > 437:
        yp1 = yp1 + -1
    if xp1 > 730:
        xp1 = xp1 + -1
    if yp1 < -3:
        yp1 = yp1 + 1
    if xp1 < 10:
        xp1 = xp1 + 1
    
    if yp2 > 437:
        yp2 = yp2 + -1
    if xp2 > 720:
        xp2 = xp2 + -1
    if yp2 < -3:
        yp2 = yp2 + 1
    if xp2 < 10:
        xp2 = xp2 + 1
    # player 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        yp1+=1
    if keys[pygame.K_w]:
        yp1-=1
    screen.blit(picture, (xp1,yp1))
    # shooting p1
    if yp1 is yp2 and keys [pygame.K_v]:
        picture2 = pygame.image.load('banana.png')
        boume.play()
    
    # player 2
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        yp2+=1
    if keys[pygame.K_UP]:
        yp2-=1
    screen.blit(picture2, (xp2,yp2))
    # shooting p2
    if yp2 is yp1 and keys [pygame.K_m]:
        picture = pygame.image.load('banana.png')
        boume.play()
    
    # explotion
    if pou1 == yp2 and pou1 == xp2:
        picture2 = pygame.image.load('banana.png')
    
    if pou2 == yp1 and pou2 == xp1:
        picture = pygame.image.load('banana.png')
    
    # disparetre les véseau cassé
    if keys [pygame.K_r]:
        picture = pygame.image.load('Shooting_Gliders_Goa_4.png')
    
    if keys [pygame.K_n]:
        picture2 = pygame.image.load('Shooting_Gliders_Hum_2.png')
    
    # fermer la fenêtre
    
    if keys [pygame.K_i]:
        exit(0)
    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
