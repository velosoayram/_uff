'''
f) Escreva um programa que imprime na tela os n primeiros números perfeitos. Um número
perfeito é aquele que é igual à soma dos seus divisores (tirando ele mesmo). Por exemplo, 6 = 1
+ 2 + 3 é perfeito.
'''

cont = 1
n = int(input())
while cont <= n:
    soma = 0
    for x in range(1, cont):
        if cont % x == 0:
            soma += x
    if soma == cont:
        print(f'{cont} é perfeito.')
    cont += 1