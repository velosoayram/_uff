# IDENTIFICANDO O CHÁ.

soma = 0
t = int(input())
a, b, c, d, e = map(int, input().split())
for n in [a, b, c, d, e]:
    if n == t:
        soma += 1
print(soma)
