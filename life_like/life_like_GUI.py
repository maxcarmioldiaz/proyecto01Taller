import pickle
import easygui as gui
import pygame
import life_like_logic as log

tam = 10
filas = 50
columnas = 50
tick = 10

def main():
    pygame.init()

    clock = pygame.time.Clock()

    #Bienvenida al juego
    gui.msgbox(
        msg= "Bienvenido al juego de la vida, en este juego se simularan diferentes celulas en un" \
        " espacio con las dimensiones que decida ud y a su vez estas celulas naceran o viviran" \
        " segun los parametros que indique proximamente.\n" \
        "Gracias por jugar :D\n" \
        "Desarrollado por: \n" \
        "Maximiliano Carmiol y Santiago Arrieta",
        title= "Bienvenido al Juego de la Vida",
        ok_button= "Quiero Jugar!"
    )

    #Eleccion de cuantos vecinos vivos necesita para que nazca una nueva celula
    loop = True
    while loop:

        B = gui.multchoicebox(
        msg= "Cuantos vecinos deben haber para que nazca una nueva celula?",
        title= "Nacimientos",
        choices= ("0", "1", "2", "3", "4", "5", "6", "7", "8"),
        preselect= None
        )

        if B is None:
            gui.msgbox(
                msg= "Debe ingresar un valor para el parametro \"nacimientos\".",
                title= "Error en el ingreso del valor",
                ok_button = "Ingresar otra vez"
            )

        else:
            B = [int(valor) for valor in B]

            loop = False

    #Eleccion de cuantos vecinos vivos necesita para que las celulas se mantengan vivas
    loop = True
    while loop:

        S = gui.multchoicebox(
        msg= "Cuantos vecinos deben haber para que una celula se mantenga viva?",
        title= "Supervivencia",
        choices= ("0", "1", "2", "3", "4", "5", "6", "7", "8"),
        preselect= None
        )

        if S is None:
            gui.msgbox(
                msg= "Debe ingresar un valor para el parametro \"supervivencia\".",
                title= "Error en el ingreso del valor",
                ok_button = "Ingresar otra vez"
            )

        else:
            S = [int(valor) for valor in S]

            loop = False

    #Eleccion de la cantidad de filas de la matriz
    loop = True
    while loop:

        filas = gui.enterbox(
        msg= "Cuantas filas desea que tenga la matriz para el juego?",
        title= "Dimensiones de la matriz",
        default= "Ingrese aqui un valor entre 1 y 500"
        )

        if filas is None:
            gui.msgbox(
                msg= "Debe ingresar un valor para filas.",
                title= "Error en el ingreso del valor",
                ok_button= "Ingresar otra vez"
            )

        if not filas.isdigit():
            gui.msgbox(
                msg="Debe ingresar un numero para el valor de las filas",
                title= "Error en el ingreso del valor",
                ok_button= "Ingresar otra vez"
            )
        filas = int(filas)
        if filas < 1 or filas > 500:
            gui.msgbox(
                msg="Debe ingresar un numero para el valor mayor a 0 y menor que 500",
                title= "Error en el ingreso del valor",
                ok_button= "Ingresar otra vez"
            )

        else:
            loop = False


    #Eleccion de la cantidad de columnas de la matriz
    loop = True
    while loop:

        columnas = gui.enterbox(
        msg= "Cuantas columnas desea que tenga la matriz para el juego?",
        title= "Dimensiones de la matriz",
        default= "Ingrese aqui un valor entre 1 y 500"
        )

        if columnas is None:
            gui.msgbox(
                msg= "Debe ingresar un valor para columnas.",
                title= "Error en el ingreso del valor",
                ok_button= "Ingresar otra vez"
            )

        if not columnas.isdigit():
            gui.msgbox(
                msg="Debe ingresar un numero para el valor de las columnas",
                title= "Error en el ingreso del valor",
                ok_button= "Ingresar otra vez"
            )
        columnas = int(columnas)
        if columnas < 1 or columnas > 500:
            gui.msgbox(
                msg="Debe ingresar un numero para el valor, mayor a 0 y menor que 500",
                title= "Error en el ingreso del valor",
                ok_button= "Ingresar otra vez"
            )

        else:
            loop = False

    #Eleccion del tamaño de cada celula
    loop = True
    while loop:

        tam = gui.enterbox(
        msg= "De que tamaño desea que sean las celulas?",
        title= "Tamaño de las celulas",
        default= "Ingrese aqui un valor entre 1 y 10"
        )

        if tam is None:
            gui.msgbox(
                msg= "Debe ingresar un valor para el tamaño.",
                title= "Error en el ingreso del valor",
                ok_button= "Ingresar otra vez"
            )

        if not tam.isdigit():
            gui.msgbox(
                msg="Debe ingresar un numero para el valor de las tamaño",
                title= "Error en el ingreso del valor",
                ok_button= "Ingresar otra vez"
            )
        tam = int(tam)
        if tam < 1 or tam > 10:
            gui.msgbox(
                msg="Debe ingresar un numero para el valor entre 1 y 10",
                title= "Error en el ingreso del valor",
                ok_button= "Ingresar otra vez"
            )

        else:
            loop = False

    #Eleccion de matriz vacia o matriz aleatoria
    loop = True
    while loop:

        eleccion = gui.buttonbox(
            msg= "Desea utilizar una matriz vacia o desea que las celulas vivas se coloquen aleatoriamente?",
            title= "Pantalla vacia o celulas aleatorias",
            choices= ("Matriz vacia","Matriz con celulas aleatorias")
        )

        if eleccion is None:
            gui.msgbox(
                msg= "Debe elegir alguna de las 2 opciones",
                title= "Error en la eleccion de la matriz",
                ok_button= "Ingresar otra vez"
            )
        
        if  eleccion != "Matriz vacia" and eleccion != "Matriz con celulas aleatorias":
            gui.msgbox(
                msg= "Debe elegir alguna de las 2 opciones",
                title= "Error en la eleccion de la matriz",
                ok_button= "Ingresar otra vez"
            )
            
        else:
            loop = False

    #Creacion de la matriz segun la eleccion anterior con las filas y columnas indicadas por el usuario
    if eleccion == "Matriz vacia":
        M = log.generar_matriz_vacia(filas, columnas)
    else:
        M = log.generar_matriz_aleatoria(filas, columnas)

    #Tamaño de ventana
    w, h = columnas * tam, filas * tam
    window = pygame.display.set_mode((w, h))

    pausa = False

    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_p]:
                    pausa = not pausa
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                x, y = pygame.mouse.get_pos()
                if buttons[0]:
                    f = y // tam
                    c = x // tam
                    M[f][c] = (M[f][c] + 1) % 2
        
        window.fill((0, 0, 0))
        for f in range(filas):
            for c in range(columnas):
                if M[f][c] == 1:
                    x = c * tam
                    y = f * tam
                    pygame.draw.rect(window, (0, 255, 128), (x, y, tam, tam))
        if not pausa:
            M = log.transicion(M, B, S)
        pygame.display.update()
        clock.tick(10)
    pygame.quit()

if __name__ == "__main__":
    main()
