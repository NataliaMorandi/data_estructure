"""
Um hospital deseja implementar um sistema de gerenciamento de entrada de pacientes. Seu chefe quer que você faça isso utilizando 
uma queue simplesmente encadeada.
Cada nó da lista deve armazenar informações sobre um paciente, como nome, idade e número do prontuário de entrada.
A fila deve ser ordenada pelo número do prontuário.

Escreva um programa em Python que permita ao usuário realizar as seguintes operações:

-Adicionar um novo paciente à fila, informando nome, idade e número do prontuário.
O número do prontuário deverá ser um número sequencial. Exemplo: 2503240001, 2503240002, 2503240003,...
-Listar todos os pacientes da lista pelo nome.(Busca sequencial)
-Buscar um paciente pelo número do prontuário.(Busca binária)
"""


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



p1 = Paciente("Joao", 30)
p2 = Paciente("Maria", 25)
p3 = Paciente("Carlos", 40)

fila = Queue()

fila.add_paciente(p1)
fila.add_paciente(p2)
fila.add_paciente(p3)

fila.buscar_paciente(102)
fila.imprimir_fila()