import string


def numero_letra(numero: int):
    if(numero < 1):
        print("Por favor de introducir un numero valido")
    
    letra_numero_calcular = numero
    contador = 0
    
    resultado = []
    
    
    while letra_numero_calcular > 0:
        letra_numero_calcular = (letra_numero_calcular - 1) // 26
        contador += 1
    
    numero2 = numero
    
    
    for _ in range(contador):
        
        numero2, restante = divmod(numero2 - 1, 26)
        resultado.append(string.ascii_uppercase[restante])
    
    return print("".join(reversed(resultado)))


numero_letra(28)