from niveles import *
#documentar todas las funciones y los metodos

def mostrar_menu():
    """
    muestra el menu principal del juego
    """
    pygame.init()

    pygame.mixer.music.load("musica_fondo_menu.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Menú")
    fuente = pygame.font.SysFont("Arial", 50)
    fuente_autoria = pygame.font.SysFont("Arial", 30)

    texto_jugar = fuente.render("JUGAR", True, COLOR_AZUL)
    texto_puntajes = fuente.render("PUNTAJES", True, COLOR_AZUL)
    texto_autoria = fuente_autoria.render("JUEGO HECHO POR MARIANO LATTNER", True, COLOR_BLANCO)
    texto_titulo = fuente.render("UNA NAVIDAD DE TERROR", True, COLOR_VERDE)

    imagen_fondo = pygame.image.load("fondo_menu.jpg")
    imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
    crear_bd()
    bandera_corriendo = True
    while bandera_corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                bandera_corriendo = False  
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)
                if (posicion_click[0] > 251 and posicion_click[0] < 388) and (posicion_click[1] > 310 and posicion_click[1] < 350) :
                    mostrar_niveles()                   
                elif (posicion_click[0] > 600 and posicion_click[0] < 810) and (posicion_click[1] > 310 and posicion_click[1] < 350) :
                    mostrar_puntajes()
                
        pantalla.blit(imagen_fondo, (0, 0))
        pantalla.blit(texto_jugar, (250, 300))
        pantalla.blit(texto_puntajes, (600, 300))
        pantalla.blit(texto_autoria, (25, 700))
        pantalla.blit(texto_titulo,(240,100))

        pygame.display.flip()

