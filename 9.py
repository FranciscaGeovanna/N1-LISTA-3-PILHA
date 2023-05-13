print("Mostra se o número na string é um políndromo")

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

string = input("\nDigite um número: ")

pilha = Pilha() 

for numero in string:
    pilha.push(numero)

sInvertida = "" 
while not pilha.is_empty():
    sInvertida += pilha.pop() 

print("Número invertida:", sInvertida)

if sInvertida == string:
    print("\nO número é um políndromo!")
else:
    print("\nO número não é um políndromo!")
