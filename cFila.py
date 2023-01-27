class NoF:
    def __init__(self, dado, proxNo=None): #Nó
        self.dado = dado
        self.prox = proxNo
    
    def __str__(self): #Formatação
        return str(self.dado)


class Fila: # Fila encadeada
    def __init__(self):
        self.ini = None
        self.fim = None
        self.numObjs = 0

    def enqueue(self, elemento): #adiciona ao fim da fila
        novoNo = NoF(elemento)
        if self.ini == None:
            self.ini = novoNo
            self.fim = novoNo
        else:
            self.fim.prox = novoNo
            self.fim = novoNo

        self.numObjs += 1
        return True

    def dequeue(self): #remove do inicio da fila
        if self.numObjs > 0:
            valorARemover = self.ini
            self.ini = self.ini.prox
            self.numObjs -= 1
            return valorARemover
        if self.ini == None:
            self.fim = None
            return False

    def inicio(self): #inicio da fila
        return self.ini
    
    def vazia(self): #se está vazia
        if self.numObjs == 0:
            return True
        else:
            return False
    
    def tamanho(self): #tamanho
        return self.numObjs
