from funcoes import * 


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto


frota = {}

nomes = ["porta-aviões", "navio-tanque", "contratorpedeiro", "submarino"]
tamanhos = [4, 3, 2, 1]
quantidades = [1, 2, 3, 4]

for i in range(4):
    nome = nomes[i]
    tamanho = tamanhos[i]

    for j in range(quantidades[i]):
        valida = False

 
        while valida == False:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
    

            if nome == "submarino":
                orientacao = "vertical"

            else:
                orientacao = int(input("[1] Vertical [2] Horizontal >"))
                if orientacao == 1:
                    orientacao = "vertical"
                elif orientacao == 2:
                    orientacao = "horizontal"


            if posicao_valida(frota, linha, coluna, orientacao, tamanho) == True:
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                valida = True
            else:
                print("Esta posição não está válida!")




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

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

jogando = True
while jogando == True:
    texto = monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
    print(texto)

    repetido = True
    while repetido == True:
        linha = int(input("Jogador, quaç linha deseja atacar? "))
        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Jogador, qual linha deseja atacar? "))

        coluna = int(input("Jogador, qual coluna deseja atacar? "))
        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Jogador, qual coluna deseja atacar? "))


        if tabuleiro_oponente[linha][coluna] == "X" or tabuleiro_oponente[linha][coluna] == "-":
            print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        else:
            repetido = False


        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)
        if afundados(frota_oponente, tabuleiro_oponente) == 10:
            print("Parabéns! Você derrubou todos os navios do seu oponente!")
            jogando = False

    import random

    if jogando == True:
        repetido = True
        while repetido == True:
            linha_op = random.randint(0,9)
            coluna_op = random.randint(0,9)
            if tabuleiro_jogador[linha_op][coluna_op] != 'X' and tabuleiro_jogador[linha_op][coluna_op] != '-':
                repetido = False
        print(f'Seu oponente está atacando na linha {linha_op} e coluna {coluna_op}')
        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_op, coluna_op)
        if afundados(frota,tabuleiro_jogador) == 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False
        



