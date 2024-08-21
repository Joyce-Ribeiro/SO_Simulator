class Escalonador:
    def __init__(self, quantum):
        # Inicializa o escalonador com o quantum (tempo máximo que cada processo pode executar)
        # e uma lista vazia para armazenar os processos.
        self.quantum = quantum
        self.processos = []

    def adicionar_processo(self, processo):
        # Adiciona um novo processo à lista de processos.
        self.processos.append(processo)

    def proximo_processo(self):
        # Retorna o próximo processo na fila.
        # Se não houver processos, retorna None.
        if not self.processos:
            return None
        
        # Remove o primeiro processo da fila (FIFO).
        processo = self.processos.pop(0)
        
        # Se o processo já estiver terminado, retorna None.
        if processo.estado == 'terminado':
            return None
        
        # Retorna o processo para ser executado.
        return processo

    def atualizar_fila(self):
        # Atualiza a fila de processos removendo aqueles que estão no estado 'terminado'.
        # Usa uma lista por compreensão para manter apenas os processos que não estão terminados.
        self.processos = [p for p in self.processos if p.estado != 'terminado']
