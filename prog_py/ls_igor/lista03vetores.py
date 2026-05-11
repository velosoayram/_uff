'''
1) Faça um programa em Python que receba um conjunto de 100 elementos numéricos e os armazene em uma lista. Em seguida, o programa deverá procurar se existem no vetor elementos iguais a um dado valor também informado pelo usuário e imprimir o índice das posições em que estes são encontrados.
'''

from random import randint

n = int(input())
vetor, pos = [randint(0, 100) for _ in range(100)], []
for i in range(len(vetor)):
    if vetor[i] == n:
        pos.append(i)
if len(pos) > 1:
    print(f'{n}, POSIÇÃO: {pos}')
elif len(pos) == 1:
    print(f'Só há um elemento {n} no vetor.')
else:
    print(f'{n} não está no vetor.')

'''
2) Uma locadora de videogame tem guardada, em uma lista de 500 posições, a quantidade de jogos retirados por seus clientes durante o ano passado (i.e. Clientes[i] = X -> o cliente “i” retirou X jogos no ano passado). Agora esta locadora está fazendo uma promoção e, para cada 10 jogos retirados no ano passado, o cliente tem direito a uma locação grátis. Faça um programa que crie um outro vetor contendo a quantidade de locações gratuitas a que cada cliente tem direito.
'''

from random import randint

clientes = [randint(0, 50) for _ in range(500)]
locacoes = [(a // 10) for a in clientes]
for x in range(len(clientes)):
    print(f'Cliente {x+1} com direito a {locacoes[x]} locações gratuitas.')

'''
3) Faça um programa que receba uma lista A de dimensão N e:

(a) Inverta os valores de A, troque o primeiro pelo ultimo, o segundo pelo penúltimo e assim por diante.

(b) Após este procedimento, criar um vetor B de dimensão N com o fatorial de cada valor de A, respeitando as posições, caso o valor for positivo ou nulo. Deixe os valores negativos intactos.

(c) Imprima o vetor B.
'''

from random import randint

n, c1, c2 = int(input()), 0, -1
la, lb = [randint(-10, 15) for _ in range(n)], []

# for x in range(n // 2):
#     temp = la[c1]
#     la[c1] = la[c2]
#     la[c2] = temp
#     c1 += 1
#     c2 -= 1

print(la)
la = la[::-1]

for x in la:
    if x < 0:
        lb.append(x)
    else:
        fat = 1
        for y in range(2, (x+1)):
            fat *= y
        lb.append(fat)
print(la)
print(lb)

'''
4) Faça um programa que recebe uma lista de números inteiros de tamanho 100. O programa
deve percorrer esta lista e imprimir na tela o valor mais próximo da média dos valores deste
vetor. Exemplo:
vetor = [2.5, 7.5, 10.0, 4.0]
(média = 6.0)
Valor mais próximo da média = 7.5
'''

from random import randint
from os import maxsize


vetor = [randint(1, 100) for _ in range(100)]
media = sum(vetor) / 100
dif, menor = 0, maxsize

if media in vetor:
    print(f'VETOR: {vetor}\nMEDIA: {media}\nVALOR MAIS PROX: {menor}')
else:
    for x in vetor:
        dif = abs(x - media)
        if dif < menor:
            menor = dif
    print(f'VETOR: {vetor}\nMEDIA: {media}\nVALOR MAIS PROX: {menor}')
