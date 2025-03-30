
class Lista:
    def __init__(self, a:int = 0, b:int = 10, numeroEscolhido:int = 4): 
        self.lista = list(range(a, b))
        self.numeroEscolhido = numeroEscolhido
        self.inicio = 0
        self.fim = len(self.lista) -1 
        self.count = 0


    def buscaBinaria(self):
        #numeroEscolhido = int(input("Digite o número que deseja buscar: "))
        while self.inicio <= self.fim:
            meio = (self.inicio + self.fim) // 2
            self.count += 1  

            if self.lista[meio] == self.numeroEscolhido:
                print(f"Achei o {self.numeroEscolhido} na posicao {meio} em {self.count} operacoes.")
                return meio
            elif self.lista[meio] < self.numeroEscolhido:
                self.inicio = meio + 1  
            else:
                self.fim = meio - 1  
            
        print("Número não encontrado!")
        return -1  

l1 = Lista(0, 50, 47)

l1.buscaBinaria()