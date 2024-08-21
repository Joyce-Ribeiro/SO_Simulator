class LinguagemInstrucoes:
    def __init__(self):
        # Inicializa o dicionário que armazenará as instruções da linguagem,
        # onde a chave é o nome da instrução e o valor é a função associada.
        self.instrucoes = {}

    def adicionar_instrucao(self, nome, funcao):
        # Armazena a função da instrução associada ao nome.
        self.instrucoes[nome] = funcao

    def obter_instrucao(self, nome):
        # Retorna a função da instrução correspondente ao nome fornecido, ou None se não existir.
        return self.instrucoes.get(nome, None)

    def listar_instrucoes(self):
        # Retorna uma lista de todos os nomes de instruções disponíveis.
        return list(self.instrucoes.keys())
