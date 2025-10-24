#Cria função que diz todas as coordenadas da embarcação
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

#Armazena as coordenadas num dicionário
def preenche_frota(dicio, navio, linha, coluna, orientacao, tamanho):
    navio_cor = define_posicoes(linha, coluna, orientacao, tamanho)
    
    if navio not in dicio:
        dicio[navio] = []
    dicio[navio].append(navio_cor)

    return dicio

#Marca um X se a coordenada pertence a alguma embarcação
def faz_jogada (tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

#Preenche o grid com os navios do dicionário
def posiciona_frota(dicio):
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

#Mostra quantidade de embarcações afundadas
def afundados(dicio, tabuleiro):
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

#Verifica se a jogada é possível
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    verificador = 0
    quantia_coord = 0
    for cont in posicao:
        quantia_coord += 1

    for coordernadas in posicao:
        for posicoes in frota.values():
            for coord2 in posicoes:
                if coord2 == coordernadas:
                    verificador += 1

    if verificador == quantia_coord:
        return True
    else:
        return False
    
