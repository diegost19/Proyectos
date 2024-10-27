def Anagrama (palabra1, palabra2):
    palabra1= palabra1.lower()
    palabra2= palabra2.lower()
    if palabra1==palabra2:
        return False
    else:
        if len(palabra1) != len(palabra2):
            return False
        else:
            for x in palabra1:
                if Contador_letras(x,palabra1)!=Contador_letras(x,palabra2):
                    return False
            return True
    
def Contador_letras(letra,palabra):
    contador = 0
    for x in palabra:
        if x == letra:
            contador+=1
    return contador


def Es_Anagrama(palabra1,palabra2):
    if Anagrama(palabra1,palabra2):
        print("Son Anagramas")
    else:
        print("No son Anagramas")

Es_Anagrama("Papelera","arelepap")

 