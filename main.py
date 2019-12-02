#-------------------------------------------------------------------------------
# Name:        Jeu
# Purpose:
#
# Author:      Clément Laymajoux
#
# Created:     23/10/2019
# Copyright:   (c) Clément Laymajoux 2019
#              All Rights Reserved ^^
#-------------------------------------------------------------------------------
import pygame,sys
from pygame.locals import *

largeur = 500
hauteur = 300
pos_x_j1 =10
pos_y_j1 =200
pos_x_j2 =largeur-20
pos_y_j2 =0
scorej1=0
scorej2=0
score =''
score+=str(scorej1)
score+='  -  '
score+=str(scorej2)
pygame.init()
ecran = pygame.display.set_mode((largeur,hauteur))
fond= pygame.image.load("image\map.png").convert_alpha()
pygame.display.set_caption("Py-Pong")
ball = pygame.image.load("image/ball.png").convert_alpha()
joueur1 = pygame.image.load("image\joueur1.png").convert_alpha()
joueur2 = pygame.image.load("image\joueur2.png").convert_alpha()
police=pygame.font.Font(None, 30)
text = police.render(score,True,(255,255,255))
position_perso = joueur1.get_rect()
position_perso2 = joueur2.get_rect()
position_perso2[0]=largeur-position_perso2[2]
position_ball = ball.get_rect()
position_ball[0]=250
position_ball[1]=250

x_direction = 1
y_direction = 1
x=60
timer = 1

pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
clock = pygame.time.Clock()
try :
    while continuer:

        if pygame.key.get_pressed()[pygame.K_w] and position_perso[1]>0:
            position_perso = position_perso.move(0,-1)
        if pygame.key.get_pressed()[pygame.K_s] and position_perso[1]<hauteur-position_perso[3]:
            position_perso = position_perso.move(0,1)

        if pygame.key.get_pressed()[pygame.K_UP] and position_perso2[1]>0:
            position_perso2= position_perso2.move(0,-1)
        if pygame.key.get_pressed()[pygame.K_DOWN] and position_perso2[1]<hauteur-position_perso2[3]:
            position_perso2 = position_perso2.move(0,1)

        if position_ball[1]<0 or position_ball[1]>=hauteur-position_ball[2]:
            y_direction = -y_direction
        if position_ball[0]<0  :
            x_direction = -x_direction
            position_ball[0]=250
            position_ball[1]=150
            x=60
            scorej2+=1
            score =''
            score+=str(scorej1)
            score+=' -  '
            score+=str(scorej2)
            text = police.render(score,True,(255,255,255))

        if position_ball[0]>=largeur-position_ball[3]:
            x_direction = -x_direction
            position_ball[0]=250
            position_ball[1]=150
            x=60
            scorej1+=1
            score =''
            score+=str(scorej1)
            score+='  -  '
            score+=str(scorej2)
            text = police.render(score,True,(255,255,255))

        if position_ball[0]==position_perso[0]+position_perso[2] and position_perso[1]-5<position_ball[1]<position_perso[1]+5+position_perso[3] :
            x_direction = -x_direction
            timer+=1

        if position_ball[0]==position_perso2[0]-position_perso2[2]and position_perso2[1]-5<position_ball[1]<position_perso2[1]+5+position_perso2[3]:
            x_direction = -x_direction
            timer+=1

        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
                pygame.quit()
                sys.exit()
        if timer%2==0 and x<960:
            timer+=1
            x+=50

        position_ball[1] +=y_direction
        position_ball[0] +=x_direction
        ecran.blit(fond,(0,0))
        ecran.blit(text,(230,10))
        ecran.blit(ball, position_ball)
        ecran.blit(joueur1, position_perso)
        ecran.blit(joueur2, position_perso2)

        pygame.display.flip()
        clock.tick(x)
except :
    traceback.print_exc()
finally:
    pygame.quit()
    sys.exit()



