print("Converter número decimal recebido em uma string em binário")

class Item:
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
        no = Item(valor)
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

def converter(numero):
    pilha = Pilha()
    numero = int(numero)

    while numero > 0:
        restoDivisao = numero % 2
        pilha.inserir(restoDivisao)
        numero = numero // 2
    return pilha
    
numeroStr = input("\nDigite um número decimal: ")

restoDivisao = converter(numeroStr)

print(f"\nO número {numeroStr} em binário é: ")
while not restoDivisao.is_empty():
        print(restoDivisao.remover(), end = "")
  