from linguagem import LinguagemInstrucoes
from gerenciador_processo import GerenciadorDeProcessos
from escalonador import Escalonador
from vm import VirtualMachine
from simulador import Simulador
from instrucoes import add, sub, mul, div, jmp, jz, jnz, read, write, load, store, end

# Inicializando a linguagem e o gerenciador
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
linguagem.adicionar_instrucao('END', end)

gerenciador_processos = GerenciadorDeProcessos()
quantum = 2
escalonador = Escalonador(quantum)
vm = VirtualMachine(escalonador)

instrucoes1 = [
    "LOAD R0, 0",
    "READ R1",
    "ADD R0, R1",
    "WRITE R0",
    "END"
]

instrucoes2 = [
    "READ R2",
    "MUL R2, R2",
    "WRITE R2",
    "END"
]

memoria_alocada1 = [10, 20, 30]
memoria_alocada2 = [5, 10, 15]

processo1 = gerenciador_processos.criar_processo(len(memoria_alocada1), instrucoes1, linguagem)
processo2 = gerenciador_processos.criar_processo(len(memoria_alocada2), instrucoes2, linguagem)

escalonador.adicionar_processo(processo1)
escalonador.adicionar_processo(processo2)

simulador = Simulador(gerenciador_processos, escalonador, vm)
simulador.menu()
vm.executar(gerenciador_processos)
# Inicializando o simulador
