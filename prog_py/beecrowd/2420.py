# GUERRA POR TERRITÓRIO.

n = int(input())
lista = list(map(int, input().split()))
total, soma, cont = sum(lista), 0, 0
for x in lista:
    total -= x
    soma += x
    cont += 1
    if total == soma:
        print(cont)
        break