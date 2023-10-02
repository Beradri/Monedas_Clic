import pygame 
import time
import random

#Constantes
altopantalla = 1080
anchopantalla = 1920
screen = pygame.display.set_mode( (anchopantalla, altopantalla) )
oro = pygame.image.load("oro.jpg")
plata = pygame.image.load("plata.png")
bronce = pygame.image.load("monedabronce.jpg")
fondo = pygame.image.load("fondo.jpg").convert_alpha()

#Variables
posalto = 0

#Listas
list1 = [1, 2, 3]

#Código
Funcionando = True

while Funcionando:
    screen.blit(fondo ,  ( 0, 0))
    quemoneda = random.choice(list1)
    while (posalto<500):
        screen.blit(fondo ,  ( 0, 0))
        if (quemoneda == 1):
            screen.blit(bronce ,  ( 0, posalto))
        if (quemoneda == 2):
            screen.blit(plata ,  ( 0, posalto))
        if (quemoneda == 3):
            screen.blit(oro ,  ( 0, posalto))

        posalto = posalto + 5
        pygame.display.flip()

    
    Funcionando = False
    

time.sleep (2)
pygame.quit



#Lista de cosas pendientes

#Arreglar que aparezcan las imágenes
#Escalar imágenes
#Hacer clic funcional
#Que se sumen los puntos
#Hacer monedas más fáciles que otras