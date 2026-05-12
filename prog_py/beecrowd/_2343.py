# CAÇADORES DE MITOS.

n = int(input())

locais = []

for _ in range(n):
    x, y = map(int, input().split())
    
    if [x, y] in locais:
        print(1)
        break

    locais += [x, y]

else:
    print(0)
