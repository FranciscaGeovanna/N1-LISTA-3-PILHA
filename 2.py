print("Inverte string")

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

string = input("\nDigite uma palavra: ")

p = Pilha() #pilha vazia

for letra in string:
    p.push(letra)

sInvertida = "" #string vazia
while not p.is_empty():
    sInvertida += p.pop() #remove do topo da pilha e o retorno vai para a string

print("\nPalavra invertida:", sInvertida)