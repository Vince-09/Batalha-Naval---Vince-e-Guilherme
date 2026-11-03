from funcoes import * 

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

print(frota)
