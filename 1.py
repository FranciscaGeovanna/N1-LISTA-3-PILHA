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
            raise IndexError("A pilha está vazia!")
        valor = self._topo.valor
        self._topo = self._topo.proximo
        self.tamanho -= 1
        return valor

    def topo(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia!")
        return self._topo.valor

def verifica(expressao):
    pilha = Pilha()
    for p in expressao:
        if p == '(':
            pilha.inserir(p)
        elif p == ')':
            if len(pilha) > 0:
                pilha.remover()
            else:
                pilha.inserir(p)
    return pilha.is_empty()

print("Digite uma expressão matemática para saber se os parênteses estão balanceados: ")
expressao = input("\nExpressão: ")

if verifica(expressao):
    print("\nParênteses balanceados!")
else:
    print("\nParênteses não balanceados!")
