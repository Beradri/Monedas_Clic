import pygame
from pygame.locals import *
import random
import sys

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
elnano = pygame.image.load("elnano.jpg").convert_alpha()

# Constantes
radio_moneda = 250
radio_quit = 50
pos_quit = (1850, 20)
tiempo_moneda = 3000  # 3 segundos en milisegundos
puntos = 0
green = 152, 251, 152
blue = 0, 0, 255
font = pygame.font.Font('freesansbold.ttf', 32)

# Lista de tipos de monedas
tipos_monedas = [bronce, plata, oro]

# Inicialización de variables
contador = 3
tiempo_anterior = pygame.time.get_ticks()
pos_moneda = None  # Posición de la moneda actual
tiempo_ultima_moneda = pygame.time.get_ticks()
tiempo_inicio = pygame.time.get_ticks()

Funcionando = True

# Texto objetivo
texto_objetivo = "El objetivo es hacer clic en 33 monedas en el menor tiempo posible"
font_objetivo = pygame.font.Font('freesansbold.ttf', 32)
text_objetivo = font_objetivo.render(texto_objetivo, True, (0, 0, 0))
text_rect_objetivo = text_objetivo.get_rect(center=(ancho_pantalla // 2, 20))

# Texto cronómetro
font_cronometro = pygame.font.Font('freesansbold.ttf', 32)

# Bucle principal
while Funcionando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            Funcionando = False
        elif evento.type == MOUSEBUTTONDOWN:
            pos_raton = pygame.mouse.get_pos()
            if ClicQuit(pos_raton, pos_quit):
                Funcionando = False
            elif pos_moneda and ClicMoneda(pos_raton, pos_moneda):
                pos_moneda = None  # La moneda desaparece al hacer clic
                tiempo_ultima_moneda = pygame.time.get_ticks()
                puntos += 1
                print(f"Puntos: {puntos}")  # Puedes imprimir el mensaje en la consola
                if puntos == 33:
                    tiempo_final = pygame.time.get_ticks() - tiempo_inicio

                    # Elimina los textos y muestra el fondo en blanco
                    pantalla.fill((255, 255, 255))
                    pygame.display.flip()

                    # Texto especial en rojo en el centro
                    font_especial = pygame.font.Font('freesansbold.ttf', 64)
                    texto_especial = "COMO QUE 33. ME REPITES ESE NUMERÍN???"
                    text_especial = font_especial.render(texto_especial, True, (255, 0, 0))
                    text_rect_especial = text_especial.get_rect(center=(ancho_pantalla // 2, alto_pantalla // 2 - 50))
                    pantalla.blit(text_especial, text_rect_especial)

                    # Tiempo tardado en el centro en la parte de abajo
                    cronometro_texto = f"Tiempo: {tiempo_final / 1000:.3f} s"
                    text_cronometro = font_cronometro.render(cronometro_texto, True, (0, 0, 0))
                    text_rect_cronometro = text_cronometro.get_rect(center=(ancho_pantalla // 2, alto_pantalla - 20))
                    pantalla.blit(text_cronometro, text_rect_cronometro)

                    #Imagen elnano
                    pantalla.blit(elnano, (800, 0))

                    pygame.display.flip()
                    pygame.time.delay(5000)  # Espera 5 segundos antes de salir
                    Funcionando = False

    pos_raton = pygame.mouse.get_pos()
    
    pantalla.blit(fondo, (0, 0))

    if pos_moneda is None or pygame.time.get_ticks() - tiempo_ultima_moneda > tiempo_moneda:
        quemoneda = random.choice(tipos_monedas)
        pos_moneda = (random.randint(300, 1620), random.randint(300, 780))
        tiempo_ultima_moneda = pygame.time.get_ticks()

    pantalla.blit(quit_button, pos_quit)
    if pos_moneda:
        pantalla.blit(quemoneda, pos_moneda)

    # Muestra el texto objetivo
    pantalla.blit(text_objetivo, text_rect_objetivo)

    # Muestra el texto de los puntos
    text_puntos = f"Puntos: {puntos}"
    text = font.render(text_puntos, True, green, blue)
    text_rect = text.get_rect(center=(ancho_pantalla - 1820, alto_pantalla // 2))
    pantalla.blit(text, text_rect)

    # Muestra el cronómetro
    tiempo_transcurrido = (pygame.time.get_ticks() - tiempo_inicio) / 1000
    cronometro_texto = f"Tiempo: {tiempo_transcurrido:.3f} s"
    text_cronometro = font_cronometro.render(cronometro_texto, True, (0, 0, 0))
    text_rect_cronometro = text_cronometro.get_rect(center=(ancho_pantalla // 2, alto_pantalla - 20))
    pantalla.blit(text_cronometro, text_rect_cronometro)


    pygame.display.flip()

pygame.quit()
sys.exit()
