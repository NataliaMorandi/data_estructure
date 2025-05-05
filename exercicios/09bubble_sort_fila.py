class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0


    def adicionar(self):
        pass

    def imprimir(self):
        pass
    
    def ordenar(self):
        pass 



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
