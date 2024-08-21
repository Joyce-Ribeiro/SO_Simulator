def add(processo, rx, ry):
    processo.registros[rx] += processo.registros[ry]
    processo.zero_flag = (processo.registros[rx] == 0)
    print(f"ADD R{rx}, R{ry} -> R{rx} = {processo.registros[rx]}")

def sub(processo, rx, ry):
    processo.registros[rx] -= processo.registros[ry]
    processo.zero_flag = (processo.registros[rx] == 0)
    print(f"SUB R{rx}, R{ry} -> R{rx} = {processo.registros[rx]}")

def mul(processo, rx, ry):
    processo.registros[rx] *= processo.registros[ry]
    processo.zero_flag = (processo.registros[rx] == 0)
    print(f"MUL R{rx}, R{ry} -> R{rx} = {processo.registros[rx]}")

def div(processo, rx, ry):
    if processo.registros[ry] != 0:
        processo.registros[rx] //= processo.registros[ry]
    else:
        raise ZeroDivisionError("Tentativa de divisão por zero!")
    processo.zero_flag = (processo.registros[rx] == 0)
    print(f"DIV R{rx}, R{ry} -> R{rx} = {processo.registros[rx]}")

def jmp(processo, address):
    processo.pc = address - 1  # Ajusta para o incremento no loop de execução
    print(f"JMP {address} -> PC = {processo.pc + 1}")

def jz(processo, address):
    if processo.zero_flag:
        processo.pc = address - 1
    print(f"JZ {address} -> PC = {processo.pc + 1} (Zero flag: {processo.zero_flag})")

def jnz(processo, address):
    if not processo.zero_flag:
        processo.pc = address - 1
    print(f"JNZ {address} -> PC = {processo.pc + 1} (Zero flag: {not processo.zero_flag})")

def read(processo, rx):
    processo.set_bloqueado()  
    processo.registros[rx] = int(input(f"Processo {processo.pid} - Enter value for R{rx}: "))
    print(f"READ -> R{rx} = {processo.registros[rx]}")
    

def write(processo, rx):
    print(f"Processo {processo.pid} - R{rx} = {processo.registros[rx]}")

def load(processo, rx, address):
    processo.registros[rx] = processo.memoria_alocada[address]
    print(f"LOAD R{rx}, {address} -> R{rx} = {processo.registros[rx]}")

def store(processo, rx, address):
    processo.memoria_alocada[address] = processo.registros[rx]
    print(f"STORE R{rx}, {address} -> MEM[{address}] = {processo.memoria_alocada[address]}")

def end(processo):
    processo.set_terminado()
    print(f"Processo {processo.pid} foi finalizado por END")