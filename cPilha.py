class NoP:
    def __init__(self, dado, antNo=None): #Nó 
        self.dado = dado
        self.ant = antNo
    
    def __str__(self): #Formatação
        return str(self.dado)


class Pilha: # Pilha encadeada
    def __init__(self):
        self.topo = None
        self.numObjs = 0

    def insert(self, elemento): #adiciona ao topo da pilha
        novoNo = NoP(elemento)
        novoNo.ant = self.topo
        self.topo = novoNo

        self.numObjs += 1
        return True

    def pop(self): #remove do topo da pilha
        if self.numObjs > 0:
            valorARemover = self.topo
            self.topo = self.topo.ant
            self.numObjs -= 1
            return valorARemover
        else:
            return False

    def top(self): #topo
        return self.topo

    def vazia(self): #se está vazia
        if self.numObjs == 0:
            return True
        else:
            return False
    
    def tamanho(self): #tamanho
        return self.numObjs