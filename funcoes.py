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
