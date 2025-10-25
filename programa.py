from funcoes import *

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}     

#Quantidade e tamanho, respectivamente
definicao_frota = {
    "porta-aviões":[1,4],
    "navio-tanque":[2,3],
    "contratorpedeiro":[3,2],
    "submarino": [4,1],
}

for navio, definicao in definicao_frota.items():
    quantidade = definicao[0]
    tamanho = definicao[1]

    for i in range(quantidade):
        
        continua = False
        while continua is False:
            print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}')
            insere_linha = int(input('Linha: '))
            insere_coluna = int(input('Coluna: '))
            
            orientacao = 'vertical'

            if navio != 'submarino':
                orientacao = int(input('Orientação: digite 1 para vertical e 2 para horizontal '))
                if orientacao == 1:
                    orientacao = 'vertical'
                elif orientacao == 2:
                    orientacao = 'horizontal'
            
            if posicao_valida(frota,insere_linha, insere_coluna, orientacao, tamanho):
                preenche_frota(frota,navio, insere_linha, insere_coluna, orientacao, tamanho)
                continua = True
                
            else:
                print('Esta posição não está válida!')

            
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)

total_navios_oponente = 0
for lista_navios in frota_oponente.values():
    total_navios_oponente += len(lista_navios)

jogando = True
posicoes_atacadas = [] 

while jogando:
    
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    linha_valida = False
    while not linha_valida:
        linha_ataque = int(input('Linha de ataque: '))
        if 0 <= linha_ataque <= 9:
            linha_valida = True
        else:
            print('Linha inválida!')

    coluna_valida = False
    while not coluna_valida:
        coluna_ataque = int(input('Coluna de ataque: '))
        if 0 <= coluna_ataque <= 9:
            coluna_valida = True
        else:
            print('Coluna inválida!')
            
    coordenada_ataque = [linha_ataque, coluna_ataque]
    
    if coordenada_ataque in posicoes_atacadas:
        print(f'A posição linha {linha_ataque} e coluna {coluna_ataque} já foi informada anteriormente!')
        continue
    
    posicoes_atacadas.append(coordenada_ataque)
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_ataque, coluna_ataque)

    navios_afundados_oponente = afundados(frota_oponente, tabuleiro_oponente)
    
    if navios_afundados_oponente == total_navios_oponente:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False 