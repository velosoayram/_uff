# FILA DO RECREIO.

n = int(input())

for i in range(n):
    
    qtd_alunos = int(input())
    notas = list(map(int, input().split()))
    
    notas_corrigidas = sorted(notas, reverse=True)
    cont = len(notas)

    for j in range(len(notas)):
        if notas_corrigidas[j] != notas[j]: cont -= 1

    print(cont)
