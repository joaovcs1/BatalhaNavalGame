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
        print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}')
        continua = False
        while continua is False:
            insere_linha = int(input('Linha: '))
            insere_coluna = int(input('Coluna: '))
            
            orientacao = 'vertical'

            if navio =! 'submarino':
                orientacao = int(input('Orientação: digite 1 para vertical e 2 para horizontal '))
                if orientacao == 1:
                    orientacao = 'vertical'
                elif orientacao == 2:
                    orientacao = 'horizontal'
            
            if posicao_valida(insere_linha, insere_coluna, orientacao, tamanho):
                preenche_frota(frota,navio, insere_linha, insere_coluna, orientacao)
                continua = True
                
            else:
                print('Esta posição não está válida!')

print(frota)
            





