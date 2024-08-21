def add(processo, rx, ry):
    # Soma o valor do registrador ry ao registrador rx e armazena o resultado em rx
    processo.registros[rx] += processo.registros[ry]
    # Define o zero_flag se o valor no registrador rx for zero
    processo.zero_flag = (processo.registros[rx] == 0)
    # Exibe a operação realizada e o valor resultante
    print(f"ADD R{rx}, R{ry} -> R{rx} = {processo.registros[rx]}")

def sub(processo, rx, ry):
    # Subtrai o valor do registrador ry do registrador rx e armazena o resultado em rx
    processo.registros[rx] -= processo.registros[ry]
    # Define o zero_flag se o valor no registrador rx for zero
    processo.zero_flag = (processo.registros[rx] == 0)
    # Exibe a operação realizada e o valor resultante
    print(f"SUB R{rx}, R{ry} -> R{rx} = {processo.registros[rx]}")

def mul(processo, rx, ry):
    # Multiplica o valor do registrador rx pelo valor de ry e armazena o resultado em rx
    processo.registros[rx] *= processo.registros[ry]
    # Define o zero_flag se o valor no registrador rx for zero
    processo.zero_flag = (processo.registros[rx] == 0)
    # Exibe a operação realizada e o valor resultante
    print(f"MUL R{rx}, R{ry} -> R{rx} = {processo.registros[rx]}")

def div(processo, rx, ry):
    # Realiza a divisão inteira de rx por ry, se ry não for zero
    if processo.registros[ry] != 0:
        processo.registros[rx] //= processo.registros[ry]
    else:
        # Levanta uma exceção se ry for zero
        raise ZeroDivisionError("Tentativa de divisão por zero!")
    # Define o zero_flag se o valor no registrador rx for zero
    processo.zero_flag = (processo.registros[rx] == 0)
    # Exibe a operação realizada e o valor resultante
    print(f"DIV R{rx}, R{ry} -> R{rx} = {processo.registros[rx]}")

def jmp(processo, address):
    # Modifica o contador de programa (PC) para o endereço especificado
    # Subtrai 1 pois o PC será incrementado após a instrução
    processo.pc = address - 1
    # Exibe o novo valor do PC
    print(f"JMP {address} -> PC = {processo.pc + 1}")

def jz(processo, address):
    # Se o zero_flag estiver setado, modifica o PC para o endereço especificado
    if processo.zero_flag:
        processo.pc = address - 1
    # Exibe o novo valor do PC e o estado do zero_flag
    print(f"JZ {address} -> PC = {processo.pc + 1} (Zero flag: {processo.zero_flag})")

def jnz(processo, address):
    # Se o zero_flag não estiver setado, modifica o PC para o endereço especificado
    if not processo.zero_flag:
        processo.pc = address - 1
    # Exibe o novo valor do PC e o estado do zero_flag
    print(f"JNZ {address} -> PC = {processo.pc + 1} (Zero flag: {not processo.zero_flag})")

def read(processo, rx):
    # Bloqueia o processo para simular uma operação de leitura
    processo.set_bloqueado()
    try:
        # Solicita ao usuário um valor de entrada para o registrador rx
        processo.registros[rx] = int(input(f"Processo {processo.pid} - Enter value for R{rx}: "))
    except ValueError:
        # Caso a entrada seja inválida, define 0 como valor padrão
        print("Entrada inválida, usando 0 como valor padrão.")
        processo.registros[rx] = 0
    # Exibe o valor lido para o registrador rx
    print(f"READ -> R{rx} = {processo.registros[rx]}")
    # Desbloqueia o processo após a leitura
    processo.set_pronto()

def write(processo, rx):
    # Exibe o valor contido no registrador rx
    print(f"Processo {processo.pid} - R{rx} = {processo.registros[rx]}")

def load(processo, rx, address):
    # Carrega o valor da memória no endereço especificado para o registrador rx
    processo.registros[rx] = processo.memoria_alocada[address]
    # Exibe a operação realizada e o valor carregado
    print(f"LOAD R{rx}, {address} -> R{rx} = {processo.registros[rx]}")

def store(processo, rx, address):
    # Armazena o valor do registrador rx na memória no endereço especificado
    processo.memoria_alocada[address] = processo.registros[rx]
    # Exibe a operação realizada e o valor armazenado
    print(f"STORE R{rx}, {address} -> MEM[{address}] = {processo.memoria_alocada[address]}")

def end(processo):
    # Finaliza o processo alterando seu estado para 'terminado'
    processo.set_terminado()
    # Exibe uma mensagem indicando que o processo foi finalizado
    print(f"Processo {processo.pid} foi finalizado por END")
