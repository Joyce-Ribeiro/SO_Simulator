from linguagem import LinguagemInstrucoes
from gerenciador_processo import GerenciadorDeProcessos
from vm import VirtualMachine
from instrucoes import add, sub, mul, div, jmp, jz, jnz, read, write, load, store

# Criando e configurando a linguagem de instruções
linguagem = LinguagemInstrucoes()
linguagem.adicionar_instrucao('ADD', add)
linguagem.adicionar_instrucao('SUB', sub)
linguagem.adicionar_instrucao('MUL', mul)
linguagem.adicionar_instrucao('DIV', div)
linguagem.adicionar_instrucao('JMP', jmp)
linguagem.adicionar_instrucao('JZ', jz)
linguagem.adicionar_instrucao('JNZ', jnz)
linguagem.adicionar_instrucao('READ', read)
linguagem.adicionar_instrucao('WRITE', write)
linguagem.adicionar_instrucao('LOAD', load)
linguagem.adicionar_instrucao('STORE', store)

# Inicializando o gerenciador de processos e a máquina virtual
gerenciador_processos = GerenciadorDeProcessos()
vm = VirtualMachine(gerenciador_processos)

# Criando um processo com algumas instruções exemplo
instrucoes = [
    "LOAD R0, 0",  # Carrega valor da memória para o registrador R0
    "READ R1",     # Lê um valor para o registrador R1
    "ADD R0, R1",  # Adiciona R1 a R0
    "WRITE R0",    # Escreve valor de R0
    "JMP 1"        # Salta para a instrução 1
]
memoria_alocada = [10, 20, 30]

processo = gerenciador_processos.criar_processo(len(memoria_alocada), instrucoes, linguagem)

# Executando o processo
vm.execute_process(processo.pid)