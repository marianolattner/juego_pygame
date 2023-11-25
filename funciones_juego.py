import pygame
import sys
from constantes import *

def realizar_reloj (segundos) :
    """_summary_
    convierte la cantidad de segundos al formato reloj
    Args:
        segundos (int): segundos

    Returns:
        int: retorna los segundos en formato reloj
    """
    
    seg = int(segundos) % 60
    min = int(segundos) // 60
    if seg < 10 :
        seg = f"0{seg}"
    if min < 10 :
        min = f"0{min}"

    resultado = f"{min} : {seg}"
    return resultado

def crear_portal(pantalla):
    """_summary_
    carga la imagen del portal, la blitea en la pantalla y crea el rect alrededor de la imagen
    Args:
        pantalla (_type_): recibe como parametro la pantalla para poder blitear el portal

    Returns:
        _type_: retorna el rect portal
    """
    imagen_portal = pygame.image.load("portal.png")
    imagen_portal = pygame.transform.scale(imagen_portal, (60, 60))
    rect_portal = imagen_portal.get_rect()
    rect_portal.x = 100
    rect_portal.y = 150
    pantalla.blit(imagen_portal,(100,150))
    return rect_portal


def juego_ganado():
    """_summary_
    blitea una pantalla donde el usuario puede ingresar su nombre para cargarlo a la base de datos cuando gana
    Returns:
        str: retorna el nombre ingresado
    """
    copa_del_mundo = "copa_del_mundo.png"

    imagen_copa = pygame.image.load(copa_del_mundo)
    imagen_copa = pygame.transform.scale(imagen_copa, (150,150))

    pygame.init()

    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    font_input = pygame.font.SysFont("Arial", 50)
    font_message_large = pygame.font.SysFont("Arial", 60)  
    font_message_small = pygame.font.SysFont("Arial", 30)

    ingreso = ""
    ingreso_rect = pygame.Rect(200, 400, 400, 40)  
    imagen_fondo = pygame.image.load("fondo_navidad.jpg")
    fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))


    correr = True
    while correr:
        pantalla.blit(fondo, (0, 0)) 

        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                correr = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    ingreso = ingreso[0:-1]
                elif evento.key == pygame.K_RETURN:
                    if len(ingreso) >= 3:
                        correr = False
                else:
                    ingreso += evento.unicode

    
        mensaje_surface = font_message_small.render("Ingrese su nombre de jugador", True, COLOR_BLANCO)
        mensaje_rect = mensaje_surface.get_rect(topleft=(150, 300))
        pantalla.blit(mensaje_surface, mensaje_rect.topleft)

        pygame.draw.rect(pantalla, COLOR_BLANCO, ingreso_rect, 2)
        font_input_surface = font_input.render(ingreso, True, COLOR_BLANCO)

        text_rect = font_input_surface.get_rect(center=ingreso_rect.center)
        pantalla.blit(font_input_surface, text_rect.topleft)
    
        felicitaciones_surface = font_message_large.render("¡Felicitaciones!", True, COLOR_BLANCO)
        felicitaciones_rect = felicitaciones_surface.get_rect(center=(ANCHO_VENTANA // 2, 200))
        pantalla.blit(felicitaciones_surface, felicitaciones_rect.topleft)


        for i in range(3):
                copa_rect = imagen_copa.get_rect(topleft=(250 + i * 200, 20))
                pantalla.blit(imagen_copa, copa_rect.topleft)
        pygame.display.flip()

    return ingreso



def ingresar_nombre():
    """_summary_
    blitea una pantalla donde el usuario puede ingresar su nombre para cargarlo a la base de datos cuando pierde
    Returns:
        str: retorna el nombre ingresado
    """
    grinch = "grinch.jpg"
    imagen_grinch = pygame.image.load(grinch)
    imagen_grinch = pygame.transform.scale(imagen_grinch, (150, 150))
    fuente_game_over = pygame.font.SysFont("Arial", 70)
    texto_game_over = fuente_game_over.render("GAME OVER", True, COLOR_NEGRO)
    pygame.init()

    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    font_input = pygame.font.SysFont("Arial", 50)
    font_message = pygame.font.SysFont("Arial", 30)

    ingreso = ""
    ingreso_rect = pygame.Rect(200, 400, 400, 40)
    imagen_fondo = pygame.image.load("fondo_nieve.jpg")
    fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
    correr = True

    while correr:
        pantalla.blit(fondo, (0, 0))

        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                correr = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    ingreso = ingreso[0:-1]
                elif evento.key == pygame.K_RETURN:
                    if len(ingreso) >= 3:
                        correr = False
                else:
                    ingreso += evento.unicode

        mensaje_surface = font_message.render("Ingrese su nombre de jugador", True, COLOR_NEGRO)
        mensaje_rect = mensaje_surface.get_rect(topleft=(200, 200))
        pantalla.blit(mensaje_surface, mensaje_rect.topleft)

        pygame.draw.rect(pantalla, COLOR_NEGRO, ingreso_rect, 2)
        font_input_surface = font_input.render(ingreso, True, COLOR_ROJO)

        text_rect = font_input_surface.get_rect(center=ingreso_rect.center)
        pantalla.blit(font_input_surface, text_rect.topleft)
        pantalla.blit(imagen_grinch, (700, 350))
        pantalla.blit(texto_game_over, (280, 50))
        pygame.display.flip()

    return ingreso