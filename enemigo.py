from pj import *

class Enemigo() :  
    def __init__(self, path_l, path_r, path_u, path_d, cantidad, left, top, velocidad, tamaño) -> None:
        self.animaciones = crear_animaciones(path_l, path_r, path_u, path_d, cantidad, tamaño)
        self.rect_enemigo = self.animaciones["izquierda"][0].get_rect()
        self.rect_enemigo.x = left
        self.rect_enemigo.y = top
        self.contador_pasos_enemigo = 0
        self.velocidad = velocidad
        self.direccion_enemigo = "izquierda"
        self.animacion_actual = self.animaciones["izquierda"]

    def desplazar(self, rect_pj):
        """_summary_
        el metodo desplaza al enemigo en direccion al personaje
        Args:
            rect_pj (_type_): recibe el rectangulo del personaje para perseguirlo
        """
        delta_x = rect_pj.x - self.rect_enemigo.x
        delta_y = rect_pj.y - self.rect_enemigo.y
        # Calcula la distancia entre el enemigo y el personaje principal
        distancia = ((delta_x ** 2) + (delta_y ** 2)) ** 0.5
        # Calcula el desplazamiento necesario en las coordenadas x e y para que el enemigo siga al personaje
        try:
            desplazamiento_x = (delta_x / distancia) * self.velocidad
            desplazamiento_y = (delta_y / distancia) * self.velocidad
        except ZeroDivisionError:
            print("division por 0, no se puede hacer")
        # Actualiza las coordenadas del enemigo
        self.rect_enemigo.x += desplazamiento_x
        self.rect_enemigo.y += desplazamiento_y


        if abs(delta_x) > abs(delta_y):
            if delta_x > 0:
                self.direccion_enemigo = "derecha"
                self.animacion_actual = self.animaciones["derecha"]
                

            else:
                self.direccion_enemigo = "izquierda"
                self.animacion_actual = self.animaciones["izquierda"]

        else:
            if delta_y > 0:
                self.direccion_enemigo = "abajo"
                self.animacion_actual = self.animaciones["abajo"]


            else:
                self.direccion_enemigo = "arriba"
                self.animacion_actual = self.animaciones["arriba"]


    def animar(self, pantalla, rect_pj):
        """_summary_
        pasa las imagenes para simular el movimiento
        Args:
            pantalla (_type_): recibe la pantalla donde se blitea la imagen
            rect_pj (_type_): recibe el rectangulo del personaje
        """
        largo = len(self.animacion_actual)
        if self.contador_pasos_enemigo >= largo:
            self.contador_pasos_enemigo = 0
        self.desplazar(rect_pj)

        pantalla.blit(self.animacion_actual[self.contador_pasos_enemigo], self.rect_enemigo)
        self.contador_pasos_enemigo += 1
