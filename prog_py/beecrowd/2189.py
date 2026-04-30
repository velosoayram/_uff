# QUERMESSE.

n, r, cont = int(input()), 1, 1
while n != 0:
    ingressos = input().split()
    print(f'Teste {cont}')
    for x in ingressos:
        if int(x) == ((ingressos.index(x)) + 1):
            r = int(x)
            break
    print(r)
    print()
    cont += 1
    n = int(input())
