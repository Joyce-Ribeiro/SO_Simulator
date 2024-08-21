class VirtualMachine:
    def __init__(self, escalonador):
        self.escalonador = escalonador

    def executar_processo(self, processo):
        if processo.estado == 'pronto':
            processo.set_executando()
        while processo.estado == 'executando':
            processo.executar_instrucao()
        processo.set_terminado()

    def executar(self, gerenciador_processos):
        while any(p.estado != 'terminado' for p in gerenciador_processos.processos.values()):
            self.escalonador.atualizar_fila()
            processo = self.escalonador.proximo_processo()
            if processo:
                self.executar_processo(processo)
                if processo.estado != 'terminado':
                    self.escalonador.adicionar_processo(processo)
