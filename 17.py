print("Transforma octal em décimal")

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
            raise IndexError("A pilha está vazia")
        return self._top.value
    
    def is_empty(self):
        return self._top is None

def transforma(octal):
    pilha = Pilha()
    
    for p in octal:
        pilha.push(int(p))
   
    potencia = 0
    somaPotencias = 0
     
    while not pilha.is_empty():
        somaPotencias += pilha.pop() * (8 ** potencia)
        potencia += 1
    
    return somaPotencias
    
numero = input("\nDigite um número em octal: ")

decimal = transforma(numero)
print(f"\nO número {numero} em decimal é: ", decimal)


