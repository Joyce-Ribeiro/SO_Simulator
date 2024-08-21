class Processo:
    def __init__(self, pid, memoria_alocada, instrucoes, linguagem):
        self.pid = pid
        self.estado = 'pronto'
        self.pc = 0
        self.registros = [0] * 8
        self.memoria_alocada = [0] * memoria_alocada
        self.instrucoes = instrucoes
        self.zero_flag = False
        self.linguagem = linguagem

    def __repr__(self):
        return f"<Processo PID={self.pid}, Estado={self.estado}, PC={self.pc}>"

    def set_pronto(self):
        if self.estado != 'terminado':
            self.estado = 'pronto'
            print(f"Processo {self.pid} está pronto para executar.")

    def set_executando(self):
        if self.estado == 'pronto':
            self.estado = 'executando'
            print(f"Processo {self.pid} está em execução.")

    def set_bloqueado(self):
        if self.estado == 'executando':
            self.estado = 'bloqueado'
            print(f"Processo {self.pid} está bloqueado.")

    def set_terminado(self):
        self.estado = 'terminado'
        print(f"Processo {self.pid} foi terminado.")

    def executar_instrucao(self):
        if self.estado == 'executando':
            if self.pc < len(self.instrucoes):
                instrucao = self.instrucoes[self.pc]
                print(f"Processo {self.pid} executando instrução: {instrucao}")
                self.interpretar(instrucao)
                self.pc += 1
                if self.pc >= len(self.instrucoes):
                    self.set_terminado()
            else:
                self.set_terminado()
        elif self.estado == 'bloqueado':
            print(f"Processo {self.pid} está bloqueado e não pode executar instruções.")
        else:
            print(f"Processo {self.pid} não está em execução e não pode executar instruções.")

    def interpretar(self, instrucao):
        parts = instrucao.split()
        op = parts[0]
        funcao = self.linguagem.obter_instrucao(op)
        if funcao:
            funcao(self, *map(self._parse_operand, parts[1:]))
        else:
            print(f"Instrução desconhecida: {op}")

    def _parse_operand(self, operand):
        if operand.startswith('R'):
            return int(operand[1])
        return int(operand)
