# QUADRO DE MEDALHAS.

n = int(input())
paises = []

for pais in range(n):

    data = list(input().split())

    paises.append(data)

paises.sort(key=lambda pais: (-int(pais[1]), -int(pais[2]), -int(pais[3]), pais[0]))

for i in range(len(paises)):
    print(' '.join(paises[i]))
