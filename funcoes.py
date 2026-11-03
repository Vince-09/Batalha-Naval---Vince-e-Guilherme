def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    for i in range(tamanho):
        if orientacao == 'vertical':
            posicoes.append([linha + i,coluna])
        else:
            posicoes.append([linha,coluna + i])
    return posicoes


def preenche_frota(frota, nome_do_navio, linha, coluna, orientacao, tamanho):

    navio = define_posicoes(linha,coluna,orientacao,tamanho)

    if nome_do_navio not in frota:
        frota[nome_do_navio] = []
    frota[nome_do_navio].append(navio)

    return frota


def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = "-"

    return tabuleiro


def posiciona_frota(frota):
    tabuleiro = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    for nome in frota:
        for navio in frota[nome]:
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1

    return tabuleiro

def afundados(frota,tabuleiro):
    navios_afundados = 0
    for i in frota:
        for navio in frota[i]:
            acertos = 0
            for posicao in navio:
                if tabuleiro[posicao[0]][posicao[1]] == 'X':
                    acertos += 1
            if acertos == len(navio):
                navios_afundados += 1
    return navios_afundados

def posicao_valida(frota,linha,coluna,orientacao,tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for i in posicoes:
        linha_ = i[0]
        coluna_ = i[1]
        if linha_<0 or linha_>9 or coluna_<0 or coluna_>9:
            return False
        for nome in frota:
            for navio in frota[nome]:
                if i in navio:
                    return False
 
    return True