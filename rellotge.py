#-*- coding: utf-8 -*-
"""
Created on wend Aug 7 06:19
@file: rellotge.py
@description: creació d'un rellotge digital en finestre pygame
        sortim del bucle amb "QUIT" o sigui "X" en la finestre
@author: Gilbert VIader
"""
#importarem el mòduls pygame datetime i time
import pygame, datetime, time
from pygame.locals import *
#inicialització del mòdul pygame
pygame.init()
finestre = pygame.display.set_mode((650,500))
# rètul del joc i rellotge de cops de repetició del bucle
pygame.display.set_caption("Rellotge digital")
segons = pygame.time.Clock()
#variable boolean de control del bucle
sortir = False
while not sortir:
    for moment in pygame.event.get() :
        if moment.type == pygame.QUIT :
            sortir = True
        elif moment.type == pygame.KEYDOWN :
            if moment.key == pygame.K_ESCAPE :
                sortir = True
        finestre.fill((244, 244, 244))
        tipografia = pygame.font.SysFont(None, 80)   
        dt = datetime.datetime.now()
        #print("{} : {} : {} ".format(dt.hour, dt.minute, dt.second))
        hora = tipografia.render("{} : {} : {}".format(dt.hour, dt.minute, dt.second), 1, (11, 11, 11))
        finestre.blit(hora, (162, 160))
        dia = tipografia.render("{} - {} - {}".format(dt.day, dt.month, dt.year), 1, (177, 0 , 0))
        finestre.blit(dia, (152, 320))
        pygame.display.flip()
        time.sleep(1)
    # càrrega de les imatges a la pantalla
    pygame.display.update()
    segons.tick(60)
# sortida del programa
pygame.quit()
quit()
