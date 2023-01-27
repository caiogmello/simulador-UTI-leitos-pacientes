from cPilha import Pilha
import random

class Leitos:
    def __init__(self):
        self.qtd_leitos = 0
        # 3 pilhas de leito criadas
        self.leitos_neonatal = Pilha()
        self.leitos_pediatrico = Pilha()
        self.leitos_adulto = Pilha()

    def gerarID(self, tipo, hosp): # gera hospital de envio e ID de leito aleatórios
        iD = 999
        iD += 1
        # 9 hospitais diferentes. Ex: H9#NEONATAL#1000
        return f'H{hosp}#{tipo}#{iD}'
        
    def numLeitos(self): # retorna número de leitos livres
        return self.leitos_neonatal.tamanho() + self.leitos_pediatrico.tamanho() + self.leitos_adulto.tamanho()

    def mapaLeitos(self): # retorna mapa de leitos livres
        return self.leitos_neonatal.tamanho(), self.leitos_pediatrico.tamanho(), self.leitos_adulto.tamanho()
    
    def mostrarHospital(self): # retorna de qual hospital estão vindo os leitos
        return f'Hospital {self.n_hospital}'
# ==============================================================

    def adicionarLeitos(self, tipo, hosp): # adiciona leitos às pilhas de leitos
        if tipo == 0: # neonatal
            self.leitos_neonatal.insert(self.gerarID("NEONATAL", hosp))
            return True

        elif 0 < tipo < 13: # pediátrico
            self.leitos_pediatrico.insert(self.gerarID("PEDIATRICO", hosp))
            return True

        elif 13 <= tipo: # adulto
            self.leitos_adulto.insert(self.gerarID("ADULTO", hosp))
            return True

    def gerarLeitos(self, num): # gera quantidade de leitos, escolhe de qual hospital virá e executa a função adicionarLeitos()
        self.qtd_leitos += num
        self.n_hospital = random.randint(1,9) # escolhe de qual hospital vai vir a remessa de leitos: (1-9)
        for i in range(num):
            self.tipo = random.randint(0,100)
            self.adicionarLeitos(self.tipo, self.n_hospital)
        return True

# ==============================================================

    def ocuparLeitoNeo(self, num_neo): # ocupa leito neonatal com paciente e o remove da pilha
        for i in range(num_neo):
            self.leitos_neonatal.pop()
        return True
            
    def ocuparLeitoPed(self, num_ped): # ocupa leito pediátrico com paciente e o remove da pilha
        for i in range(num_ped):
            self.leitos_pediatrico.pop()
        return True
            
    def ocuparLeitoAdulto(self, num_adulto): # ocupa leito adulto com paciente e o remove da pilha
        for i in range(num_adulto):
            self.leitos_adulto.pop()   
        return True        

# ==============================================================

    def ocuparLeitos(self, neo, ped, adulto): # ocupa todos os tipos leito com pacientes
        self.ocuparLeitoNeo(neo)
        self.ocuparLeitoPed(ped)
        self.ocuparLeitoAdulto(adulto)

        return self.qtd_leitos
    