import pygame #importa pygame
from time import * #importa time 
import random #importa random
from pygame import * #vuelve a imnportar pygame por si acaso :)



#Funciones

#Función del clic en una moneda 
def ClicMoneda(posRaton, posMoneda):
     global radio 
     xClic = posRaton[0]
     yClic = posRaton[1]
     xMoneda = posMoneda[0]
     yMoneda = posMoneda[1]
     return xClic>(xMoneda-radio) and xClic<(xMoneda+radio) and \
            yClic>(yMoneda-radio) and yClic<(yMoneda+radio)

#Función del clic en el botón de cerrar vel programa
def ClicQuit(posRaton, posQuit):
     global radioq 
     xClic = posRaton[0]
     yClic = posRaton[1]
     xQuit = posQuit[0]
     yQuit = posQuit[1]
     return xClic>(xQuit-radioq) and xClic<(xQuit+radioq) and \
            yClic>(yQuit-radioq) and yClic<(yQuit+radioq)


#Constantes
altopantalla = 1080 #define el alto de la pantalla
anchopantalla = 1920 #define el ancho de la pantalla
pygame.display.set_caption("Restar 1 cada segundo")
radio = 125.5 #define el radio de las monedas
radioq = 25 #define el radio del botón de quit
posQuit = (1850, 20) #define la posición del botón de quit
screen = pygame.display.set_mode( (anchopantalla, altopantalla) ) #define las dimensiones de la pantalla
fondo = pygame.image.load("fondo.jpg").convert_alpha() #convierte fondo en una imagen
plata = pygame.image.load("platared.jpg").convert_alpha() #convierte plata en una imagen
bronce = pygame.image.load("broncered.png").convert_alpha() #convierte bronce en una imagen
oro = pygame.image.load("orored.png").convert_alpha() #convierte oro en una imagen
quit = pygame.image.load("quit.png").convert_alpha() #convierte quit en una imagen
contador = 3


#Listas
list1 = [1, 2, 3] #da los valores a list1

#Comienza el programa

Funcionando = True

while Funcionando:
    contador = 0
    screen.blit(fondo ,  ( 0, 0))
    screen.blit(quit , posQuit )
    quemoneda = random.choice(list1)
    posrandom = (random.randint(300, 1620), random.randint(300, 780))
    if (quemoneda == 1):
        screen.blit(bronce , posrandom )
    if (quemoneda == 2):
        screen.blit(plata ,  posrandom)
    if (quemoneda == 3):
        screen.blit(oro ,  posrandom)
    pygame.display.flip()
    contador = 3
    tiempo_anterior = pygame.time.get_ticks()
    while contador > 0:
        lista_eventos = event.get()
        for evento in lista_eventos:
            if evento.type == MOUSEBUTTONUP:
                posRaton = mouse.get_pos()
            if ClicQuit(posRaton, posQuit):
                Funcionando = False
            if ClicMoneda(posRaton, posrandom):
                print('Clic dentro de una moneda')
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - tiempo_anterior >= 3000:  
            contador -= 3
            tiempo_anterior = tiempo_actual
 
   


pygame.quit
