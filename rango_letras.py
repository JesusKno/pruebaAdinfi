def rango_letras(cadena: str):
    if cadena == '':
       return print('Favor de introducir texto')
    
    
    resultado = []
    letra_contar = cadena[0]
    contador = 1
    
    for l in cadena[1:]:
        
        if l == letra_contar:
            contador +=1
        else:
            
            resultado.append(f"{letra_contar}{contador}")
            letra_contar = l
            contador = 1
    
    resultado.append(f"{letra_contar}{contador}")
    
    return print("".join(resultado))


rango_letras('aaacccaaaabbbddda')