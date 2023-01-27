from cPacientes import Pacientes
from cLeitos import Leitos

class Simulador:
    def __init__(self):
        # cria os objetos leitos e pacientes
        self.leitos = Leitos()
        self.pacientes = Pacientes()

        # contadores
        self.num_leitos_total = 0
        self.num_leitos_disponiveis = 0
        self.num_pacientes_total = 0
        self.num_pacientes_atendidos = 0

    def geradorLeito(self, num): # gera a quantidade {num} de leitos
        self.leitos.gerarLeitos(num)

        self.num_leitos_total += num
        self.num_leitos_disponiveis += num

        return True

    def geradorFila(self, num): # gera a quantidade {num} de pacientes e adiciona a fila
        self.pacientes.gerarPacientes(num)

        self.num_pacientes_total += num

        return True

    def atenderPaciente(self): # atende todos os pacientes possíveis para a quantidade de leitos
        self.neo, self.ped, self.adulto = self.pacientes.mapaTotalAtual()
        neoL, pedL, adultoL = self.leitos.mapaLeitos()
    
        self.pacientes.enviarParaLeitos(neoL, pedL, adultoL)

        return True

    def ocuparLeito(self): # ocupa todos os leitos possíveis para a quantidade de pacientes
        self.leitos.ocuparLeitos(self.neo, self.ped, self.adulto)

        self.num_leitos_disponiveis = self.leitos.numLeitos()
        self.num_pacientes_atendidos = self.num_leitos_total - self.leitos.numLeitos()

        return True
    
    def mostrarMapaLeitos(self): # mostra mapa de leitos atuais
        neo, ped, adulto = self.leitos.mapaLeitos()
        
        return f'\n       \033[1;35mHospital de chegada dos leitos: \033[4m{self.leitos.mostrarHospital()}\n\n\033[1;32m\033[4mNúmero de leitos disponíveis:\033[00m\033[1m {self.leitos.numLeitos()}\n\033[00m \n\033[1;37mTotal:\033[00m          Neonatal: {neo} | Pediátrico: {ped } | Adulto: {adulto}\n'

    def mostrarMapaFilas(self): # mostra mapa de filas atuais
        neo_emergencia, ped_emergencia, adulto_emergencia = self.pacientes.mapaEmergencia()
        neo_mto_urg, ped_mto_urg, adulto_mto_urg = self.pacientes.mapaMtoUrgente()
        neo_urg, ped_urg, adulto_urg = self.pacientes.mapaUrgente()

        return f'\n\033[1;32m\033[4mNúmero de pessoas na fila:\033[00m\033[1m {self.pacientes.tamFila()}\033[00m\n \n\033[91m\033[1mEmergência:    \033[00m Neonatal: {neo_emergencia} | Pediátrico: {ped_emergencia} | Adulto: {adulto_emergencia}\n\033[38;5;214m\033[1mMuita urgência:\033[00m Neonatal: {neo_mto_urg} | Pediátrico: {ped_mto_urg} | Adulto: {adulto_mto_urg}\n\033[93m\033[1mUrgência:      \033[00m Neonatal: {neo_urg} | Pediátrico: {ped_urg} | Adulto: {adulto_urg}\n'

    def LeitosRestantes(self): # mostra mapa de leitos depois do atendimento 
        neo, ped, adulto = self.leitos.mapaLeitos()
        
        return f'\n\033[1;32m\033[4mLeitos restantes:\033[00m\033[1m {self.leitos.numLeitos()}\n\033[00m \n\033[1;37mTotal:\033[00m          Neonatal: {neo} | Pediátrico: {ped } | Adulto: {adulto}\n'

    def FilaRestante(self): # mostra mapa de filas depois do atendimento
        neo_emergencia, ped_emergencia, adulto_emergencia = self.pacientes.mapaEmergencia()
        neo_mto_urg, ped_mto_urg, adulto_mto_urg = self.pacientes.mapaMtoUrgente()
        neo_urg, ped_urg, adulto_urg = self.pacientes.mapaUrgente()

        return f'\n\033[1;32m\033[4mContinuam na fila:\033[00m\033[1m {self.pacientes.tamFila()}\033[00m\n \n\033[91m\033[1mEmergência:    \033[00m Neonatal: {neo_emergencia} | Pediátrico: {ped_emergencia} | Adulto: {adulto_emergencia}\n\033[38;5;214m\033[1mMuita urgência:\033[00m Neonatal: {neo_mto_urg} | Pediátrico: {ped_mto_urg} | Adulto: {adulto_mto_urg}\n\033[93m\033[1mUrgência:      \033[00m Neonatal: {neo_urg} | Pediátrico: {ped_urg} | Adulto: {adulto_urg}\n'

    def mostrarStatusGeral(self): # mostra as estatísticas dos contadores
        return f'\n\033[1;37m                 Total de leitos gerados:\033[1;36m {self.num_leitos_total} \n\n\033[1;37m                 Leitos disponíveis:\033[1;36m      {self.num_leitos_disponiveis} \n\n\033[1;37m                 Pacientes na fila:\033[1;36m       {self.pacientes.tamFila()}\n\n\033[1;37m                 Pacientes atendidos:\033[1;36m     {self.num_pacientes_atendidos}\033[00m\n'


        