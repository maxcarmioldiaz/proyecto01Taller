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

    #Cargar automata en el inicio
    eleccion = gui.buttonbox(
        msg= "Tiene un automata guardado que desee utilizar?",
        title= "Inicio",
        choices= ("Sí, quiero usar mi automata", "No, iniciaré uno nuevo")
    )
    if eleccion == "Sí, quiero usar mi automata":
        loop = True
        while loop:

            #Pregunta la ruta de carga
            ruta = gui.fileopenbox(
            msg= "Seleccione el automata a ejecutar",
            title= "Cargar Automata Life-Like",
            default= None 
            )

            #En caso de cerrar la ventana (Retorna None) pregunta si se desea cargar o no
            if ruta == None:
                eleccion = gui.buttonbox(
                    msg= "No seleccionó ningun archivo a cargar",
                    title= "No se cargó ningun programa",
                    choices= ("Intentar otra vez", "No quiero cargar")
                    )
                            
                #En caso de no quererse cargar termina el bucle y continua con el programa
                if eleccion == "No quiero cargar":
                    loop = False
                        
            #Recibe la ruta de carga y abre el archivo de la ruta
            else:
                try:
                    file = open(ruta, "rb")
                    datos = pickle.load(file)
                    file.close()         

                    #Recupera los datos cargados y los guarda en sus respectivas variables
                    M = datos["matriz"]
                    filas = datos["filas"]
                    columnas = datos["columnas"]
                    tam = datos["tamaño"]
                    B = datos["B"]
                    S = datos["S"]

                    #Carga la ventana con las dimensiones que tiene que tener segun el archivo cargado
                    w, h = columnas * tam, filas * tam
                    window = pygame.display.set_mode((w, h))

                    loop = False

                except Exception:
                    gui.msgbox(
                        msg= "Ocurrio un error en la carga del archivo",
                        title= "Error en la carga",
                        ok_button= "Elegir otra vez"
                        )
                    
            #Controles del juego
            gui.msgbox(
                "P: Pausa \n" \
                "R: Reinicia la matriz con valores aleatorios \n" \
                "B: Reinicia la matriz totalmente vacia \n" \
                "G: Guardar el automata \n" \
                "C: Cargar un automata\n" \
                "Recomendacion: En caso de querer cargar o guardar un automata pause el juego para asi " \
                "poder ver su estado antes de guardarlo o en su contraparte su estado antes de cargarlo." \
                " Tambien en caso de utilizar una matriz vacia recomendamos pause el juego con la " \
                "tecla P para asi poder colocar los automatas vivos a su gusto y comodidad. \n" \
                "Disfrute el juego :D",
                title= "Controles del juego",
                ok_button= "Entendido!"
        )
    
    else:
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
            default= "50"
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
            default= "50"
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
            default= "5"
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
                
            else:
                loop = False

        #Controles del juego
        gui.msgbox(
            "Barra Espaciadora: Pausa \n" \
            "R: Reinicia la matriz con valores aleatorios \n" \
            "B: Reinicia la matriz totalmente vacia \n" \
            "G: Guardar el automata \n" \
            "C: Cargar un automata \n" \
            "Recomendacion: En caso de querer cargar o guardar un automata pause el juego para asi " \
            "poder ver su estado antes de guardarlo o en su contraparte su estado antes de cargarlo." \
            " Tambien en caso de utilizar una matriz vacia recomendamos pause el juego con la " \
            "tecla P para asi poder colocar los automatas vivos a su gusto y comodidad. \n" \
            "Disfrute el juego :D",
            title= "Controles del juego",
            ok_button= "Entendido!"
        )
        #Creacion de la matriz segun la eleccion anterior con las filas y columnas indicadas por el usuario
        if eleccion == "Matriz vacia":
            M = log.generar_matriz_vacia(filas, columnas)
        else:
            M = log.generar_matriz_aleatoria(filas, columnas)

        #Tamaño de ventana
        w, h = columnas * tam, filas * tam
        window = pygame.display.set_mode((w, h))

    pausa = False
    #Inicio
    loop = True
    while loop:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if keys[pygame.K_SPACE]:
                    pausa = not pausa

                #Reiniciar con valores neutros con la tecla b
                if keys[pygame.K_b]:

                        #Se crea la matriz vacia (es decir con valores neutros)
                        M = log.generar_matriz_vacia(filas, columnas)

                #Reiniciar con valores aleatorios con la tecla r
                if keys[pygame.K_r]:

                        #Se crea la matriz con valores aleatorios
                        M = log.generar_matriz_aleatoria(filas, columnas)
                
                #Guarda el estado actual del automata junto con todas sus caracteristicas en un archivo
                if keys[pygame.K_g]:

                    tecla = True
                    while tecla:

                        #Pregunta la ruta de guardado
                        ruta = gui.filesavebox(
                            msg= "Seleccione donde desea guardar el automata",
                            title= "Guardar Automata Life-Like",
                            default= None 
                        )

                        #En caso de cerrar la ventana (Retorna None) pregunta si se desea guardar o no
                        if ruta == None:
                            eleccion = gui.buttonbox(
                                msg= "No seleccionó ninguna ruta de guardado",
                                title= "No se guardó el autómata",
                                choices= ("Intentar otra vez", "No quiero guardar")
                            )
                            
                            #En caso de no quererse guardar termina el bucle y continua con el programa
                            if eleccion == "No quiero guardar":
                                tecla = False
                        
                        #Recibe la ruta de guardado y guarda el archivo en la ruta
                        else:
                            file = open(ruta, "wb")
                            pickle.dump({
                                "matriz" : M,
                                "filas" : filas,
                                "columnas" : columnas,
                                "tamaño" : tam,
                                "B" : B,
                                "S" : S
                            }, 
                            file)
                            file.close()

                            tecla = False
                        


                #Carga el estado del automata que proviene de un archivo previamente guardado
                if keys[pygame.K_c]:
                    tecla = True
                    while tecla:

                        #Pregunta la ruta de carga
                        ruta = gui.fileopenbox(
                            msg= "Seleccione el automata a ejecutar",
                            title= "Cargar Automata Life-Like",
                            default= None 
                        )

                        #En caso de cerrar la ventana (Retorna None) pregunta si se desea cargar o no
                        if ruta == None:
                            eleccion = gui.buttonbox(
                                msg= "No seleccionó ningun archivo a cargar",
                                title= "No se cargó ningun programa",
                                choices= ("Intentar otra vez", "No quiero cargar")
                            )
                            
                            #En caso de no quererse cargar termina el bucle y continua con el programa
                            if eleccion == "No quiero cargar":
                                tecla = False
                        
                        #Recibe la ruta de carga y abre el archivo de la ruta
                        else:
                            try:
                                file = open(ruta, "rb")
                                datos = pickle.load(file)
                                file.close()         

                                #Recupera los datos cargados y los guarda en sus respectivas variables
                                M = datos["matriz"]
                                filas = datos["filas"]
                                columnas = datos["columnas"]
                                tam = datos["tamaño"]
                                B = datos["B"]
                                S = datos["S"]

                                #Carga la ventana con las dimensiones que tiene que tener segun el archivo cargado
                                w, h = columnas * tam, filas * tam
                                window = pygame.display.set_mode((w, h))

                                tecla = False

                            except Exception:
                                gui.msgbox(
                                        msg= "Ocurrio un error en la carga del archivo",
                                        title= "Error en la carga",
                                        ok_button= "Elegir otra vez"
                                        )


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
