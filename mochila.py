#Problema de la mochila

elementos = [ ( 2, 3 ), ( 3, 4 ), ( 4, 5 ), ( 5, 6 ) ]
capacidadMochila = 8

def mochila( capacidad ):
    memo = [ [ 0 for _ in range( capacidad + 1 ) ] for _ in range( len( elementos ) + 1 ) ]
    seleccion = [ [ [  ] for _ in range( capacidad + 1 ) ] for _ in range( len( elementos ) + 1 ) ]
    for i in range( 1, len( elementos ) + 1 ):
        for j in range( 1, capacidad + 1 ):
            if elementos[ i - 1 ][ 0 ] <= j:
                incluirElemento = elementos[ i - 1 ][ 1 ] + memo[ i - 1 ][ j - elementos[ i - 1 ][ 0 ] ]
                excluirElemento = memo [ i - 1 ][ j ]
                if incluirElemento > excluirElemento:
                    memo[ i ][ j ] = incluirElemento
                    seleccion[ i ][ j ] = seleccion[ i - 1 ][ j - elementos[ i - 1 ][ 0 ] ] + [ i - 1 ]
                else:
                    memo[ i ][ j ] = excluirElemento
                    seleccion[ i ][ j ] = seleccion[ i - 1 ][ j ]
            else:
                memo[ i ][ j ] = memo[ i - 1 ][ j ]
                seleccion[ i ][ j ] = seleccion[ i - 1 ][ j ]
    elementosOff = []
    valorTotalElementosOff = 0
    capacidadElementosOff = 0
    for i in range( len( elementos ) ):
        if i not in seleccion[ len( elementos ) ][ capacidad ]:
            elementosOff.append( elementos[ i ] ) 
            capacidadElementosOff += elementos[ i ][ 0 ]
            valorTotalElementosOff += elementos[ i ][ 1 ]
    print( f"Valor máximo obtenido: { memo[ len( elementos ) ][ capacidad ] }" )
    print( f"Elementos no llevados fueron: { elementosOff }, su valor total fue de { valorTotalElementosOff } con una capacidad de { capacidadElementosOff } para la mochila." )

mochila( capacidadMochila )