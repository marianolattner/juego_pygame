import pygame
import sys
from funciones_juego import *
from constantes import *
from pj import *
from enemigo import *
from monedas import *

class Nivel:
    def __init__(self, fondo, puntaje, segundos, cantidad_monedas, velocidad_enemigo, tamaño_enemigo, caption) -> None:
        self.fondo = fondo
        self.puntaje = puntaje
        self.segundos = segundos
        self.cantidad_monedas = cantidad_monedas
        self.velocidad_enemigo = velocidad_enemigo
        self.tamaño_enemigo = tamaño_enemigo
        self.caption = caption

    def mostrar_nivel(self):
        """_summary_
        muestra el nivel 

        Returns:
            bool: devuelve true en caso de que el jugador haya colisionado con el portal (paso de nivel) o false en caso de que haya colisionado con el enemigo
        """
        fin_tiempo = False
        mostrar_rectangulos = False
        mostrar_musica = True


        pygame.init()
        timer_segundos = pygame.USEREVENT
        pygame.time.set_timer(timer_segundos, 1000)
        pygame.mixer.music.load("musica_fondo.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

        pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        pygame.display.set_caption(self.caption)

        fuente = pygame.font.SysFont("Arial", 35)
        texto_score = fuente.render("SCORE", True, COLOR_VERDE)

        texto_tiempo = fuente.render("TIEMPO", True,COLOR_NEGRO)

        imagen_fondo = pygame.image.load(self.fondo)
        imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
        reloj = pygame.time.Clock()

        personaje_principal = Personaje("caminata_izquierda_t", "caminata_derecha_t", "caminata_arriba_t", "caminata_abajo_t", 3, 400, 350, 10, self.puntaje)
        enemigo = Enemigo("enemigo_izquierda_","enemigo_derecha_", "enemigo_arriba_", "enemigo_abajo_", 4, 600, 200, self.velocidad_enemigo, self.tamaño_enemigo)
        monedas = Moneda(self.cantidad_monedas)
        FPS = 18
        colision_portal = False
        colision_enemigo = False
        while colision_enemigo == False and colision_portal == False :
            reloj.tick(FPS)
            lista_eventos = pygame.event.get()
            for evento in lista_eventos:
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.USEREVENT :
                    if evento.type == timer_segundos :
                        if fin_tiempo == False :
                                self.segundos = int(self.segundos) + 1
            lista_teclas = pygame.key.get_pressed()
            if lista_teclas[pygame.K_RIGHT] :
                personaje_principal.direccion = "d_derecha"
                
            elif lista_teclas[pygame.K_LEFT]:
                personaje_principal.direccion = "d_izquierda"
            
            elif lista_teclas[pygame.K_UP]: 
                personaje_principal.direccion = "d_arriba"
                
            elif lista_teclas[pygame.K_DOWN]:
                personaje_principal.direccion = "d_abajo"

            elif lista_teclas[pygame.K_1]:
                if mostrar_rectangulos == False :
                    mostrar_rectangulos = True
                else :
                    mostrar_rectangulos = False

            elif lista_teclas[pygame.K_2]:
                if mostrar_musica :
                    mostrar_musica = False
                    pygame.mixer.music.pause()
                else :
                    mostrar_musica = True
                    pygame.mixer.music.unpause()

            else:
                personaje_principal.direccion = "d_quieto"
            
            pantalla.blit(imagen_fondo, (0, 0))        
            rect_portal = crear_portal(pantalla)
            
            colision_enemigo = personaje_principal.detectar_colision(enemigo.rect_enemigo)#bool
            colision_portal = personaje_principal.detectar_colision(rect_portal)#bool
            segundos_texto = fuente.render(realizar_reloj(self.segundos),True,COLOR_NEGRO)
            personaje_principal.detectar_colision_moneda(monedas.lista_monedas, fuente, pantalla)
            personaje_principal.animar_personaje(pantalla)
            enemigo.animar(pantalla, personaje_principal.rect_pj)
            
            pantalla.blit(texto_score, (10, 10))
            pantalla.blit(texto_tiempo, (850,10))
            pantalla.blit(segundos_texto, (850, 50))
            

            if mostrar_rectangulos == True:
                pygame.draw.circle(pantalla, COLOR_ROJO, (rect_portal.centerx, rect_portal.centery), 28, 1)
                pygame.draw.rect(pantalla, COLOR_ROJO, personaje_principal.rect_pj, 1)
                pygame.draw.rect(pantalla, COLOR_ROJO, enemigo.rect_enemigo, 1)
                for moneda in monedas.lista_monedas:
                    pygame.draw.circle(pantalla, COLOR_ROJO, (moneda["rect_moneda"].centerx, moneda["rect_moneda"].centery), 14, 1)       

            pygame.display.flip()

        self.puntaje = personaje_principal.puntaje
        
        if colision_portal:
            retorno = colision_portal
        elif colision_enemigo:
            nombre = ingresar_nombre()
            escribir_puntaje(nombre, personaje_principal.puntaje)
            retorno = False

        
        return retorno

    def devolver_segundos(self):
        """_summary_
        la funcion retorna los segundos transcurridos hasta el momento
        Returns:
            int: reloj
        """
        return self.segundos
    
    def devolver_puntajes(self):
        """_summary_
        la funcion retorna el puntaje obtenido hasta el momento
        Returns:
            int: puntaje
        """
        return self.puntaje