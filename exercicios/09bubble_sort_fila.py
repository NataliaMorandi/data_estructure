class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def adicionar(self, nodo):
        if self.inicio == None:
            self.inicio = nodo

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
            print(self.tamanho)
    
    def ordenar(self, no_atual):
        no_anterior = None 

        for i in range(self.tamanho):
            for j in range(self.tamanho -i -1):

                if no_atual.nome > no_atual.proximo.nome: # C > B
                    auxiliar = no_atual.proximo           # aux = 200 (B)
                    no_atual.proximo = auxiliar.proximo   # no_atual.prox = 300 (E)
                    self.inicio.proximo = auxiliar        # aux.prox = C100
                
                    if no_anterior is not None:           # só entra aqui em trocas que não são logo no [0] com [1]
                        no_anterior.proximo = auxiliar    # faz a troca entre o menor e o maior. ex: passa o A p/tras do F

                    else:                                 # só entra aqui em trocas [0] e [1]
                        self.primeiro = auxiliar          # self.primeiro = B
                    
                    no_anterior = auxiliar                # no_anterior = B (o menor)

                else:                                     # muda o ponteiro pq o atual é menor que o proximo e não precisa trocar os dois de lugar. ex C < E
                    no_anterior = no_atual                # anterior = C
                    no_atual = no_atual.proximo           # atual passa a ser E
                    

fila = Fila()
fila.adicionar(64)
fila.adicionar(34)
fila.adicionar(25)
fila.adicionar(12)
fila.adicionar(22)
fila.adicionar(11)
fila.adicionar(90)

fila_ordenada = fila.ordenar()

imprimir(fila_ordenada)
