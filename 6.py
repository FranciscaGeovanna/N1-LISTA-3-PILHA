class Item:
    def __init__(self, value):
        self.value = value
        self.next = None

class Pilha:
    def __init__(self):
        self.top = None
        self.size = 0
   
    def __len__(self):
        return self.size
    
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
        return self.top.value
    
    def is_empty(self):
        return self.top is None

def balanceado(expressao):
    pilha = Pilha()
    for caractere in expressao:
        if caractere in "([{":
            pilha.push(caractere)
        elif caractere in ")]}":
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.push(caractere)
                
    return pilha.is_empty()

exp = input("Digite uma expressão para saber se os caracteres estão balanceados: ")

if balanceado(exp):
    print("\nOs caracteres estão balanceados!")
else:
    print("\nOs caracteres não estão balanceados!")
