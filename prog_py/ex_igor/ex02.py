# IDENTIFICADOR DE NÚMEROS PRIMOS.

n = int(input())
qtd_divisores = 0
for nums in range(n):
    if n % (nums+1) == 0:
        qtd_divisores += 1
if qtd_divisores < 2:
    print(f'{n} NÃO É PRIMO')
elif qtd_divisores > 2:
    print(f'{n} NÃO É PRIMO')
else:
    print(f'{n} É PRIMO')
