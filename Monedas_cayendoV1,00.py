import pygame
from time import * #importa time 
import random #importa random
from pygame import *


#Funciones
def ClicMoneda(posRaton, posMoneda):
     global radio 
     xClic = posRaton[0]
     yClic = posRaton[1]
     xMoneda = posMoneda[0]
     yMoneda = posMoneda[1]
     return xClic>(xMoneda-radio) and xClic<(xMoneda+radio) and \
            yClic>(yMoneda-radio) and yClic<(yMoneda+radio)

def ClicQuit(posRaton, posQuit):
     global radioq 
     xClic = posRaton[0]
     yClic = posRaton[1]
     xQuit = posQuit[0]
     yQuit = posQuit[1]
     return xClic>(xQuit-radioq) and xClic<(xQuit+radioq) and \
            yClic>(yQuit-radioq) and yClic<(yQuit+radioq)


#Constantes
altopantalla = 1080
anchopantalla = 1920
radio = 125.5
radioq = 25
posQuit = ( 1850, 20)
screen = pygame.display.set_mode( (anchopantalla, altopantalla) )
fondo = pygame.image.load("fondo.jpg").convert_alpha()
plata = pygame.image.load("platared.jpg").convert_alpha()
bronce = pygame.image.load("broncered.png").convert_alpha()
oro = pygame.image.load("orored.png").convert_alpha()
quit = pygame.image.load("quit.png").convert_alpha()

#Listas
list1 = [1, 2, 3]

#Comienza el programa

Funcionando = True

while Funcionando:
    screen.blit(fondo ,  ( 0, 0))
    screen.blit(quit , posQuit )
    quemoneda = random.choice(list1)
    posrandom = ( random.randint(300, 1620), random.randint(300, 780))
    if (quemoneda == 1):
        screen.blit(bronce , posrandom )
    if (quemoneda == 2):
        screen.blit(plata ,  posrandom)
    if (quemoneda == 3):
        screen.blit(oro ,  posrandom)
        
    pygame.display.flip()

    if pygame.event == MOUSEBUTTONUP:
           posRaton = mouse.get_pos()
           if ClicQuit(posRaton, posQuit):
                        print('hola')
                        Funcionando = False

       




pygame.quit
#Arreglar todo no va nada no furula es una mierda me estoy rayando mucho ayuda