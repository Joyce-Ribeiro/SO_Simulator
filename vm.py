class VirtualMachine:
    def __init__(self, escalonador):
        # Inicializa a máquina virtual com o escalonador de processos
        self.escalonador = escalonador

    def executar_processo(self, processo):
        # Executa o processo fornecido, alterando seu estado conforme necessário
        if processo.estado == 'pronto':
            processo.set_executando()  # Define o processo como em execução
        
        while processo.estado == 'executando':
            processo.executar_instrucao()  # Executa a instrução atual do processo
            if processo.estado == 'bloqueado':
                # Se o processo se torna bloqueado, adiciona-o novamente à fila de execução
                self.escalonador.adicionar_processo(processo)
                break  # Sai do loop para permitir que o próximo processo seja executado
        
        if processo.estado != 'terminado':
            # Se o processo ainda não terminou, re-adiciona-o à fila para execução futura
            self.escalonador.adicionar_processo(processo)

    def executar(self, gerenciador_processos):
        # Executa os processos até que todos estejam terminados
        while any(p.estado != 'terminado' for p in gerenciador_processos.processos.values()):
            self.escalonador.atualizar_fila()  # Atualiza a fila de processos, removendo os terminados
            processo = self.escalonador.proximo_processo()  # Obtém o próximo processo para execução
            if processo:
                self.executar_processo(processo)  # Executa o processo usando a função de execução de processos
