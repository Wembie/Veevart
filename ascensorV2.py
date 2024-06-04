#Problema ascensor

from heapq import heappush, heappop

"""
    Simula el funcionamiento de un elevador en un edificio de 29 pisos.

    Args:
        pisosA (list): Lista de pisos a los cuales se llama al elevador en un orden definido.
        inicial (int): Piso inicial de ejecución del elevador.
        estado (str): Dirección inicial del elevador ("subiendo" o "bajando").

    Returns:
        None
"""

def elevador( pisosA, inicial, estado ):
    # Inicialización de variables
    pisosIniciales = []
    cola = {}
    contador = 1
    piso = inicial
    pisos = []
    estadoU = 0
    estadoD = 0
    pisoIr = 0
     # Llenar la cola de prioridad 'pisos' con los pisos a los que se llama el elevador
    for i in range( len( pisosA ) ):
        heappush( pisos, ( 0, pisosA[ i ] ) )
        pisosIniciales.append( pisosA[ i ] )
    # Bucle principal
    while pisos:
        # Imprimir el estado actual del elevador
        print( f"{ contador }. Elevador en piso { piso }" )
        contador += 1
        # Verificar si el elevador llega a un piso llamado
        if piso == pisos[ 0 ][ 1 ]:
            if piso in pisosIniciales and pisoIr < 4:
                #Se le pregunta del piso inicial hacia que piso desea ir
                while True:
                    preguntarPiso = int( input( "Digite hacia que piso deseas ir: " ) )
                    if preguntarPiso != piso:
                        break
                    else:
                        print( "Digita el valor nuevamente, no puede ser igual al piso actual" )
                cola[ piso ] = preguntarPiso
                pisoIr += 1
            # Determinar la dirección del elevador
            if len( pisos ) >= 2 and pisos[ 0 ][ 1 ] < pisos[ 1 ][ 1 ]:
                estado = "subiendo"
            else:
                estado = "bajando"
            # Detener el elevador en el piso llamado y eliminarlo de la lista de pisos a llamar
            heappop( pisos )
            pisosA.remove( piso )
            # Imprimir mensaje de detención del elevador
            print( pisos )
            if len( pisosA ):
                print( f"{ contador }. Elevador se detiene → { pisosA }" )
                contador += 1
                condicion = False
                # Verificar si hay algún piso ingresado en este piso y agregarlo a la cola de prioridad
                if piso in cola.keys():
                    for i in range( len( pisos ) ):
                        if cola[ piso ] == pisos[ i ][ 1 ]:
                            condicion = True
                            break
                    if not condicion:
                        if estado == "subiendo":
                            if preguntarPiso < piso:
                                estadoU += 1
                            else:
                                estadoU -= 1
                            heappush( pisos, ( estadoU, cola[ piso ] ) )
                        else:
                            if preguntarPiso < piso:
                                estadoU -= 1
                            else:
                                estadoU += 1
                            heappush( pisos, ( estadoD, cola[ piso ] ) )
                        pisosA.append( cola[ piso ] )
                        print( f"{ contador }. Piso ingresado { cola[ piso ] } → { pisosA }" )
                        contador += 1
                # Imprimir el estado del elevador (subiendo o bajando)
                print( f"{ contador }. Elevador { estado }" )
                contador += 1
            else:
                print( f"{ contador }. Elevador se detiene" )
                contador += 1
        else:
            # Si el elevador no llega a un piso llamado, imprimir el estado del elevador (subiendo o bajando)
            print( f"{ contador }. Elevador { estado }" )
            contador += 1
        if estado == "subiendo":
            piso += 1
        else:
            piso -= 1

# Ejemplo de uso
pisosA = [ 5, 29, 13, 10 ]
inicial = 4
estado = "subiendo"
elevador( pisosA, inicial, estado )