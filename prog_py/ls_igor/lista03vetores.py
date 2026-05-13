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
from math import trunc
from sys import maxsize

vetor = [randint(1, 10) for _ in range(100)]
media = sum(vetor) / 100
menor, dif, valor = maxsize, 0, 0
for x in vetor:
    dif = abs(media - x)
    if dif == 0:
        valor = x
        break
    if dif < menor:
        menor = dif
        valor = x
print(f'O VALOR {valor} É O MAIS PRÓXIMO DA MÉDIA {media} DO VETOR.')


'''
5) Faça um programa que receba duas listas, uma de tamanho N e outra de tamanho M. O programa deve percorrer as duas listas e intercalar os elementos de ambas, formando uma
terceira lista. A terceira lista deve começar pelo primeiro elemento da lista menor. Quando acabar de intercalar os elementos, se ainda tiver elementos sobrando na lista maior, colocar esses elementos no fim da terceira lista.

Exemplo:
v1 = [1, 7, 3, 9]
v2 = [10, 2, 47, 40, 93, 8]
v3 = [1, 10, 7, 2, 3, 47, 9, 40, 93, 8]
'''

from random import randint

n, m, i = int(input('VALOR N: ')), int(input('VALOR M: ')), 0
l1, l2, l3 = [randint(1, 10) for _ in range(n)], [randint(1, 10) for _ in range(m)], []
while len(l3) != (n+m):
    if n < m:
        if i < len(l1):
            l3.append(l1[i])
        if i < len(l2):
            l3.append(l2[i])
    else:
        if i < len(l2):
            l3.append(l2[i])
        if i < len(l1):
            l3.append(l1[i])
    i += 1
print(l3)


'''
6) Escreva um programa que:

(a) O funcionário fornecerá o número de candidatos N, o nome e as 3 notas de cada
candidato. O programa deve armazenar os nomes dos candidatos em uma lista e a média das
notas em outra lista (dado as 3 notas).

(b) Apresentar um relatório apresentando o nome dos candidatos em ordem crescente
de classificação de acordo com a média obtida, como exemplo abaixo. Para isso as listas
devem ser ordenadas ao mesmo tempo (por algum método).
'''

n, c = int(input()), 0
nomes, medias = [], []

for i in range(n):
    nome, nota1, nota2, nota3 = input(), int(input()), int(input()), int(input())
    nomes.append(nome)
    medias.append((nota1 + nota2 + nota3) / 3)
candidatos = sorted(zip(nomes, medias), reverse = True)
for v in candidatos:
    print(f'NOME: {v[0]:<8}  |  MEDIA: {v[1]:.2f}')

'''
7) Faça um programa que simule uma agenda telefônica onde o usuário informe os telefones
(inteiros) e você deverá inserir estes valores de forma ordenada uma lista. O usuário deve ser
capaz de inserir até 100 telefones. A cada número inserido, imprima a agenda.
Ex:
Insere 2211
Agenda=[2211]
Insere 923
Agenda=[923,2211]
Insere 1555
Agenda=[923,1555,2211]
'''

agenda = []
for a in range(100):
    num = int(input())
    agenda.append(num)
    agenda.sort()
    print(agenda)