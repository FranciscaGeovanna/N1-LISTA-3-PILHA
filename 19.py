print("Converte de binário para octal")

class Item:
    def __init__(self, value):
        self.value = value
        self.next = None

class Pilha:
    def __init__(self):
        self._top = None
        self.size = 0
   
    def __len__(self):
        return self.size
    
    def push(self, value):
        novoItem = Item(value)
        novoItem.next = self._top
        self._top = novoItem
        self.size += 1
   
    def pop(self):
        if self.size == 0:
            raise Exception("\nA pilha está vazia!")
        valor = self._top.value
        self._top = self._top.next
        self.size -= 1
        return valor

    def top(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia!")
        return self._top.value
    
    def is_empty(self):
        return self._top is None

def transforma(binario):
    pilha = Pilha()
    
    string = str(binario)

    for p in string:
        pilha.push(int(p))
   
    potencia = 0
    somaPotencias = 0
     
    while not pilha.is_empty():
        somaPotencias += pilha.pop() * (2 ** potencia)
        potencia += 1
    
    return somaPotencias

def converter(numero):
    pilha = Pilha()
    while numero > 0:
        restoDivisao = numero % 8
        pilha.push(restoDivisao)
        numero = numero // 8
    return pilha

num = int(input("\nDigite um número em binário: "))

decimal = transforma(num)
decimalPoctal = converter(decimal)

print(f"\nO número {num} em octal é: ")
while not decimalPoctal.is_empty():
    print(decimalPoctal.pop(), end = "")
