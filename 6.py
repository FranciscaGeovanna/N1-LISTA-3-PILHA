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

def balanceado(expressao):
    pilha = Pilha()
    
    abrir = ['(', '[', '{']
    fechar = [')', ']', '}']
    
    for caractere in expressao:
        if caractere in abrir:
            pilha.push(caractere)
        elif caractere in fechar:
            if pilha.is_empty:
                return False

        elif caractere == '(':
            if pilha.top() == ')':
                pilha.pop()
            else:
                return False

        elif caractere == '{':
            if pilha.top() == '}':
                pilha.pop()  
            else:
                return False

        elif caractere == '[':
            if pilha.top() == ']':
                pilha.pop()
            else:
                return False
       
    return pilha.is_empty()
    
exp = input ("Digite uma expressão para saber se os caracteres estão balanceados: ")
    
if balanceado(exp):
    print("\nOs caracteres estão balanceados!")
else:
    print("\nOs caracteres não estão balanceados!")
    





