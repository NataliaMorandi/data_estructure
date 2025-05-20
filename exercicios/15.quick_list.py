# import random

# def gerador_lista():
#     lista = []

#     for i in range(5):
#         numero_aleatorio = random.randint(1,50)
#         lista.append(numero_aleatorio)
        
#     print(lista)
#     return lista

#gerador_lista()

def swap(lista, index1, index2):
    temp = lista[index1]
    lista[index1] = lista[index2]
    lista[index2] = temp


def pivot(lista, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if lista[i] < lista[pivot_index]:
            swap_index += 1
            swap(lista, swap_index, i)
    swap(lista, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(lista, left, right):
    if left < right:
        pivot_index = pivot(lista, left, right)
        quick_sort_helper(lista, left, pivot_index -1)
        quick_sort_helper(lista, pivot_index + 1, right)

    return lista 

def quick_sort(lista):
    quick_sort_helper(lista, 0, len(lista)-1)

#print(quick_sort([4, 6, 1, 7, 3, 2, 5]))

lista = [4,6,1,7,3,2,5]

quick_sort(lista)

print(lista)

# lista_aleatoria = gerador_lista()
# lista_ordenada = quick_sort(lista_aleatoria)
# print(lista_ordenada)

# 5 8 11 2 4    