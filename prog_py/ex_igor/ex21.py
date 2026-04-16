# VECTOR SIZE.

from random import randint

vtA, vtB, vtC, vtD = [], [], [], []
n = int(input())
for x in range(n):
    vtA += [randint(0, 9)]
    vtB += [randint(0, 9)]
    vtC += [randint(0, 9)]
for y in range(n):
    vtD += [vtA[y]]
    vtD += [vtB[y]]
    vtD += [vtC[y]]
print(vtA)
print(vtB)
print(vtC)
print(vtD)

