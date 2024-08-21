from processo import Processo

class GerenciadorDeProcessos:
    def __init__(self):
        # Dicionário para armazenar processos, onde a chave é o PID e o valor é o objeto Processo
        self.processos = {}
        # Contador para gerar novos PIDs de forma incremental
        self.pid_counter = 1
    
    def criar_processo(self, memoria_alocada, instrucoes, linguagem):
        # Cria um novo processo com um PID único, memória alocada, instruções e linguagem
        pid = self.pid_counter
        processo = Processo(pid, memoria_alocada, instrucoes, linguagem)
        # Armazena o processo no dicionário usando o PID como chave
        self.processos[pid] = processo
        # Incrementa o contador de PID para garantir PIDs únicos para futuros processos
        self.pid_counter += 1
        print(f"Processo {pid} criado e está pronto.")
        # Retorna o processo recém-criado
        return processo
    
    def finalizar_processo(self, pid):
        # Finaliza o processo com o PID fornecido, se ele existir
        if pid in self.processos:
            # Define o estado do processo como 'terminado'
            self.processos[pid].set_terminado()
            # Remove o processo do dicionário
            del self.processos[pid]
        else:
            print(f"Processo {pid} não encontrado.")
    
    def obter_estado(self, pid):
        # Retorna o estado do processo com o PID fornecido, se ele existir
        if pid in self.processos:
            return self.processos[pid].estado
        else:
            return "Processo não encontrado"
    
    def executar_processos(self):
        # Itera sobre todos os processos no dicionário de processos
        for pid, processo in list(self.processos.items()):
            # Verifica se o processo está pronto para ser executado
            if processo.estado == 'pronto':
                processo.set_executando()  # Coloca o processo em estado de execução
            
            # Se o processo estiver em execução, executa a próxima instrução
            if processo.estado == 'executando':
                processo.executar_instrucao()
            
            # Se o processo estiver terminado após a execução, finaliza-o
            if processo.estado == 'terminado':
                self.finalizar_processo(pid)
            
            # Se o processo estiver bloqueado, tenta desbloqueá-lo
            if processo.estado == 'bloqueado':
                self.desbloquear_processo(pid)
    
    def desbloquear_processo(self, pid):
        # Desbloqueia o processo com o PID fornecido, se ele estiver bloqueado
        if pid in self.processos and self.processos[pid].estado == 'bloqueado':
            # Altera o estado do processo para 'pronto'
            self.processos[pid].set_pronto()
        else:
            print(f"Processo {pid} não encontrado ou não está bloqueado.")
