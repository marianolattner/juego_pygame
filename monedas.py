import pygame
import random
from constantes import *
def crear_monedas(numero_monedas):
        """_summary_
        la funcion crea la cantidad de monedas pasadas por parametro de forma aleatoria a excepcion del centro de la pantalla donde aparece el personaje
        Args:
                numero_monedas (int): cantidad de monedas a crear

        Returns:
                list: retorna la lista con las monedas creadas
        """
        lista_monedas = []
        
        while len(lista_monedas) < numero_monedas:
                posicion_y = random.randrange(100, ALTO_VENTANA - 100, 75)
                posicion_x = random.randrange(100, ANCHO_VENTANA - 100, 75)
                path_moneda = "girar_moneda_0.jpg" 
                if not ((300 < posicion_x < 500) and (250 < posicion_y < 450) and (40 < posicion_x < 160) and (90 < posicion_y < 210) ):
                        imagen_moneda = pygame.image.load(path_moneda)
                        imagen_moneda = pygame.transform.scale(imagen_moneda, (30, 30))
                        rect_moneda = imagen_moneda.get_rect()
                        rect_moneda.x = posicion_x
                        rect_moneda.y = posicion_y

                        dic_moneda = {"imagen": imagen_moneda , "rect_moneda": rect_moneda, "visible" : True}
                        lista_monedas.append(dic_moneda)
        
        return lista_monedas



class Moneda():
        def __init__(self, numero_monedas) -> None:
                self.lista_monedas = crear_monedas(numero_monedas)



