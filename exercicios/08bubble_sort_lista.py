import random

def gerador_lista():
    lista = []

    for i in range(5):
        numero_aleatorio = random.randint(1,50)
        lista.append(numero_aleatorio)
        
    print(lista)
    return lista

#gerador_lista()

def bubble_sort(lista):
    for i in range(0, len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j+1]:
                auxiliar = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = auxiliar
    return lista 

lista_aleatoria = gerador_lista()
lista_ordenada = bubble_sort(lista_aleatoria)
print(lista_ordenada)

# 5 8 11 2 4            