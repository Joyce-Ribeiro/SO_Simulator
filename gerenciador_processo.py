from processo import Processo

class GerenciadorDeProcessos:
    def __init__(self):
        self.processos = {}  # Dicionário para armazenar processos
        self.pid_counter = 1
    
    def criar_processo(self, memoria_alocada, instrucoes, linguagem):
        pid = self.pid_counter
        processo = Processo(pid, memoria_alocada, instrucoes, linguagem)
        self.processos[pid] = processo
        self.pid_counter += 1
        print(f"Processo {pid} criado e está pronto.")
        return processo
    
    def finalizar_processo(self, pid):
        if pid in self.processos:
            self.processos[pid].set_terminado()
            del self.processos[pid]
        else:
            print(f"Processo {pid} não encontrado.")
    
    def obter_estado(self, pid):
        if pid in self.processos:
            return self.processos[pid].estado
        else:
            return "Processo não encontrado"
    
    def executar_processos(self):
        for pid, processo in list(self.processos.items()):
            if processo.estado == 'pronto':
                processo.set_executando()
            if processo.estado == 'executando':
                processo.executar_instrucao()
            if processo.estado == 'terminado':
                self.finalizar_processo(pid)
            if processo.estado == 'bloqueado':
                self.desbloquear_processo(pid)
    
    def desbloquear_processo(self, pid):
        if pid in self.processos and self.processos[pid].estado == 'bloqueado':
            self.processos[pid].set_pronto()
        else:
            print(f"Processo {pid} não encontrado ou não está bloqueado.")
