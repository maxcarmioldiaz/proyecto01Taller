import pickle
import easygui as gui
import pygame 
import hormiga_logic as log
from random import randrange

tam = 10
filas = 50
columnas = 50

def main():
    pygame.init()
    clock = pygame.time.Clock()
    global tam, filas, columnas

    #Bienvenida

    gui.msgbox(
        msg=   "Bienvenido a la Hormiga de Langton!\n"
               "En este automata una hormiga recorre una matriz y va cambiando\n"
               "los colores de las celdas segun las reglas que usted defina.\n\n"
               "Desarrollado por:\n"
               "Maximiliano Carmiol y Santiago Arrieta",
        title= "Bienvenido a la Hormiga de Langton",
        ok_button= "Quiero jugar!"
    )

    #Cargar automata o crear nuevo

    eleccion_inicio = gui.buttonbox(
        msg = "Tiene un automata guardado que desee utilizar?",
        title = "Inicio",
        choices = ("Si, quiero usar mi automata guardado", "No, quiero crear un nuevo automata")
        
    )

    if eleccion_inicio == "Si, quiero usar mi automata guardado":
        loop = True
        while loop:
            ruta = gui.fileopenbox(
                msg = "Seleccione el archivo de su automata guardado",
                title = "Cargar Hormiga de Langton",
            )
            if ruta is None:
                eleccion = gui.buttonbox(
                    msg=    "No selecciono ningun archivo",
                    title=  "Sin archivo seleccionado",
                    choices= ("Intentar otra vez", "No quiero cargar")
                )
                if eleccion == "No quiero cargar":
                    loop = False
            else:
                try:
                    archivo = open(ruta, "rb")
                    datos   = pickle.load(archivo)
                    archivo.close()
    
                    matriz = datos["matriz"]
                    filas = datos["filas"]
                    columnas = datos["columnas"]
                    tam = datos["tamaño"]
                    reglas = datos["reglas"]
                    fila_hormiga = datos["fila_hormiga"]
                    columna_hormiga = datos["columna_hormiga"]
                    direccion_hormiga = datos["direccion_hormiga"]
    
                    ancho_ventana = columnas * tam
                    alto_ventana = filas * tam
                    ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
                    pygame.display.set_caption("Hormiga de Langton")
    
                    loop = False
                except Exception as e:
                    gui.msgbox(
                    msg=      "Ocurrio un error al cargar el archivo. Intentelo de nuevo.",
                    title=    "Error al cargar",
                    ok_button= "Elegir otro archivo"
                )
    else:
        
        #Pedir reglas

        loop = True
        while loop:
            reglas = gui.enterbox(
                msg=     "Ingrese las reglas de la hormiga.\n"
                         "Use solo letras L (izquierda) y R (derecha).\n"
                         "Cada letra representa un color.\n"
                         "Ejemplo: LR es la hormiga original, LLRR genera patrones simetricos.",
                title=   "Reglas de la hormiga",
                default= "LR"
            )
        
            if reglas is None or reglas.strip() == "":
                gui.msgbox(
                    msg=      "Debe ingresar al menos una regla.",
                    title=    "Error en las reglas",
                    ok_button= "Ingresar otra vez"
                )
    
            elif not all(letra in "LRlr" for letra in reglas):
                gui.msgbox(
                    msg=      "Las reglas solo pueden contener letras L y R.",
                    title=    "Error en las reglas",
                    ok_button= "Ingresar otra vez"
                )
    
            else:
                reglas = reglas.upper()
                loop   = False
        
        # Pedir la cantidad de filas
        
        loop = True
        while loop:
    
            respuesta_filas = gui.enterbox(
                msg=     "Cuantas filas desea que tenga la matriz?",
                title=   "Filas de la matriz",
                default= "50"
            )
    
            if respuesta_filas is None:
                gui.msgbox(
                    msg=      "Debe ingresar un valor para las filas.",
                    title=    "Error",
                    ok_button= "Ingresar otra vez"
                )
    
            elif not respuesta_filas.isdigit():
                gui.msgbox(
                    msg=      "Debe ingresar un numero entero para las filas.",
                    title=    "Error",
                    ok_button= "Ingresar otra vez"
                )
    
            elif int(respuesta_filas) < 1 or int(respuesta_filas) > 500:
                gui.msgbox(
                    msg=      "El valor de las filas debe estar entre 1 y 500.",
                    title=    "Error",
                    ok_button= "Ingresar otra vez"
                )
    
            else:
                filas = int(respuesta_filas)
                loop  = False
    
        
        # Pedir la cantidad de columnas
        
        loop = True
        while loop:
    
            respuesta_columnas = gui.enterbox(
                msg=     "Cuantas columnas desea que tenga la matriz?",
                title=   "Columnas de la matriz",
                default= "50"
            )
    
            if respuesta_columnas is None:
                gui.msgbox(
                    msg=      "Debe ingresar un valor para las columnas.",
                    title=    "Error",
                    ok_button= "Ingresar otra vez"
                )
    
            elif not respuesta_columnas.isdigit():
                gui.msgbox(
                    msg=      "Debe ingresar un numero entero para las columnas.",
                    title=    "Error",
                    ok_button= "Ingresar otra vez"
                )
    
            elif int(respuesta_columnas) < 1 or int(respuesta_columnas) > 500:
                gui.msgbox(
                    msg=      "El valor de las columnas debe estar entre 1 y 500.",
                    title=    "Error",
                    ok_button= "Ingresar otra vez"
                )
    
            else:
                columnas = int(respuesta_columnas)
                loop     = False
        # Pedir el tamaño de las celdas
        
        loop = True
        while loop:
 
            respuesta_tam = gui.enterbox(
                msg=     "De que tamaño desea que sean las celdas? (entre 1 y 20)",
                title=   "Tamaño de las celdas",
                default= "10"
            )
    
            if respuesta_tam is None:
                gui.msgbox(
                    msg=      "Debe ingresar un valor para el tamaño.",
                    title=    "Error",
                    ok_button= "Ingresar otra vez"
                )
    
            elif not respuesta_tam.isdigit():
                gui.msgbox(
                    msg=      "Debe ingresar un numero entero para el tamaño.",
                    title=    "Error",
                    ok_button= "Ingresar otra vez"
                )
    
            elif int(respuesta_tam) < 1 or int(respuesta_tam) > 20:
                gui.msgbox(
                    msg=      "El tamaño debe estar entre 1 y 20.",
                    title=    "Error",
                    ok_button= "Ingresar otra vez"
                )
    
            else:
                tam  = int(respuesta_tam)
                loop = False
        # Crear la matriz - valores 0s
        matriz = [[0 for c in range(columnas)] for f in range(filas)]

        # Posicion inicial de la hormiga
        fila_hormiga      = filas    // 2
        columna_hormiga   = columnas // 2
        direccion_hormiga = "arriba"

        #Ventana de pygame
        ancho_ventana = columnas * tam
        alto_ventana  = filas    * tam
        ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
        pygame.display.set_caption("Hormiga de Langton")

        #Mostras controles
        gui.msgbox(
            msg=   "Controles del juego:\n\n"
                "ESPACIO: Pausa y continua la simulacion\n"
                "R:       Reinicia la matriz (con colores aleatorios)\n"
                "B:       Reinicia la matriz con la hormiga en el centro\n"
                "G:       Guardar el estado del automata\n"
                "C:       Cargar un automata guardado\n\n"
                "Recomendacion: pause el juego antes de guardar o cargar.",
            title=    "Controles",
            ok_button= "Entendido!"
        )

        #Lista de colores
        lista_colores = log.generar_colores(len(reglas))

        #Bucle principal
        pausa = False
        loop  = True
    
        while loop:
    
            for evento in pygame.event.get():
    
                if evento.type == pygame.QUIT:
                    loop = False   

                if evento.type == pygame.KEYDOWN:
                    teclas = pygame.key.get_pressed()

                    if teclas[pygame.K_SPACE]:
                        pausa = not pausa

                    if teclas[pygame.K_r]:
                        matriz            = [[0 for c in range(columnas)] for f in range(filas)]
                        fila_hormiga      = filas    // 2
                        columna_hormiga   = columnas // 2
                        direccion_hormiga = "arriba"
 
                    if teclas[pygame.K_b]:
                        matriz            = [[0 for c in range(columnas)] for f in range(filas)]
                        fila_hormiga      = filas    // 2
                        columna_hormiga   = columnas // 2
                        direccion_hormiga = "arriba"
    
                    if teclas[pygame.K_g]:
                        tecla = True
                        while tecla:
 
                            ruta = gui.filesavebox(
                                msg=   "Seleccione donde desea guardar el automata",
                                title= "Guardar Hormiga de Langton"
                            )
    
                            if ruta is None:
                                eleccion = gui.buttonbox(
                                    msg=    "No selecciono ninguna ruta de guardado",
                                    title=  "Sin ruta seleccionada",
                                    choices= ("Intentar otra vez", "No quiero guardar")
                                )
                                if eleccion == "No quiero guardar":
                                    tecla = False
    
                            else:
                                archivo = open(ruta, "wb")
                                pickle.dump({
                                    "matriz"           : matriz,
                                    "filas"            : filas,
                                    "columnas"         : columnas,
                                    "tamaño"           : tam,
                                    "reglas"           : reglas,
                                    "fila_hormiga"     : fila_hormiga,
                                    "columna_hormiga"  : columna_hormiga,
                                    "direccion_hormiga": direccion_hormiga
                                }, archivo)
                                archivo.close()
                                tecla = False
 
                    if teclas[pygame.K_c]:
                        tecla = True
                        while tecla:
 
                            ruta = gui.fileopenbox(
                                msg=   "Seleccione el archivo del automata a cargar",
                                title= "Cargar Hormiga de Langton"
                            )
 
                            if ruta is None:
                                eleccion = gui.buttonbox(
                                    msg=    "No selecciono ningun archivo",
                                    title=  "Sin archivo seleccionado",
                                    choices= ("Intentar otra vez", "No quiero cargar")
                                )
                                if eleccion == "No quiero cargar":
                                    tecla = False
 
                            else:
                                try:
                                    archivo = open(ruta, "rb")
                                    datos   = pickle.load(archivo)
                                    archivo.close()
 
                                    matriz            = datos["matriz"]
                                    filas             = datos["filas"]
                                    columnas          = datos["columnas"]
                                    tam               = datos["tamaño"]
                                    reglas            = datos["reglas"]
                                    fila_hormiga      = datos["fila_hormiga"]
                                    columna_hormiga   = datos["columna_hormiga"]
                                    direccion_hormiga = datos["direccion_hormiga"]
 
                                    lista_colores = log.generar_colores(len(reglas))
 
                                    ancho_ventana = columnas * tam
                                    alto_ventana  = filas    * tam
                                    ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
 
                                    tecla = False
 
                                except Exception:
                                    gui.msgbox(
                                        msg=      "Ocurrio un error al cargar el archivo.",
                                        title=    "Error al cargar",
                                        ok_button= "Elegir otro archivo"
                                    )

            for f in range(filas):
                for c in range(columnas):
                    color_celda = lista_colores[matriz[f][c]]
                    x_celda     = c * tam
                    y_celda     = f * tam
                    pygame.draw.rect(ventana, color_celda, (x_celda, y_celda, tam, tam))

            x_hormiga = columna_hormiga * tam
            y_hormiga = fila_hormiga    * tam
            pygame.draw.rect(ventana, (80, 80, 80), (x_hormiga, y_hormiga, tam, tam))

            if not pausa:
                matriz, fila_hormiga, columna_hormiga, direccion_hormiga = log.siguiente(
                    matriz, fila_hormiga, columna_hormiga, direccion_hormiga, reglas
                )

            pygame.display.update()
            clock.tick(120)
 
    pygame.quit()
 
 
if __name__ == "__main__":
    main()
