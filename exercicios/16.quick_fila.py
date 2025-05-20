class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0


    def adicionar(self, nodo):
        if self.inicio == None:
            self.inicio = nodoz

        else:
            self.fim.proximo = nodo

        self.fim = nodo
        self.tamanho += 1


    def imprimir(self):
        if self.inicio == None:
            print("Fila vazia")
        else:
            ponteiro = self.inicio
            while ponteiro:
                print(ponteiro.valor)
                ponteiro = ponteiro.proximo
            print(" ")


    def swap(self, no_anterior, no_atual):
        auxiliar = no_anterior.valor
        no_anterior.valor = no_atual.valor
        no_atual.valor = auxiliar


    """
    def pivot(self, primeiro, ultimo): #arrumar
        pivot = self.inicio
        no_anterior = primeiro
        #no_atual = self.inicio.proximo
        no_atual = primeiro.proximo

        for i in range(self.tamanho -1): #preciso de um int do self.inicio.proximo
            if no_atual.valor < pivot.valor:
                swapper = no_atual.proximo
                swap(no_atual, no_atual.proximo)

            else:
                no_anterior = no_atual
                no_atual = no_atual.proximo

        swap(no_atual, pivot)
        return no_atual
    """
    
    def pivot(self, primeiro, ultimo): #arrumar
        pivot_valor = primeiro.valor 
        no_anterior = primeiro
        no_atual = primeiro.proximo

        while no_atual != ultimo.proximo:
            if no_atual.valor < pivot_valor:
                no_anterior = no_anterior.proximo
                self.swap(no_anterior, no_atual)
            no_atual = no_atual.proximo

        self.swap(no_anterior, primeiro) 
        return no_anterior


    def quick_sort_helper(self, primeiro, ultimo):
        if primeiro is None or ultimo is None or primeiro == ultimo:
            return
        
        pivo = self.pivot(primeiro, ultimo)

        # parte antes do pivô
        anterior = primeiro
        while anterior.proximo != pivo and anterior.proximo is not None:
            anterior = anterior.proximo
        self.quick_sort_helper(primeiro, anterior)

        # parte depois do pivô
        self.quick_sort_helper(pivo.proximo, ultimo)


    def quick_sort(self): #arrumar
        if self.inicio is None:
            return
        ultimo = self.inicio
        while ultimo.proximo:
            ultimo = ultimo.proximo
        self.quick_sort_helper(self.inicio, ultimo)


fila = Fila()
fila.adicionar(No(4))
fila.adicionar(No(6))
fila.adicionar(No(1))
fila.adicionar(No(7))
fila.adicionar(No(3))
fila.adicionar(No(2))
fila.adicionar(No(5))

fila.imprimir()

#fila.pivot(fila.inicio)
fila.quick_sort()

fila.imprimir()

