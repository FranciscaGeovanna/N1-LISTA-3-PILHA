print("Converte string em número décimal ")

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

def stringPdecimal(string):
    pilha = Pilha()
    
    for letra in range(len(string) -1, -1, -1):
        if string[letra].isdigit():
            pilha.push(string[letra])
    
    emDecimal = ""
    
    while not pilha.is_empty():
        emDecimal += pilha.pop()
    
    return emDecimal

num = input("\nDigite uma string com números: ")

Strdecimal = stringPdecimal(num)

print(f"\nA String {num} em decimal é:", Strdecimal)


