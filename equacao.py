# equacao1 = "3 * [(5 - 2) + (4 - 2)]"
# pilha = []

# for char in equacao1:
#     if char in ["[", "(", "{"]:
#         sinal.append(char)
#     if char in ["]", ")", "}"]:
#         if char == "]":
#             find "["
#             list.remove("[")


# print(pilha)

class Sinal:
    def __init__(self, simbolo):
        self.simbolo = simbolo
        self.proximo = None
    
    def __str__(self):
        return self.simbolo
    

class Pilha():
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def inserir(self, sinal):
        if self.topo != None: 
            sinal.proximo = self.topo
        self.topo = sinal
        self.tamanho += 1
        #self.imprimir()

    def imprimir(self):
        if self.tamanho ==0:
            print('equação válida') 
        else: 
            print('equação inválida')
        # print("\nTotal ", self.tamanho)
        # ponteiro = self.topo
        # while ponteiro:
        #     print(ponteiro, end=" ")
        #     ponteiro = ponteiro.proximo
        # print()

    # def conferirSimbolo(self, sinal):
    #     ponteiro = self.topo
    #     while ponteiro:
    #         #if ponteiro == ")":
    #         #    print('achei )')
    #         #else:
    #         #print(ponteiro, end=" ")
    #         ponteiro = ponteiro.proximo
    #     #print()

    def remover(self, simbolo):
        #if self.topo == None:
        #    print("equação inválida")
        #    return
        if (
            (self.topo.simbolo == "(" and simbolo == ")") or
            (self.topo.simbolo == "[" and simbolo == "]") or
            (self.topo.simbolo == "{" and simbolo == "}")
        ):
            self.topo = self.topo.proximo
            self.tamanho -= 1
            return True
        else:
            print("equação invalida")
            return False

def filtrar_simbolos(equacao, pilha):
    for char in equacao:
        if char in "({[":
            pilha.inserir(Sinal(char)) # (Sinal(char)) crio um novo obj na classe Sinal passando char como argumento para o atributo simbolo
                                       # pilha.inserir(...) chama o metodo inserir da instancia pilha, passando o objeto Sinal(char) como argumento
        elif char in ")}]":
            resultado = pilha.remover(char)
            if resultado == False:
                return False
            #passar ponteiro conferindo se existe simbolo correspondente
            #se existir, remover o correspondente. se nao existir print('equação invalida') e parar o codigo

    #print(self.topo)


equacao = "3 * [(5 - 2) + (4 - 2)]"

pilha = Pilha()
filtrar_simbolos(equacao, pilha)
pilha.imprimir()

