# Dada una lista de enteros y un entero X, genera una funcion que regrese los indices de dos elementos de la lista cuya suma sea igua la X.

def buscadorSuma(lista: [], numero: int):
    for i1, dato in enumerate(lista, start=0):# creamos un ciclo for para 
        for i2 in range(len(lista)-i1):# iteramos el resto de la lista que no se haya evaluado para no evaluar las mismas sumas dos veces
            # if (dato>numero): # si nuestro numero es mayor no habra suma que nos de el resultado si la funcion le no le daremos numeros negativos descomentar
            #    break
            
            if(dato+lista[i1+i2]==numero):# revisamos si la suma da el numero que buscamos y mandamos los indices
                return ((i1, i1+i2))
    
    return (())# regresamos una tupla vacia si no se encuentra la suma
