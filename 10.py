class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self._topo = None
        self.tamanho = 0
   
    def __len__(self):
        return self.tamanho
   
    def is_empty(self):
        return self.tamanho == 0
   
    def inserir(self, valor):
        no = No(valor)
        no.proximo = self._topo
        self._topo = no
        self.tamanho += 1
   
    def remover(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        valor = self._topo.valor
        self._topo = self._topo.proximo
        self.tamanho -= 1
        return valor
   
    def topo(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self._topo.valor


def valida(expressao):
    pilha = Pilha()
    for caractere in expressao:
        if caractere == '(':
            pilha.inserir(caractere)
        elif caractere == ')':
            if len(pilha) > 0:
                pilha.remover()
            else:
                pilha.inserir(caractere)
        else:
            pilha.inserir(caractere)
    return pilha.is_empty()

def infixa_para_posfixa(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operadores = Pilha()
    posfixa = []
    numeros = '0123456789'
    for caracter in expressao:
        if caracter in numeros:
            posfixa.append(caracter)
        elif caracter == '(':
            operadores.inserir(caracter)
        elif caracter == ')':
            while operadores.topo() != '(':
                posfixa.append(operadores.remover())
            operadores.remover()
        elif caracter in precedencia:
            while not operadores.is_empty()  \
                and operadores.topo() != '(' \
                and precedencia[caracter] <= precedencia[operadores.topo()]:
                posfixa.append(operadores.remover())
            operadores.inserir(caracter)
    while not operadores.is_empty():
        posfixa.append(operadores.remover())
    return ''.join(posfixa)


exp = input("Digite uma expressão matemática para verificar se é válida: ")
if valida(exp):
    print("\nA expressão é válida!")
else:
    print("\nA expressão não é válida!")
