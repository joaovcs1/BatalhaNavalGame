def define_posicoes(linha, coluna, orientacao, tamanho):
    pos_inicial = [linha, coluna]
    opcoes = []

    if orientacao == 'vertical':
        for i in range(tamanho):
            opcoes.append([linha+i,coluna])
    elif orientacao == 'horizontal':
        for i in range(tamanho):
            opcoes.append([linha,coluna+i])

    return opcoes

def preenche_frota(dicio, navio, linha, coluna, orientacao, tamanho):
    navio_cor = define_posicoes(linha, coluna, orientacao, tamanho)
    
    if navio not in dicio:
        dicio[navio] = []
    dicio[navio].append(navio_cor)

    return dicio

def faz_jogada (tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota (dicio):
    tabuleiro = []
    for i in range(10):
        tabuleiro.append([0]* 10)
    for navios,posicoes in dicio.items():
        for posicao in posicoes:
            for cord in posicao:
                linha = cord[0]
                coluna = cord[1]
            
                tabuleiro[linha][coluna] = 1
    return tabuleiro

def afundados(dicio,tabuleiro):
    conta = 0
    for navios, posicoes in dicio.items():
        for posicao in posicoes:
            afundado = True
            for cord in posicao:
                linha = cord[0]
                coluna = cord[1]
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False      
            if afundado == True:
                conta += 1
    return conta
    