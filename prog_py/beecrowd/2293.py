# CAMPO DE MINHOCAS.

l, c = map(int, input().split())
matriz, linhas, colunas = [], [], []
for a in range(l):
    linha = list(map(int, input().split()))
    linhas.append(sum(linha))
    matriz.append(linha)
campo1 = max(linhas)
for a in range(l):
    if a == 0:
        for b in matriz[a]:
            colunas.append(b)
    else:
        for c in range(len(matriz[a])):
            colunas[c] += matriz[a][c]
campo2 = max(colunas)
print(max(campo1, campo2))
