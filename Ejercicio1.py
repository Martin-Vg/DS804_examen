# Dado un string implemente una funcion que haciendo uso de la tecnica de recursividad, regrese el inverso del string
def stringInverso(string: str):
    #Evaluamos el string para saber si ya llego a su ultimo caracter
    if(string==""):
        return string # Si el string ya no cuenta con caracteres se regresa un texto vacio para ya no volver a llamar la funcion
    else:
        return string[-1] + stringInverso(string[:-1])# En caso de que aun cuente con caracteres regresamos el ultimo caracter mas la funcion menos el ultimo caracter

