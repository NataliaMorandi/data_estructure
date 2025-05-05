import random

def gerador_lista():
    lista = []

    for i in range(10):
        numero_aleatorio = random.randint(1,50)
        lista.append(numero_aleatorio)
        
    print(lista)
    return lista

gerador_lista()