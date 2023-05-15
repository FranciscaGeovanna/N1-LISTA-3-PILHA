print("Ordena pilha em ordem crescente ")

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
        return self._top == None

def ordenar(pilha):
    pilhaOrdenada = Pilha()

    while not pilha.is_empty():
        num = pilha.pop()
        while not pilhaOrdenada.is_empty() and pilhaOrdenada.top() > num: #enquanto a pilha não estiver vazia e o número no topo for maior
            pilha.push(pilhaOrdenada.pop())
        pilhaOrdenada.push(num)

    return pilhaOrdenada


quant = int(input("\nQuantos números deseja ordenar? "))

guardarNumeros = Pilha()

for i in range(quant):    
    numero = int(input(f"Digite o {i+1}° número: "))
    guardarNumeros.push(numero)

pilhaCrescente = ordenar(guardarNumeros)

#inverter pilha
p = Pilha()

while not pilhaCrescente.is_empty():
    p.push(pilhaCrescente.pop())
    
print("\nPilha em ordem crescente: ")
while not p.is_empty():
    print(p.pop(), end=' ')





