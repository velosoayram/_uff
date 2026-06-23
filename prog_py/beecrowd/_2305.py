# COLHEITA DE CAJU.

def colheita(matriz, m, n):

    tot_linhas = len(matriz)
    tot_colunas = len(matriz[0])

    # CRIAR SUMMED-AREA-TABLE.
    sat = [[0] * (tot_colunas + 1) for l in range(tot_linhas + 1)]

    # PREENCHER SUMMED-AREA-TABLE.
    for l in range(1, tot_linhas + 1):
        for c in range(1, tot_colunas + 1):

            valor = matriz[l - 1][c - 1]
            sat[l][c] = valor - sat[l - 1][c - 1] + sat[l - 1][c] + sat[l][c - 1]


    # BUSCA PELO MAIOR.
    maior_colheita = 0

    for l in range(0, tot_linhas - m + 1):
        for c in range(0, tot_colunas - n + 1):

            bloco = sat[l + m][c + n] - sat[l + m][c] - sat[l][c + n] + sat[l][c]

            if bloco > maior_colheita: maior_colheita = bloco

    return print(maior_colheita)

        
l, c, m, n = map(int, input().split())
matriz = []

for linhas in range(l):
    
    matriz.append(list(map(int, input().split())))

colheita(matriz, m, n)
