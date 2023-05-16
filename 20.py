print("Converte de binário para hexadecimal ")

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

    def peek(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self.top.value
    
    def is_empty(self):
        return self.top is None

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
        restoDivisao = numero % 16
        if restoDivisao < 10:
            pilha.push(str(restoDivisao))
        else:
            if restoDivisao == 10:
                pilha.push("A")
            elif restoDivisao == 11:
                pilha.push("B")
            elif restoDivisao == 12:
                pilha.push("C")
            elif restoDivisao == 13:
                pilha.push("D")
            elif restoDivisao == 14:
                pilha.push("E")
            elif restoDivisao == 15:
                pilha.push("F")
        numero = numero // 16
    return pilha

num = input("\nDigite um número em binário: ")

decimal = transforma(num)
hexadecimal = converter(decimal)

print(f"\nO número {num} em hexadecimal é: ")
while not hexadecimal.is_empty():
    print(hexadecimal.pop(), end="")