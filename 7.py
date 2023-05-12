print("Converte número décimal em octal")

class Item:
    def __init__(self, value):
        self.value = value
        self.next = None

class Pilha:
    def __init__(self):
        self.top = None
        self.size = 0
   
    def __len__(self):
        return self.tamanho
    
    def push(self, value):
        novoItem = Item(value)
        novoItem.next = self.top
        self.top = novoItem
        self.size += 1
   
    def pop(self):
        if self.size == 0:
            raise Exception("\nA pilha está vazia!")
        valor = self.top.value
        self.top = self.top.next
        self.size -= 1
        return valor

    def top(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia!")
        return self._top.valor
    
    def is_empty(self):
        return self.top == None

def converter(numero):
    pilha = Pilha()
    while numero > 0:
        restoDivisao = numero % 8
        pilha.push(restoDivisao)
        numero = numero // 8
    return pilha
 
numero = int(input("\nDigite um número decimal: "))
restoDivisao = converter(numero)

print(f"\nO número {numero} em octal é: ")
while not restoDivisao.is_empty():
    print(restoDivisao.pop(), end = "")
    
    