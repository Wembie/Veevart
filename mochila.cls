public class Mochila{

    public static List<List<Integer>> memo;
    public static List<List<List<Integer>>> seleccion;
    public static Integer capacidadMochila;
    public static List<List<Integer>> elementos;

    public static void main() {
        elementos = new List<List<Integer>>();
        elementos.add(new List<Integer>{2, 3});
        elementos.add(new List<Integer>{3, 4});
        elementos.add(new List<Integer>{4, 5});
        elementos.add(new List<Integer>{5, 6});
        capacidadMochila = 8;

        mochila(capacidadMochila);
    }

    public static void mochila(Integer capacidad) {
        memo = new List<List<Integer>>();
        seleccion = new List<List<List<Integer>>>();

        for (Integer i = 0; i < elementos.size() + 1; i++) {
            List<Integer> fila = new List<Integer>();
            for (Integer j = 0; j < capacidad + 1; j++) {
                fila.add(0);
            }
            memo.add(fila);

            List<List<Integer>> filaSeleccion = new List<List<Integer>>();
            for (Integer j = 0; j < capacidad + 1; j++) {
                filaSeleccion.add(new List<Integer>());
            }
            seleccion.add(filaSeleccion);
        }
        
        for (Integer i = 1; i < elementos.size() + 1; i++) {
            for (Integer j = 1; j < capacidad + 1; j++) {
                List<Integer> elementoActual = elementos.get(i - 1);
                Integer valorElemento = elementoActual.get(1);
                Integer pesoElemento = elementoActual.get(0);

                if (pesoElemento <= j) {
                    Integer incluirElemento = valorElemento + memo.get(i - 1).get(j - pesoElemento);
                    Integer excluirElemento = memo.get(i - 1).get(j);

                    if (incluirElemento > excluirElemento) {
                        memo.get(i).set(j, incluirElemento);
                        seleccion.get(i).get(j).addAll(seleccion.get(i - 1).get(j - pesoElemento));
                        seleccion.get(i).get(j).add(i - 1);
                    } else {
                        memo.get(i).set(j, excluirElemento);
                        seleccion.get(i).get(j).addAll(seleccion.get(i - 1).get(j));
                    }
                } else {
                    memo.get(i).set(j, memo.get(i - 1).get(j));
                    seleccion.get(i).get(j).addAll(seleccion.get(i - 1).get(j));
                }
            }
        }

        List<List<Integer>> elementosOff = new List<List<Integer>>();
        Integer valorTotalElementosOff = 0;
        Integer capacidadElementosOff = 0;
        for (Integer i = 0; i < elementos.size(); i++) {
            if (!seleccion.get(elementos.size()).get(capacidad).contains(i)) {
                elementosOff.add(elementos.get(i));
                capacidadElementosOff += elementos.get(i).get(0);
                valorTotalElementosOff += elementos.get(i).get(1);
            }
        }


        System.debug( 'Valor máximo obtenido:' + memo.get(elementos.size()).get(capacidad));
        System.debug('Elementos no llevados fueron: ' + elementosOff + ', su valor total fue de ' + valorTotalElementosOff + '  con una capacidad de ' + capacidadElementosOff + ' para la mochila.');
        
    }
}

Mochila.main();