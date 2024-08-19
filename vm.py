class VirtualMachine:
    def __init__(self, gerenciador_processos):
        self.gerenciador_processos = gerenciador_processos

    def execute_process(self, pid):
        processo = self.gerenciador_processos.processos.get(pid)
        if processo:
            while any(p.estado != 'terminado' for p in self.gerenciador_processos.processos.values()):
                self.gerenciador_processos.executar_processos()
