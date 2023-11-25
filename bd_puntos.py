import sqlite3
from constantes import *
import pygame

def crear_bd():
    """_summary_
    crea la base de datos
    """
    with sqlite3.connect("bd_puntos.db") as conexion:
        try:
            sentencia = '''CREATE TABLE IF NOT EXISTS puntos
            (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            puntaje INTEGER
            )
            '''
            conexion.execute(sentencia)
            print("Se creó la tabla de puntos")
        except sqlite3.OperationalError:
            print("La tabla de puntos ya existe")

def escribir_puntaje(nombre, puntaje):
    """_summary_
    carga el puntaje y el nombre en la base de datos
    Args:
        nombre (str): nombre del jugador
        puntaje (int): puntaje obtenido
    """
    with sqlite3.connect("bd_puntos.db") as conexion:
        try:
            conexion.execute("INSERT INTO puntos(nombre, puntaje) VALUES(?, ?)", (nombre, puntaje))
            conexion.commit()
        except:
            print("Hubo un error al insertar datos")


def leer_puntajes():
    """_summary_
    lee  y ordena la base de datos segun su puntaje en forma descendente con un limite de 5
    Returns:
        _type_: devuelve los datos de la base de datos
    """
    with sqlite3.connect("bd_puntos.db") as conexion:
        cursor = conexion.execute("SELECT nombre, puntaje FROM puntos ORDER BY puntaje DESC LIMIT 5;")

    return cursor

def mostrar_puntajes():
    """_summary_
    muestra el nombre y los puntajes de la base de datos en la pantalla
    """
    fuente_volver = pygame.font.SysFont("Arial", 70)
    texto_volver = fuente_volver.render("VOLVER", True, COLOR_BLANCO)
    puntajes = leer_puntajes()
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Tabla de Puntajes")

    imagen_fondo = pygame.image.load("fondo_puntajes.jpg")
    fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
    pantalla.blit(fondo, (0, 0)) 
    fuente = pygame.font.SysFont("Arial", 50)

    y_pos = 100

    for nombre, puntaje in puntajes:
        texto = fuente.render(f"{nombre}: {puntaje}", True, (255, 255, 255))
        ancho_texto, _ = fuente.size(f"{nombre}: {puntaje}")
        x_pos = (800 - ancho_texto) // 2 
        pantalla.blit(texto, (x_pos, y_pos))
        y_pos += 80 
    pantalla.blit(texto_volver, (700, 600))
    pygame.display.flip()

    corriendo = True
    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(event.pos)
                if (posicion_click[0] > 700 and posicion_click[0] < 930) and (posicion_click[1] > 610 and posicion_click[1] < 665) :
                    return True                  

    pygame.quit()
