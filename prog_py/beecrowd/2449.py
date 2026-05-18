# FECHADURA. / wrong answer 75% / refazer.

n, m = map(int, input().split())
lista = list(map(int, input().split()))
soma = 0
for x in range(n):
    if x == 0:
        dist = lista[x] - m
        soma += abs(dist)
    else:
        temp = dist
        if lista[x] > m and lista[x-1] > m:
            dist = max(lista[x], lista[x-1]) - m
            if temp != dist:
                val1 = min(dist, temp)
                val2 = max(dist, temp)
                soma += abs(val2) - abs(val1)
                continue
        elif lista[x] < m and lista[x-1] < m: 
            dist = min(lista[x], lista[x-1]) - m
            if temp != dist:
                val1 = min(dist, temp)
                val2 = max(dist, temp)
                soma += abs(val1) - abs(val2)
                continue
        else:
            dist = lista[x] - m
        if temp == dist:
            continue
        else:
            soma += abs(dist)
print(soma)

# FECHADURA 2.0

n, m = map(int, input().split())
lista = list(map(int, input().split()))
soma = 0
for i in range(n-1):
    dif = m - lista[i]
    soma += abs(dif)
    lista[i+1] += dif
print(soma)
