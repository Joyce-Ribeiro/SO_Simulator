from linguagem import LinguagemInstrucoes
from gerenciador_processo import GerenciadorDeProcessos
from escalonador import Escalonador
from vm import VirtualMachine
from simulador import Simulador
from instrucoes import add, sub, mul, div, jmp, jz, jnz, read, write, load, store, end

# Inicializando a linguagem e registrando as instruções disponíveis
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
linguagem.adicionar_instrucao('END', end)    # Adiciona a instrução de finalização de processo

# Inicializando o gerenciador de processos, escalonador e máquina virtual
gerenciador_processos = GerenciadorDeProcessos()

# Definindo o quantum do escalonador (tempo de execução de cada processo antes de ser interrompido)
quantum = 2
escalonador = Escalonador(quantum)

# Inicializando a máquina virtual com o escalonador
vm = VirtualMachine(escalonador)

# Definindo a lista de instruções e memória para o primeiro processo
instrucoes1 = [
    "LOAD R0, 0",   # Carrega o valor da memória no endereço 0 para o registrador R0
    "READ R1",      # Solicita um valor de entrada e armazena no registrador R1
    "ADD R0, R1",   # Soma os valores de R0 e R1, armazenando o resultado em R0
    "WRITE R0",     # Exibe o valor armazenado no registrador R0
    "END"           # Finaliza o processo
]

# Definindo a lista de instruções e memória para o segundo processo
instrucoes2 = [
    "READ R2",      # Solicita um valor de entrada e armazena no registrador R2
    "MUL R2, R2",   # Multiplica R2 por ele mesmo, armazenando o resultado em R2
    "WRITE R2",     # Exibe o valor armazenado no registrador R2
    "END"           # Finaliza o processo
]

# Definindo a memória alocada para cada processo
memoria_alocada1 = [10, 20, 30]  # Memória alocada para o primeiro processo
memoria_alocada2 = [5, 10, 15]   # Memória alocada para o segundo processo

# Criando o primeiro processo com suas instruções e memória
processo1 = gerenciador_processos.criar_processo(len(memoria_alocada1), instrucoes1, linguagem)

# Criando o segundo processo com suas instruções e memória
processo2 = gerenciador_processos.criar_processo(len(memoria_alocada2), instrucoes2, linguagem)

# Adicionando os processos ao escalonador
escalonador.adicionar_processo(processo1)
escalonador.adicionar_processo(processo2)

# Inicializando o simulador com o gerenciador de processos, escalonador e a máquina virtual
simulador = Simulador(gerenciador_processos, escalonador, vm)

# Executando o menu do simulador (provavelmente apresenta opções ao usuário)
simulador.menu()

# Executando os processos na máquina virtual usando o gerenciador de processos
vm.executar(gerenciador_processos)

# Finalizando a simulação
