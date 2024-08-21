class Simulador:
    def __init__(self, gerenciador_processos, escalonador, vm):
        # Inicializa o simulador com o gerenciador de processos, escalonador e máquina virtual (VM)
        self.gerenciador_processos = gerenciador_processos  # Gerenciador de processos
        self.escalonador = escalonador  # Escalonador de processos
        self.vm = vm  # Máquina virtual que executa os processos

    def mostrar_estado_processos(self):
        # Exibe o estado atual de todos os processos no sistema
        print("\nEstado Atual dos Processos:")
        for processo in self.gerenciador_processos.processos.values():
            print(processo)  # Exibe a representação textual de cada processo

    def mostrar_fila_processos(self):
        # Exibe a fila atual de processos no escalonador
        print("\nFila de Processos:")
        for processo in self.escalonador.processos:
            print(processo)  # Exibe a representação textual de cada processo na fila

    def mostrar_instrucao(self, processo):
        # Exibe as instruções de um processo específico
        print(f"\nInstruções do Processo {processo.pid}:")
        for i, instrucao in enumerate(processo.instrucoes):
            # Exibe cada instrução do processo com seu índice
            print(f"{i}: {instrucao}")

    def iniciar_execucao(self):
        # Inicia a execução dos processos até que todos os processos tenham terminado
        while any(p.estado != 'terminado' for p in self.gerenciador_processos.processos.values()):
            # Continua enquanto houver processos que não tenham terminado
            self.escalonador.atualizar_fila()  # Atualiza a fila de processos, removendo os terminados
            processo = self.escalonador.proximo_processo()  # Obtém o próximo processo a ser executado
            if processo:
                self.vm.executar_processo(processo)  # Executa o processo na máquina virtual (VM)
                if processo.estado != 'terminado':
                    # Se o processo não terminou, re-adiciona-o na fila do escalonador
                    self.escalonador.adicionar_processo(processo)

    def menu(self):
        # Exibe um menu interativo para o usuário com várias opções de simulação
        while True:
            print("\nMenu:")
            print("1. Mostrar Estado dos Processos")
            print("2. Mostrar Fila de Processos")
            print("3. Mostrar Instruções de um Processo")
            print("4. Iniciar Execução dos Processos")
            print("5. Sair")

            # Solicita ao usuário que escolha uma opção do menu
            escolha = input("Escolha uma opção: ")
            
            if escolha == '1':
                # Exibe o estado atual dos processos
                self.mostrar_estado_processos()
            elif escolha == '2':
                # Exibe a fila de processos no escalonador
                self.mostrar_fila_processos()
            elif escolha == '3':
                # Solicita o PID de um processo para exibir suas instruções
                pid = int(input("Digite o PID do processo: "))
                processo = self.gerenciador_processos.processos.get(pid)
                if processo:
                    # Exibe as instruções do processo correspondente
                    self.mostrar_instrucao(processo)
                else:
                    # Informa se o processo não foi encontrado
                    print(f"Processo com PID {pid} não encontrado.")
            elif escolha == '4':
                # Inicia a execução de todos os processos
                self.iniciar_execucao()
                print("Execução concluída.")
            elif escolha == '5':
                # Encerra o simulador
                break
            else:
                # Informa que a opção escolhida é inválida
                print("Opção inválida. Tente novamente.")
