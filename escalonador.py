class Escalonador:
    def __init__(self, quantum):
        self.quantum = quantum
        self.processos = []

    def adicionar_processo(self, processo):
        self.processos.append(processo)

    def proximo_processo(self):
        if not self.processos:
            return None
        processo = self.processos.pop(0)
        if processo.estado == 'terminado':
            return None
        return processo

    def atualizar_fila(self):
        self.processos = [p for p in self.processos if p.estado != 'terminado']
