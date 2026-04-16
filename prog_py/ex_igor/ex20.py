# VECTOR B AND C.

from random import randint

listaA, listaB, somatorio = [], [], []
n = int(input())
for a in range(n):
    listaA += [randint(0, 9)]
for b in range(len(listaA)-1, -1, -1):
    listaB += [listaA[b]]
for c in listaB:
    temp = 0
    for d in range(c):
        temp += (d+1)
    somatorio += [temp]
print(f'lista A = {listaA}')
print(f'lista B = {listaB}')
print(f'somatorio = {somatorio}')
