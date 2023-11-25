import pygame
from constantes import *
from bd_puntos import *

def crear_sprite (path_parcial, cantidad, tamaño) :
    """_summary_
    crea una lista con las imagenes que conforman el sprite
    Args:
        path_parcial (str): recibe el path parcial donde esta la imagen
        cantidad (int): cantidad de imagenes que son
        tamaño (tuple): recibe el tamaño de la imagen que va a cargar

    Returns:
        list: retorna una lista con la imagen del personaje creado
    """
    lista = []
    i = 0
    for i in range(cantidad) :
            path = path_parcial + str(i) + ".png"
            imagen_pj = pygame.image.load(path)
            imagen_pj = pygame.transform.scale(imagen_pj, (tamaño))

            lista.append(imagen_pj)
    return lista

def crear_animaciones(path_l,path_r,path_u,path_d, cantidad, tamaño):
    """_summary_
    crea las animaciones a partir de la funcion crear_sprite
    Args:
        path_l (str): path de la imagen caminando hacia la izquierda
        path_r (str): path de la imagen caminando hacia la derecha
        path_u (str): path de la imagen caminando hacia arriba
        path_d (str): path de la imagen caminando hacia abajo
        cantidad (int): cantidad de imagenes que componen el sprite
        tamaño (tuple): recibe el tamaño de la imagen que va a cargar

    Returns:
        dict: retorna un diccionario en el cual la key es el movimiento que esta haciendo el personaje y el value es la lista de pasos
    """
    lista_pasos_izquierda = crear_sprite(path_l, cantidad, tamaño)
    lista_pasos_derecha = crear_sprite(path_r, cantidad, tamaño)
    lista_pasos_arriba = crear_sprite(path_u, cantidad, tamaño)
    lista_pasos_abajo = crear_sprite(path_d, cantidad, tamaño)
    lista_pasos_quieto = crear_sprite(path_d, 1, tamaño)
    dic = {}
    dic["izquierda"] = lista_pasos_izquierda
    dic["derecha"] = lista_pasos_derecha
    dic["arriba"] = lista_pasos_arriba
    dic["abajo"] = lista_pasos_abajo
    dic["quieto"] = lista_pasos_quieto
    return dic


class Personaje() :
    def __init__(self, path_l, path_r, path_u, path_d, cantidad, left, top, velocidad, puntaje : int) -> None:
        self.animaciones = crear_animaciones(path_l, path_r, path_u, path_d, cantidad, (100,100))
        self.rect_pj = self.animaciones["quieto"][0].get_rect()
        self.rect_pj.x = left
        self.rect_pj.y = top
        self.contador_pasos = 0
        self.velocidad = velocidad
        self.direccion = "quieto"
        self.animacion_actual = self.animaciones["quieto"]
        self.puntaje = puntaje
        
        
    def desplazar (self):
        """_summary_
        la funcion mueve el personaje segun la direccion que tenga en ese momento 
        """
        velocidad_actual = self.velocidad
        if self.direccion == "d_izquierda" or  self.direccion == "d_derecha":
            if self.direccion == "d_izquierda":
                velocidad_actual *= -1
            else:
                velocidad_actual = self.velocidad
            self.rect_pj.x += velocidad_actual
        elif self.direccion == "d_arriba" or self.direccion == "d_abajo":
            if self.direccion == "d_abajo":
                velocidad_actual = self.velocidad
            else:
                velocidad_actual *= -1                
            self.rect_pj.y += velocidad_actual
        

    def animar(self):
        """_summary_
        pasa los fotogramas uno atras de otro para simular una animacion
        """
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
            

    def animar_personaje (self, pantalla) :
        """_summary_
        hace lo que hacen las animaciones anteriores pero ademas las blitea en la pantalla

        Args:
            pantalla (_type_): le pasa la pantalla para blitearlo
        """
        match self.direccion :
            case "d_derecha":
                self.animacion_actual = self.animaciones["derecha"]
                if self.rect_pj.x < 900:
                    self.animar()
                    self.desplazar()
                else:
                    self.contador_pasos = 0
            case "d_izquierda":
                self.animacion_actual = self.animaciones["izquierda"]
                if self.rect_pj.x > 0:
                    self.animar()
                    self.desplazar()
                else:
                    self.contador_pasos = 0
            case "d_arriba":
                self.animacion_actual = self.animaciones["arriba"]
                if self.rect_pj.y > 0:
                    self.animar()
                    self.desplazar()
                else:
                    self.contador_pasos = 0
            case "d_abajo":
                self.animacion_actual = self.animaciones["abajo"]
                if self.rect_pj.y < 700:
                    self.animar()
                    self.desplazar()
                else:
                    self.contador_pasos = 0
            case "d_quieto":
                self.animacion_actual = self.animaciones["quieto"]
                self.animar()

        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rect_pj)
        self.contador_pasos += 1

    def detectar_colision(self, rect):
        """_summary_
        detecta la colision con el rectangulo que se le pase por parametro

        Args:
            rect (_type_): recibe el rectangulo con el cual se quiere ver si colisiona el personaje

        Returns:
            bool: en caso de detectar la colision retorna true y en caso contrario false
        """
        sigue_nivel_1 = False
        if self.rect_pj.colliderect(rect):          
            sigue_nivel_1 = True

        return sigue_nivel_1
    
    def detectar_colision_moneda(self,lista_monedas, fuente, pantalla):
        """_summary_
        detecta la colision del personaje con las monedas y si hay colision y es visible la moneda aumenta 10 puntos y cambia su estado de visible de true a false

        Args:
            lista_monedas (list): recibe la lista de monedas creadas
            fuente (_type_): recibe la fuente para escribir el puntaje en la pantalla
            pantalla (_type_): recibe la pantalla para blitear 
        """
        texto_puntaje = fuente.render(str(self.puntaje), True, COLOR_VERDE)
        for moneda in lista_monedas:
                        if self.rect_pj.colliderect(moneda["rect_moneda"]) and moneda["visible"]:
                                moneda["visible"] = False
                                self.puntaje += 10
                                texto_puntaje = fuente.render(str(self.puntaje), True, COLOR_VERDE)  
                        pantalla.blit(texto_puntaje, (10, 50)) 

                        if moneda["visible"]:
                                pantalla.blit(moneda["imagen"], moneda["rect_moneda"])
    