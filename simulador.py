class Simulador:
    def __init__(self, gerenciador_processos, escalonador, vm):
        self.gerenciador_processos = gerenciador_processos
        self.escalonador = escalonador
        self.vm = vm
    
    def mostrar_estado_processos(self):
        print("\nEstado Atual dos Processos:")
        for processo in self.gerenciador_processos.processos.values():
            print(processo)
    
    def mostrar_fila_processos(self):
        print("\nFila de Processos:")
        for processo in self.escalonador.processos:
            print(processo)
    
    def mostrar_instrucao(self, processo):
        print(f"\nInstruções do Processo {processo.pid}:")
        for i, instrucao in enumerate(processo.instrucoes):
            print(f"{i}: {instrucao}")
    
    def iniciar_execucao(self):
        while any(p.estado != 'terminado' for p in self.gerenciador_processos.processos.values()):
            self.escalonador.atualizar_fila()  # Atualiza a fila de processos
            processo = self.escalonador.proximo_processo()
            if processo:
                self.vm.executar_processo(processo)
                if processo.estado != 'terminado':
                    self.escalonador.adicionar_processo(processo)  # Re-adiciona o processo se não terminado
    
    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Mostrar Estado dos Processos")
            print("2. Mostrar Fila de Processos")
            print("3. Mostrar Instruções de um Processo")
            print("4. Iniciar Execução dos Processos")
            print("5. Sair")
            
            escolha = input("Escolha uma opção: ")
            
            if escolha == '1':
                self.mostrar_estado_processos()
            elif escolha == '2':
                self.mostrar_fila_processos()
            elif escolha == '3':
                pid = int(input("Digite o PID do processo: "))
                processo = self.gerenciador_processos.processos.get(pid)
                if processo:
                    self.mostrar_instrucao(processo)
                else:
                    print(f"Processo com PID {pid} não encontrado.")
            elif escolha == '4':
                self.iniciar_execucao()
                print("Execução concluída.")
            elif escolha == '5':
                break
            else:
                print("Opção inválida. Tente novamente.")
