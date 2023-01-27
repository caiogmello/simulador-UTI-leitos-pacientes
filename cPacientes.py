from cFila import Fila
import random

class Pacientes:
    def __init__(self):
        # contadores
        self.num_pacientes = 0
        self.num_atendidos = 0

        # 9 filas diferentes de pacientes criadas
        self.fila_emergencia_neonatal = Fila()
        self.fila_emergencia_pediatrico = Fila()
        self.fila_emergencia_adulto = Fila()

        self.fila_mto_urgente_neonatal = Fila()
        self.fila_mto_urgente_pediatrico = Fila()
        self.fila_mto_urgente_adulto = Fila()

        self.fila_urgente_neonatal = Fila()
        self.fila_urgente_pediatrico = Fila()
        self.fila_urgente_adulto = Fila()

    def numPacientes(self): # retorna número total de pacientes já passados pela fila
        return self.num_pacientes

    def numAtendidos(self): # retorna número de atendidos
        return self.num_atendidos

    def tamFila(self): # retorna quantidade de pacientes na fila atual
        self.tam_fila_emergencia = self.fila_emergencia_neonatal.tamanho() + self.fila_emergencia_pediatrico.tamanho() + self.fila_emergencia_adulto.tamanho()
        self.tam_fila_mto_urgente = self.fila_mto_urgente_neonatal.tamanho() + self.fila_mto_urgente_pediatrico.tamanho() + self.fila_mto_urgente_adulto.tamanho()
        self.tam_fila_urgente = self.fila_urgente_neonatal.tamanho() + self.fila_urgente_pediatrico.tamanho() + self.fila_urgente_adulto.tamanho()

        return  self.tam_fila_emergencia + self.tam_fila_mto_urgente + self.tam_fila_urgente

    def gerarID(self, grau, idade): # gera ID de paciente aleatório
        self.id = random.randint(2000000, 3000000)
        # exemplo: G3-43-ID2000000
        return f'G{grau}-{idade}-ID{self.id}'

# ==============================================================

    def entrarNaFila(self, idade, gravidade): # adiciona pacientes na fila com base na idade de na gravidade          
            
            if idade == 0 and gravidade == 3: #neonatal / emergência
                self.fila_emergencia_neonatal.enqueue(self.gerarID(gravidade, idade))
                return True

            elif 0 < idade < 13 and gravidade == 3: #pediatrico / emergência
                self.fila_emergencia_pediatrico.enqueue(self.gerarID(gravidade, idade))
                return True

            elif 13 <= idade and gravidade == 3: #adulto / emergência
                self.fila_emergencia_adulto.enqueue(self.gerarID(gravidade, idade))
                return True

            #======================================================================

            elif idade == 0 and gravidade == 2: #neonatal / muito urgente
                self.fila_mto_urgente_neonatal.enqueue(self.gerarID(gravidade, idade))
                return True

            elif 0 < idade < 13 and gravidade == 2: #pediátrico / muito urgente
                self.fila_mto_urgente_pediatrico.enqueue(self.gerarID(gravidade, idade))
                return True
            
            elif 13 <= idade and gravidade == 2: #adulto / muito urgente
                self.fila_mto_urgente_adulto.enqueue(self.gerarID(gravidade, idade))
                return True

            #======================================================================

            elif idade == 0 and gravidade == 1: #neonatal / urgente
                self.fila_urgente_neonatal.enqueue(self.gerarID(gravidade, idade))
                return True

            elif 0 < idade < 13 and gravidade == 1: #neonatal / urgente
                self.fila_urgente_pediatrico.enqueue(self.gerarID(gravidade, idade))
                return True
            
            elif 13 <= idade and gravidade == 1: #neonatal / urgente
                self.fila_urgente_adulto.enqueue(self.gerarID(gravidade, idade))
                return True

    def gerarPacientes(self, num): # gera quantidade de pacientes e executa função entrarNaFila()
            self.num_pacientes += num
            for i in range(num):
                self.idade = random.randint(0,100)
                self.grau = random.randint(1,3)

                self.entrarNaFila(self.idade, self.grau)
            return True

# ==============================================================    
#   
    def mapaTotalAtual(self): # retorna o mapa total de pacientes nas filas com base nos tipos
        self.tam_fila_neo = self.fila_emergencia_neonatal.tamanho() + self.fila_mto_urgente_neonatal.tamanho() + self.fila_urgente_neonatal.tamanho()
        self.tam_fila_ped = self.fila_emergencia_pediatrico.tamanho() + self.fila_mto_urgente_pediatrico.tamanho() + self.fila_urgente_pediatrico.tamanho()
        self.tam_fila_adulto = self.fila_emergencia_adulto.tamanho() + self.fila_mto_urgente_adulto.tamanho() + self.fila_urgente_adulto.tamanho()

        return  self.tam_fila_neo, self.tam_fila_ped, self.tam_fila_adulto

    def mapaEmergencia(self): # retorna o mapa de pacientes em emergência nas filas com base no tipos
        return self.fila_emergencia_neonatal.tamanho(), self.fila_emergencia_pediatrico.tamanho(), self.fila_emergencia_adulto.tamanho()

    def mapaMtoUrgente(self): # retorna o mapa de pacientes em muita urgência nas filas com base no tipos
        return self.fila_mto_urgente_neonatal.tamanho(), self.fila_mto_urgente_pediatrico.tamanho(), self.fila_mto_urgente_adulto.tamanho()

    def mapaUrgente(self): # retorna o mapa de pacientes em urgência nas filas com base no tipo
        return self.fila_urgente_neonatal.tamanho(), self.fila_urgente_pediatrico.tamanho(), self.fila_urgente_adulto.tamanho()

# ===============================================================

    def enviarParaLeitoNeonatal(self, qtd): # envia pacientes para o leito neonatal e os remove da fila

        contador = qtd
        tam_emergencia = self.fila_emergencia_neonatal.tamanho()
        tam_mto_urgente = self.fila_mto_urgente_neonatal.tamanho()
        tam_urgente = self.fila_urgente_neonatal.tamanho()

        # ordem EMERGÊNCIA -> MUITO URGENTE -> URGENTE (sempre)

        while tam_emergencia > 0: 
            if contador == 0:
                break 
            self.fila_emergencia_neonatal.dequeue()
            self.num_atendidos += 1
            tam_emergencia -= 1
            contador -= 1

        while tam_mto_urgente > 0:
            if contador == 0:
                break 
            self.fila_mto_urgente_neonatal.dequeue()
            self.num_atendidos += 1
            tam_mto_urgente -= 1
            contador -=1
            
        while tam_urgente > 0:
            if contador == 0:
                break 
            self.fila_urgente_neonatal.dequeue()
            self.num_atendidos += 1
            tam_urgente -= 1
            contador -=1

        return True

    def enviarParaLeitoPediatrico(self, qtd): # envia pacientes para o leito pediátrico e os remove da fila

        contador = qtd
        tam_emergencia = self.fila_emergencia_pediatrico.tamanho()
        tam_mto_urgente = self.fila_mto_urgente_pediatrico.tamanho()
        tam_urgente = self.fila_urgente_pediatrico.tamanho()

       # ordem EMERGÊNCIA -> MUITO URGENTE -> URGENTE (sempre)
    
        while tam_emergencia > 0:
            if contador == 0:
                break 
            self.fila_emergencia_pediatrico.dequeue()
            self.num_atendidos += 1
            tam_emergencia -= 1
            contador -= 1

        while tam_mto_urgente > 0:
            if contador == 0:
                break 
            self.fila_mto_urgente_pediatrico.dequeue()
            self.num_atendidos += 1
            tam_mto_urgente -= 1
            contador -=1
            
        while tam_urgente > 0:
            if contador == 0:
                break 
            self.fila_urgente_pediatrico.dequeue()
            self.num_atendidos += 1
            tam_urgente -= 1
            contador -=1

        return True

    def enviarParaLeitoAdulto(self, qtd): # envia pacientes para o leito adulto e os remove da fila

        contador = qtd
        tam_emergencia = self.fila_emergencia_adulto.tamanho()
        tam_mto_urgente = self.fila_mto_urgente_adulto.tamanho()
        tam_urgente = self.fila_urgente_adulto.tamanho()

        # ordem EMERGÊNCIA -> MUITO URGENTE -> URGENTE (sempre)

        while tam_emergencia > 0:
            if contador == 0:
                break 
            self.fila_emergencia_adulto.dequeue()
            self.num_atendidos += 1
            tam_emergencia -= 1
            contador -= 1

        while tam_mto_urgente > 0:
            if contador == 0:
                break 
            self.fila_mto_urgente_adulto.dequeue()
            self.num_atendidos += 1
            tam_mto_urgente -= 1
            contador -=1
            
        while tam_urgente > 0:
            if contador == 0:
                break 
            self.fila_urgente_adulto.dequeue()
            self.num_atendidos += 1
            tam_urgente -= 1
            contador -=1

        return True

# ===============================================================

    def enviarParaLeitos(self, neo = 0, ped = 0, adulto = 0): # envia todos os pacientes para os leitos disponíveis
        self.enviarParaLeitoNeonatal(neo)
        self.enviarParaLeitoPediatrico(ped)
        self.enviarParaLeitoAdulto(adulto)

        return self.num_atendidos

