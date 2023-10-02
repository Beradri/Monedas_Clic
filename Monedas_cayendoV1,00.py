import pygame #importa pygame
import time #importa time 
import random #importa random

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
     global radio 
     xClic = posRaton[0]
     yClic = posRaton[1]
     xQuit = posQuit[0]
     yQuit = posQuit[1]
     return xClic>(xQuit-radio) and xClic<(xQuit+radio) and \
            yClic>(yQuit-radio) and yClic<(yQuit+radio)


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
    if (quemoneda == 1):
            screen.blit(bronce ,  ( random.randint(300, 1620), random.randint(300, 780)))
    if (quemoneda == 2):
            screen.blit(plata ,  ( random.randint(300, 1620), random.randint(300, 780)))
    if (quemoneda == 3):
            screen.blit(oro ,  ( random.randint(300, 1620), random.randint(300, 780)))
    
    pygame.display.flip()

    time.sleep(2)
    Funcionando = False

    


pygame.quit
