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
            self.inicio = nodo

        else:
            self.fim.proximo = nodo

        self.fim = nodo
        self.tamanho += 1

    def remover(self):
        if self.inicio == None:
            print("fila vazia")
         
        ponteiro = self.inicio
        if self.tamanho == 1:
            self.inicio = None
            self.fim = None

        else:
            self.inicio = self.inicio.proximo
            ponteiro.proximo = None

        self.tamanho -= 1
        return ponteiro

    def imprimir(self):
        if self.inicio == None:
            print("Fila vazia")
        else:
            ponteiro = self.inicio
            while ponteiro:
                print(ponteiro.valor)
                ponteiro = ponteiro.proximo
            print(self.tamanho)

n1 = No('AB')
n2 = No('CD')
n3 = No('EF')

fila = Fila()

fila.adicionar(n1)
fila.adicionar(n2)
fila.adicionar(n3)
fila.imprimir()
fila.remover()
fila.imprimir()