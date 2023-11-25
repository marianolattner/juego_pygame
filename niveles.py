from class_nivel import *

def mostrar_niveles():
    """_summary_
    muestra los niveles y los va pasando si es que tiene que pasar y si no lo devuelve al menu principal
    """
    nivel_1 = Nivel("fondo.jpg", 0, 0, 10, 4, (70,70), "Nivel 1")
    corriendo_nivel_1= nivel_1.mostrar_nivel()
    if corriendo_nivel_1 == False:
        return True
    elif corriendo_nivel_1 == True:
        tiempo_actual = nivel_1.devolver_segundos()
        puntaje_actual = nivel_1.devolver_puntajes()
        nivel_2 = Nivel("fondo_nivel_2.jpg", puntaje_actual, tiempo_actual, 12, 5, (90,90), "Nivel 2")
        corriendo_nivel_2 = nivel_2.mostrar_nivel()
        if corriendo_nivel_2 == False:
            return True
        elif corriendo_nivel_2 == True:
            tiempo_actual = nivel_2.devolver_segundos()
            puntaje_actual = nivel_2.devolver_puntajes()
            nivel_3 = Nivel("fondo_nivel_3.jpg", puntaje_actual, tiempo_actual, 15, 8, (130,130), "Nivel 3")
            corriendo_nivel_3 = nivel_3.mostrar_nivel()
            if corriendo_nivel_3 == False:
                return True
            elif corriendo_nivel_3 == True:
                juego_ganado()