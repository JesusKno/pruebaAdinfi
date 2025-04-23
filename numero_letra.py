import string


def numero_letra(numero: int):
    if(numero < 0):
        print("Por favor de introducir un numero valido")
    
    letra = string.ascii_letters[numero]
    
    return print(letra)


numero_letra(1)