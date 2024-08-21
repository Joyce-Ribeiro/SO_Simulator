class Processo:
    def __init__(self, pid, memoria_alocada, instrucoes, linguagem):
        # Inicializa o processo com um PID, estado, contagem de programa, registradores, memória, instruções e linguagem de instruções.
        self.pid = pid  # ID do processo
        self.estado = 'pronto'  # Estado inicial do processo (pronto para ser executado)
        self.pc = 0  # Contador de programa (indica a posição atual da instrução a ser executada)
        self.registros = [0] * 8  # Inicializa 8 registradores com valor 0
        self.memoria_alocada = [0] * memoria_alocada  # Memória alocada para o processo
        self.instrucoes = instrucoes  # Lista de instruções do processo
        self.zero_flag = False  # Flag de condição zero
        self.linguagem = linguagem  # Referência à linguagem de instruções usada pelo processo

    def __repr__(self):
        # Retorna uma representação textual do processo, mostrando o PID, estado e contador de programa (PC).
        return f"<Processo PID={self.pid}, Estado={self.estado}, PC={self.pc}>"

    def set_pronto(self):
        # Define o estado do processo como 'pronto' se ele ainda não estiver terminado.
        if self.estado != 'terminado':
            self.estado = 'pronto'
            print(f"Processo {self.pid} está pronto para executar.")

    def set_executando(self):
        # Define o estado do processo como 'executando' se ele estiver pronto.
        if self.estado == 'pronto':
            self.estado = 'executando'
            print(f"Processo {self.pid} está em execução.")

    def set_bloqueado(self):
        # Define o estado do processo como 'bloqueado' se ele estiver em execução.
        if self.estado == 'executando':
            self.estado = 'bloqueado'
            print(f"Processo {self.pid} está bloqueado.")

    def set_terminado(self):
        # Define o estado do processo como 'terminado'.
        self.estado = 'terminado'
        print(f"Processo {self.pid} foi terminado.")

    def executar_instrucao(self):
        # Executa a próxima instrução se o processo estiver no estado 'executando'.
        if self.estado == 'executando':
            if self.pc < len(self.instrucoes):
                instrucao = self.instrucoes[self.pc]  # Obtém a próxima instrução
                print(f"Processo {self.pid} executando instrução: {instrucao}")
                self.interpretar(instrucao)  # Interpreta e executa a instrução
                self.pc += 1  # Incrementa o contador de programa
                if self.pc >= len(self.instrucoes):
                    self.set_terminado()  # Termina o processo se não houver mais instruções
            else:
                self.set_terminado()  # Termina o processo se todas as instruções já foram executadas
        elif self.estado == 'bloqueado':
            # Informa que o processo está bloqueado e não pode executar instruções
            print(f"Processo {self.pid} está bloqueado e não pode executar instruções.")
        else:
            # Informa que o processo não está em execução e não pode executar instruções
            print(f"Processo {self.pid} não está em execução e não pode executar instruções.")

    def interpretar(self, instrucao):
        # Interpreta e executa a instrução dada utilizando a linguagem de instruções do processo.
        parts = instrucao.split()  # Divide a instrução em partes (ex: ["ADD", "R1", "R2"])
        op = parts[0]  # Primeiro elemento é a operação (ex: "ADD")
        funcao = self.linguagem.obter_instrucao(op)  # Obtém a função correspondente à operação
        if funcao:
            # Executa a função da instrução com os operandos adequados
            funcao(self, *map(self._parse_operand, parts[1:]))
        else:
            # Informa que a instrução é desconhecida se a operação não for reconhecida
            print(f"Instrução desconhecida: {op}")

    def _parse_operand(self, operand):
        # Converte um operando da instrução em um valor apropriado (registrador ou valor literal).
        if operand.startswith('R'):
            # Se o operando for um registrador (ex: "R1"), retorna o número do registrador
            return int(operand[1])
        return int(operand)  # Caso contrário, retorna o valor numérico literal
