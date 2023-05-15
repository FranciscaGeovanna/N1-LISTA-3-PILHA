print("Transforma número em string em décimal ")

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

def converterParaDecimal(string):
    pilha = Pilha()
    r = 0

    for caractere in string:
        pilha.push(int(caractere))

    potencia = 0
    while not pilha.is_empty():
        r += pilha.pop() * (10 ** potencia)
        potencia += 1

    return r


numeros = input("\nDigite uma número: ")
dec = converterParaDecimal(numeros)
print(f"\nO número {numeros} em decimal é: ", dec)








