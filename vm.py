class VirtualMachine:
    def __init__(self, escalonador):
        self.escalonador = escalonador

    def executar_processo(self, processo):
        if processo.estado == 'pronto':
            processo.set_executando()
        while processo.estado == 'executando':
            processo.executar_instrucao()
            if processo.estado == 'bloqueado':
                # Coloca o processo no final da fila de execução
                self.escalonador.adicionar_processo(processo)
                break  # Sai do loop para permitir que o próximo processo seja executado
        if processo.estado != 'terminado':
            # Se o processo não foi terminado, ele deve ser re-adicionado à fila
            self.escalonador.adicionar_processo(processo)

    def executar(self, gerenciador_processos):
        while any(p.estado != 'terminado' for p in gerenciador_processos.processos.values()):
            self.escalonador.atualizar_fila()
            processo = self.escalonador.proximo_processo()
            if processo:
                self.executar_processo(processo)
