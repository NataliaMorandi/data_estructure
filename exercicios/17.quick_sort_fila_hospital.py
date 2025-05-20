class Paciente:
    contador = 2025000

    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
        Paciente.contador += 1
        self.num_prontuario = Paciente.contador  #transformar em lista
        self.proximo = None

class Queue:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def add_paciente(self, novo_paciente):
        if self.tamanho == 0:
            self.inicio = novo_paciente

        else:
            self.fim.proximo = novo_paciente
        self.fim = novo_paciente
        self.tamanho += 1


    def remove_paciente(self):
        if self.tamanho == 0:
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


    def imprimir_fila(self): #busca sequencial
        if self.tamanho > 0:
            ponteiro = self.inicio
            while ponteiro:
                print(ponteiro.nome, ponteiro.idade, ponteiro.num_prontuario)
                ponteiro = ponteiro.proximo
            print( )
        else:
            print("fila vazia")


    def buscar_paciente(self, num_prontuario): #busca sequencial
        if self.tamanho > 0:
            ponteiro = self.inicio
            while ponteiro:
                if ponteiro.num_prontuario == num_prontuario:
                    print(ponteiro.nome, ponteiro.idade, ponteiro.num_prontuario)
                ponteiro = ponteiro.proximo
        else:
            print("fila vazia")


    def swap(self, no_anterior, no_atual):
        auxiliar = no_anterior.nome
        no_anterior.nome = no_atual.nome
        no_atual.nome = auxiliar

        auxiliar = no_anterior.idade
        no_anterior.idade = no_atual.idade
        no_atual.idade = auxiliar

        auxiliar = no_anterior.num_prontuario
        no_anterior.num_prontuario = no_atual.num_prontuario
        no_atual.num_prontuario = auxiliar



        # if no_atual.nome > no_atual.proximo.nome: # C > B
        #     auxiliar = no_atual.proximo           # aux = 200 (B)
        #     no_atual.proximo = auxiliar.proximo   # no_atual.prox = 300 (E)
        #     auxiliar.proximo = no_atual        # aux.prox = C100
        
        #     if no_anterior is not None:           # só entra aqui em trocas que não são logo no [0] com [1]
        #         no_anterior.proximo = auxiliar    # faz a troca entre o menor e o maior. ex: passa o A p/tras do F

        #     else:                                 # só entra aqui em trocas [0] e [1]
        #         self.primeiro = auxiliar          # self.primeiro = B
            
        #     no_anterior = auxiliar 
    
    def pivot(self, primeiro, ultimo): #arrumar
        pivot_valor = primeiro.nome 
        no_anterior = primeiro
        no_atual = primeiro.proximo

        while no_atual is not None and no_atual!= ultimo.proximo:
            if no_atual.nome < pivot_valor:
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
        if pivo != primeiro:
            anterior = primeiro
            while anterior.proximo != pivo and anterior.proximo is not None:
                anterior = anterior.proximo
            self.quick_sort_helper(primeiro, anterior)

        # parte depois do pivô
        if pivo != ultimo:
            self.quick_sort_helper(pivo.proximo, ultimo)
    

    def quick_sort(self): #arrumar
        if self.inicio is None:
            return
        ultimo = self.inicio
        while ultimo.proximo:
            ultimo = ultimo.proximo
        self.quick_sort_helper(self.inicio, ultimo)



p1 = Paciente("Joao", 30)
p2 = Paciente("Maria", 25)
p3 = Paciente("Carlos", 40)
p3 = Paciente("Zara", 18)
p4 = Paciente("Ana", 8)
p5 = Paciente("Bruno", 17)


fila = Queue()

fila.add_paciente(p1)
fila.add_paciente(p2)
fila.add_paciente(p3)
fila.add_paciente(p4)
fila.add_paciente(p5)

#fila.buscar_paciente(102)
fila.imprimir_fila()

fila.quick_sort()

fila.imprimir_fila()