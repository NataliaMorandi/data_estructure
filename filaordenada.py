class No:
    def __init__(self, valor):
        self.valor = valor 
        self.anterior = None
        self.proximo = None
    
class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def adicionar(self, valor):
        nodo = No(valor)
        if self.primeiro == None:
            self.primeiro = nodo

        else:
            self.ultimo.proximo = nodo        
        self.ultimo = nodo
        self.tamanho += 1

    # def percorreFila(self):
    #     # for ponteiro in range(self.tamanho): #nao funciona, Fila nao tem indice
    #     # deveria percorrer a Fila usando um enumerate? não pq vai ser um saco na hora de trocar eles de lugar
    #     ponteiro = self.primeiro
    #     while ponteiro:
    #         pontA = ponteiro.valor #64
    #         ponteiro = ponteiro.proximo #aponta p/34

            

    def percorreFila(self):
        for i in range(0, self.tamanho):
            ponteiro = self.primeiro
            while ponteiro:
                pontA = ponteiro.valor #64
                print(ponteiro.valor)
                ponteiro = ponteiro.proximo #aponta p/proximo 34

                if pontA > ponteiro.proximo.valor:
                    if pontA == self.primeiro:
                        pontA.proximo, ponteiro.proximo = ponteiro.proximo, pontA.proximo
                    print(pontA, "maior", ponteiro.proximo.valor)
            print("passou aqui")
      


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

fila.percorreFila()

