
linguagem

instrucoes = [
    'START_H',   #inicia programa
    'START_G',   #inicia o jogo
    'ADD_W',     #salva palavra para o jogo
    'DEL_W',     #tira palavra do jogo
    'LIST_W'     #lista palavras
    'RAND_W',    #seta palavra aleatória
    'GUESS',     #chute
    'ITJUMP',    #JUMP se verdade
    'IFJUMP',    #jump se falso
    'END_G',     #finaliza jogo
    'ADD',       #adiciona dois valores
    'COMP',      #compara dois valores
    'WIN',       #GANHA
    'JUMP',      #JUMP
    'END'        #finaliza programa
]

processo_1=[
    'START_H',
    'ADD_W R1',
    'LIST_W',
    'RAND_W R2',
    'START_G',
    'GUESS R3',
    'ITJUMP 6, COMP R2, R3',
    'IFJUMP 10',
    'WIN',
    'END'
]