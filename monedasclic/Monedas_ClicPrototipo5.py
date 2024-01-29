import pygame
from pygame.locals import *
import random

# Inicializamos Pygame
pygame.init()

# Configuración de la pantalla
ancho_pantalla = 1920
alto_pantalla = 1080
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Sumar 1 al hacer clic en una moneda")

# Función para verificar si se hizo clic en una moneda
def ClicMoneda(posRaton, posMoneda):
    global radio_moneda 
    xClic = posRaton[0]
    yClic = posRaton[1]
    xMoneda = posMoneda[0]
    yMoneda = posMoneda[1]
    return xClic > (xMoneda - radio_moneda) and xClic < (xMoneda + radio_moneda) and \
           yClic > (yMoneda - radio_moneda) and yClic < (yMoneda + radio_moneda)

# Función para verificar si se hizo clic en el botón "Quit"
def ClicQuit(posRaton, posQuit):
    global radio_quit
    xClic = posRaton[0]
    yClic = posRaton[1]
    xQuit = posQuit[0]
    yQuit = posQuit[1]
    return xClic > (xQuit - radio_quit) and xClic < (xQuit + radio_quit) and \
           yClic > (yQuit - radio_quit) and yClic < (yQuit + radio_quit)

# Cargar imágenes
fondo = pygame.image.load("fondo.jpg").convert_alpha()
plata = pygame.image.load("platared.jpg").convert_alpha()
bronce = pygame.image.load("broncered.png").convert_alpha()
oro = pygame.image.load("orored.png").convert_alpha()
quit_button = pygame.image.load("quit.png").convert_alpha()

# Constantes
radio_moneda = 125.5
radio_quit = 25
pos_quit = (1850, 20)
tiempo_moneda = 3000  # 3 segundos en milisegundos
puntos = 0
green = 152, 251, 152
blue = 0, 0, 255
font = pygame.font.Font('freesansbold.ttf', 32)
texto_puntos = f"Puntos: {puntos}"
text = font.render(texto_puntos, True, green, blue)


# Lista de tipos de monedas
tipos_monedas = [bronce, plata, oro]

# Inicialización de variables
contador = 3
tiempo_anterior = pygame.time.get_ticks()
pos_moneda = None  # Posición de la moneda actual
tiempo_ultima_moneda = pygame.time.get_ticks()

Funcionando = True

while Funcionando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            Funcionando = False
        if evento.type == MOUSEBUTTONDOWN:
            pos_raton = pygame.mouse.get_pos()
            if ClicQuit(pos_raton, pos_quit):
                Funcionando = False
            elif pos_moneda and ClicMoneda(pos_raton, pos_moneda):
                pos_moneda = None  # La moneda desaparece al hacer clic
                tiempo_ultima_moneda = pygame.time.get_ticks()
                puntos += 1
                # Actualiza el texto
                texto_puntos = f"Puntos: {puntos}"

    pos_raton = pygame.mouse.get_pos()

    pantalla.blit(fondo, (0, 0))

    if pos_moneda is None or pygame.time.get_ticks() - tiempo_ultima_moneda > tiempo_moneda:
        quemoneda = random.choice(tipos_monedas)
        pos_moneda = (random.randint(300, 1620), random.randint(300, 780))
        tiempo_ultima_moneda = pygame.time.get_ticks()

    pantalla.blit(quit_button, pos_quit)
    if pos_moneda:
        pantalla.blit(quemoneda, pos_moneda)

    pygame.display.flip()

    tiempo_actual = pygame.time.get_ticks()

    if tiempo_actual - tiempo_anterior >= 1000:  # Restar 1 cada segundo
        contador -= 1
        tiempo_anterior = tiempo_actual

    # Muestra el texto en pantalla
    textRect = text.get_rect()
    textRect.center = (ancho_pantalla - 1820, alto_pantalla / 2)
    text = font.render(texto_puntos, True, green, blue)
    pantalla.blit(text, textRect)

    pygame.display.flip()

pygame.quit()

#Monedas clic v1.00

#El objetivo del juego es hacer clic a las monedas. Al hacer clic en la moneda esta desaparece y aparece otra. 
