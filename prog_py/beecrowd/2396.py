# CORRIDA.

n, m = map(int, input().split())
tabela = [[i+1, 0] for i in range(n)]

for laps in range(n):

    tabela[laps][1] += sum((map(int, input().split())))

tabela.sort(key=lambda item: item[:][1])

print(f'{tabela[0][0]}\n{tabela[1][0]}\n{tabela[2][0]}')
