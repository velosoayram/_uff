# MARGARIDAS. 

def lotes(matriz, m, n): # complexidade O(M x N).

    lotes = []
    tam_linhas = len(matriz)
    tam_colunas = len(matriz[0])

    for l_atual in range(0, tam_linhas, m):

        for c_atual in range(0, tam_colunas, n):

            soma = 0

            for x in range(l_atual, l_atual + m):

                for y in range(c_atual, c_atual + n):
                    
                    soma += matriz[x][y]

            lotes.append(soma)

    return print(max(lotes))


l, c, m, n = map(int, input().split())
matriz = []

for linhas in range(l):
    matriz.append(list(map(int, input().split())))

lotes(matriz, m, n)
