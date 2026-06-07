# COFRINHO DA VÓ VITÓRIA.

n = int(input())
cont = 1
while n != 0:
    dif = 0
    print(f'Teste {cont}')
    for x in range(n):
        if x == 0:
            temp = 0
        j, z = map(int, (input().split()))
        dif = abs(j - z)
        if j > z:
            dif = dif
        elif j < z:
            dif = -dif
        print(dif + temp)
        if dif + temp != 0: temp = (dif + temp)
        else: temp = 0
    print()
    cont += 1
    n = int(input())
