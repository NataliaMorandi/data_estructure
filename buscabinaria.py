
class Lista:
    def __init__(self, a:int = 0, b:int = 10, numeroEscolhido:int = 4): 
        self.lista = list(range(a, b))
        self.numeroEscolhido = numeroEscolhido
        self.inicio = 0
        self.fim = len(self.lista) -1 


    def buscaSequencial(self):
        count = 0
        for indice, values in enumerate(self.lista):
            count += 1
            if values == self.numeroEscolhido:
                print(f"Achei o {self.numeroEscolhido} na posicao {indice} em {count} operacoes sequenciais")
                return indice
        print("Numero nao encontrado na busca sequencial!")
        return -1
            


    def buscaBinaria(self):
        self.inicio = 0
        self.fim = len(self.lista) -1
        count = 0 
        while self.inicio <= self.fim:
            meio = (self.inicio + self.fim) // 2
            count +=1

            if self.lista[meio] == self.numeroEscolhido:
                print(f"Achei o {self.numeroEscolhido} na posicao {meio} em {count} operacoes binarias.") 
                return meio
            elif self.lista[meio] < self.numeroEscolhido:
                self.inicio = meio + 1  
            else:
                self.fim = meio - 1  
            
        print("Numero nao encontrado na busca binaria!")
        return -1  

l1 = Lista(4, 55, 48)

l1.buscaSequencial()
l1.buscaBinaria()
#l1.buscaBinaria()

l2 = Lista(0, 10, 9)
l2.buscaSequencial()
l2.buscaBinaria()