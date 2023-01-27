from cSimulador import Simulador
import random
import time

if __name__ == '__main__':

    simulador = Simulador()
    while(True):

        simulador.geradorFila(random.randint(0,50)) # até 50 pessoas podem entrar na fila por ciclo
        simulador.geradorLeito(random.randint(0,25)) # até 25 leitos podem chegar por ciclo

        print(simulador.mostrarMapaLeitos())
        print(simulador.mostrarMapaFilas())

        simulador.atenderPaciente()
        simulador.ocuparLeito()

        print("===========================================================")

        time.sleep(5)
        
        print(simulador.LeitosRestantes())
        print(simulador.FilaRestante())

        time.sleep(5)

        print("               ...............................")
        print(simulador.mostrarStatusGeral())
        print("               ...............................")

        time.sleep(3)

    
    
