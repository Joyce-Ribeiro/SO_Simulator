import sys
from gerenciador_processo import GerenciadorDeProcessos
from escalonador import Escalonador
from linguagem import LinguagemInstrucoes
from vm import VirtualMachine
from instrucoes import add, sub, mul, div, jmp, jz, jnz, read, write, load, store, end

linguagem = LinguagemInstrucoes()
linguagem.adicionar_instrucao('ADD', add)  # Adiciona a instrução de soma
linguagem.adicionar_instrucao('SUB', sub)  # Adiciona a instrução de subtração
linguagem.adicionar_instrucao('MUL', mul)  # Adiciona a instrução de multiplicação
linguagem.adicionar_instrucao('DIV', div)  # Adiciona a instrução de divisão
linguagem.adicionar_instrucao('JMP', jmp)  # Adiciona a instrução de salto (jump)
linguagem.adicionar_instrucao('JZ', jz)    # Adiciona a instrução de salto condicional (zero flag)
linguagem.adicionar_instrucao('JNZ', jnz)  # Adiciona a instrução de salto condicional (não zero flag)
linguagem.adicionar_instrucao('READ', read)  # Adiciona a instrução de leitura de entrada do usuário
linguagem.adicionar_instrucao('WRITE', write)  # Adiciona a instrução de escrita (exibe valor)
linguagem.adicionar_instrucao('LOAD', load)  # Adiciona a instrução de carregar valor da memória para registrador
linguagem.adicionar_instrucao('STORE', store)  # Adiciona a instrução de armazenar valor do registrador na memória
linguagem.adicionar_instrucao('END', end) # Adiciona a instrução de finalização de processo

class CLI:
    def __init__(self):
        # Inicializa o gerenciador de processos, o escalonador e a máquina virtual.
        self.gerenciador = GerenciadorDeProcessos()
        self.escalonador = Escalonador(quantum=5)  # Define o quantum para o escalonador
        self.vm = VirtualMachine(self.escalonador)
    
    def start(self):
        # Exibe uma mensagem de boas-vindas e inicia o loop da CLI
        print("Bem-vindo à CLI do sistema de simulação de SO.")
        print("Digite 'ajuda' para ver os comandos disponíveis.")
        
        while True:
            comando = input("> ").strip().split()

            if not comando:
                continue

            comando_principal = comando[0]

            if comando_principal == "ajuda":
                self.mostrar_ajuda()
            elif comando_principal == "criar_processo":
                self.criar_processo()
            elif comando_principal == "executar":
                self.executar_processos()
            elif comando_principal == "listar_processos":
                self.listar_processos()
            elif comando_principal == "finalizar_processo":
                if len(comando) > 1:
                    self.finalizar_processo(int(comando[1]))
                else:
                    print("Uso correto: finalizar_processo <pid>")
            elif comando_principal == "status_vm":
                self.status_vm()
            elif comando_principal == "sair":
                print("Saindo da CLI...")
                sys.exit(0)
            else:
                print(f"Comando desconhecido: {comando_principal}")
    
    def mostrar_ajuda(self):
        # Exibe uma lista de comandos disponíveis.
        print("""
Comandos disponíveis:
- criar_processo: Cria um novo processo.
- executar: Executa os processos na VM.
- listar_processos: Lista todos os processos na VM.
- finalizar_processo <pid>: Finaliza um processo específico.
- status_vm: Exibe o status atual da VM (Monitorar Recursos).
- sair: Finaliza a CLI.
        """)
    
    def criar_processo(self):
        # Solicita ao usuário informações para criar um novo processo.
        try:
            memoria = list(map(int, input("Memória alocada para o processo: ").split(", ")))
            instrucoes = []
            while True:
                comando = input("Digite um comando (ou 'END' para terminar): ")
    
                # Verifica se o usuário digitou "END"
                if comando.strip().upper() == "END":
                    instrucoes.append('END')
                    break  # Encerra o loop se o comando for "END"
    
                # Adiciona o comando à lista, removendo possíveis aspas
                instrucoes.append(comando.strip('"'))
            print(instrucoes)
            # Para simplificar, a linguagem seria uma referência para um conjunto de instruções que já criamos
            
            processo = self.gerenciador.criar_processo(memoria, instrucoes, linguagem)
            self.escalonador.adicionar_processo(processo)
        except ValueError:
            print("Erro: valor de memória inválido.")
    
    def executar_processos(self):
        # Executa os processos na máquina virtual.
        self.vm.executar(self.gerenciador)
    
    def listar_processos(self):
        # Lista todos os processos com seus PIDs e estados.
        for pid, processo in self.gerenciador.processos.items():
            print(f"PID: {pid}, Estado: {processo.estado}, PC: {processo.pc}")
    
    def finalizar_processo(self, pid):
        # Finaliza o processo com o PID especificado.
        self.gerenciador.finalizar_processo(pid)
    
    def status_vm(self):
        # Exibe o uso de recursos da VM (pode ser expandido conforme necessário).
        total_processos = len(self.gerenciador.processos)
        print(f"Total de processos ativos: {total_processos}")
        for pid, processo in self.gerenciador.processos.items():
            print(f"PID: {pid}, Estado: {processo.estado}, Registradores: {processo.registros}, Memória: {processo.memoria_alocada}")
    


# Inicializando a CLI
if __name__ == "__main__":
    cli = CLI()
    cli.start()
