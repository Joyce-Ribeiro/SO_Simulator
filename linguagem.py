class LinguagemInstrucoes:
    def __init__(self):
        self.instrucoes = {}

    def adicionar_instrucao(self, nome, funcao):
        """Adiciona uma nova instrução à linguagem."""
        self.instrucoes[nome] = funcao

    def obter_instrucao(self, nome):
        """Obtém a função associada a uma instrução pelo seu nome."""
        return self.instrucoes.get(nome, None)

    def listar_instrucoes(self):
        """Lista todos os nomes das instruções disponíveis."""
        return list(self.instrucoes.keys())
