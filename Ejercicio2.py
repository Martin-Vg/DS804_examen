# Dada una lista de strings, implemente una funcion que regrese una lista de tuplas de anagramas.
def anagramas(lista: []):
    resultado = []# Creamos una lista para almacenar las listas de anagramsd
    for palabra in lista:
        encontrado=False# flag por si la palabra es anagrama de otra
        if(len(resultado)==0):# si la lista aun no tiene anagramas se crea uno por default debido que no hay con que comparar
            resultado.append([palabra])
        else:
            for anagramas in resultado:# se itera todos los anagramas previamente creados
                if(sorted(anagramas[0])==sorted(palabra)): # se ordena las letras por abecedario y se commparan para saber si son anagramas
                    anagramas.append(palabra)# se ahrega la palabra en su lista de nagramas
                    encontrado=True# si se encontro la bandera se actiba
                    break
            if(not(encontrado)):# si no esta activa la bandera se crea un lista nueva de anagramas
                resultado.append([palabra])

    return [tuple(x) for x in resultado]# convertimos en tuplas las listas antes de retornar el valor

print(anagramas(["apa","paa","oso","soo","oos"])) 