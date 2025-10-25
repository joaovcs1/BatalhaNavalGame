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
    novas_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao_nova in novas_posicoes:
        linha = posicao_nova[0]
        coluna = posicao_nova[1]

        if not (0 <= linha <= 9 and 0 <= coluna <= 9):
            return False

        for lista_navios in frota.values():
            for navio in lista_navios:
                for posicao in navio:
                    if posicao_nova == posicao:
                        return False
    
    return True

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto