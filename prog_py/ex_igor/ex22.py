# VECTOR SIZE (SEM .APPEND() E CONCATENAÇÃO)

from random import randint

cont = 0
n = int(input())
veta, vetb, vetc = [randint(0, 9) for x in range(n)], [randint(0, 9) for x in range(n)], [randint(0, 9) for x in range(n)]
vetd = [0 for x in range(3*n)] # vetd = [0] * (3 * n)
while cont < (n):
    vetd[3 * cont] = veta[cont]
    vetd[3 * cont + 1] = vetb[cont]
    vetd[3 * cont + 2] = vetc[cont]
    cont += 1
print(veta)
print(vetb)
print(vetc)
print(vetd)
