'''
1) Faça um programa em Python que receba um conjunto de 100 elementos numéricos e os armazene em uma lista. Em seguida, o programa deverá procurar se existem no vetor elementos iguais a um dado valor também informado pelo usuário e imprimir o índice das posições em que estes são encontrados.
'''

from random import randint # nesse codigo, e nos seguintes, achei jogo fazer list comprehension para os conjuntos de elementos numéricos.

n = int(input())

vetor, pos = [randint(0, 100) for _ in range(100)], [] # faço o list comprehension usando randint(), evitando input()s desagradaveis.
for i in range(len(vetor)): # itero sobre os indices do meu vetor.
    if vetor[i] == n: # e se o elemento for igual ao número n que estou buscando:
        pos.append(i) # então eu armazeno o seu índice numa outra lista.

# aqui abaixo eu trabalho o output do problema, mesmo que o enunciado não peça:

if len(pos) > 1: # se houver mais de um índice na lista.
    print(f'{n}, POSIÇÃO: {pos}')
elif len(pos) == 1: # se houver somente um índice na lista.
    print(f'Só há um elemento {n} no vetor.')
else: # se a lista está vazia, não existe n na lista.
    print(f'{n} não está no vetor.')

'''
2) Uma locadora de videogame tem guardada, em uma lista de 500 posições, a quantidade de jogos retirados por seus clientes durante o ano passado (i.e. Clientes[i] = X -> o cliente “i” retirou X jogos no ano passado). Agora esta locadora está fazendo uma promoção e, para cada 10 jogos retirados no ano passado, o cliente tem direito a uma locação grátis. Faça um programa que crie um outro vetor contendo a quantidade de locações gratuitas a que cada cliente tem direito.
'''

from random import randint

clientes = [randint(1, 50) for _ in range(500)] # lista com 500 posições e valores aleatórios de 1 a 50 determinando a quantidade de jogos retirados por cada cliente.
locacoes = [(a // 10) for a in clientes] # itero sobre a lista anterior e crio o vetor da quantidade de locações gratuitas por cliente dividindo (por inteiros) quantidades de 10.
for x in range(len(clientes)):
    print(f'Cliente {x+1} com direito a {locacoes[x]} locações gratuitas.') # mesmo que o exemplo não peça explicitamente para imprimir, eu imprimo todos.

'''
3) Faça um programa que receba uma lista A de dimensão N e:

(a) Inverta os valores de A, troque o primeiro pelo ultimo, o segundo pelo penúltimo e assim por diante.

(b) Após este procedimento, criar um vetor B de dimensão N com o fatorial de cada valor de A, respeitando as posições, caso o valor for positivo ou nulo. Deixe os valores negativos intactos.

(c) Imprima o vetor B.
'''

from random import randint

# precisamos de duas listas, a A e a B (la, lb).

n, c1, c2 = int(input()), 0, -1 # n é a dimensão da lista A; c1 e c2 são contadores.
la, lb = [randint(-10, 10) for _ in range(n)], [] # listas la e lb; de acordo com o item (b), o problema entrega valores negativos, então o randint inclui negativos para la.
la = la[::-1] # aqui inverti a posição dos valores de la, usando slicing ao invés de algum tipo de ordenação.

for x in la:
    if x < 0: # se o elemento de la for negativo, ele é adicionado a lb de maneira intacta.
        lb.append(x)
    else: # se o elemento for nulo ou positivo.
        fat = 1 # por convenção, o fatorial de 0 é 1, essa variável garante isso.
        for y in range(2, (x+1)): # iteramos pelo valor x, multiplicando seus antecessores de 2 ao valor x.
            fat *= y # aqui o valor do fatorial é atualizado e adicionado a lb.
        lb.append(fat)
print(la)
print(lb) # imprimo lb, e para fins comparativos la também.

'''
4) Faça um programa que recebe uma lista de números inteiros de tamanho 100. O programa
deve percorrer esta lista e imprimir na tela o valor mais próximo da média dos valores deste
vetor. Exemplo:
vetor = [2.5, 7.5, 10.0, 4.0]
(média = 6.0)
Valor mais próximo da média = 7.5
'''

from random import randint
from sys import maxsize

vetor = [randint(1, 10) for _ in range(100)] # lista dos números inteiros de tamanho 100.
media = sum(vetor) / 100
menor, dif, valor = maxsize, 0, 0
for x in vetor: # para cada número do vetor, eu tiro o módulo dele com a média.
    dif = abs(media - x)
    if dif == 0: # se o módulo for 0, a média está no vetor, logo o loop termina.
        valor = x
        break # poupando processamento
    if dif < menor: # caso não haja média dentro do vetor, a variável recebe o menor módulo possível.
        menor = dif # sentinela para a condição.
        valor = x
print(f'O VALOR {valor} É O MAIS PRÓXIMO DA MÉDIA {media} DO VETOR.') # imprime o valor mais prócimo da média dentro do vetor.


'''
5) Faça um programa que receba duas listas, uma de tamanho N e outra de tamanho M. O programa deve percorrer as duas listas e intercalar os elementos de ambas, formando uma
terceira lista. A terceira lista deve começar pelo primeiro elemento da lista menor. Quando acabar de intercalar os elementos, se ainda tiver elementos sobrando na lista maior, colocar esses elementos no fim da terceira lista.

Exemplo:
v1 = [1, 7, 3, 9]
v2 = [10, 2, 47, 40, 93, 8]
v3 = [1, 10, 7, 2, 3, 47, 9, 40, 93, 8]
'''

from random import randint

n, m, i = int(input('VALOR N: ')), int(input('VALOR M: ')), 0 # valores n e m, e contador de índices.
l1, l2, l3 = [randint(1, 10) for _ in range(n)], [randint(1, 10) for _ in range(m)], [] # criação das listas, l1 e l2 nos raios de n e m, respectivamente.

if n < m: # se l1 < l2, l1 tem o primeiro elemento adicionado a l3.
    while len(l3) != (n+m): # enquanto o vetor l3 não chegar ao tamanho da soma de l1 e l2.
        if i < len(l1):
            l3.append(l1[i])
        if i < len(l2): # condições if necessárias: se estão iterando sobre vetores de tamanhos diferentes usando mesmo i, em dado momento -> list index out of range 
            l3.append(l2[i])
        i += 1
else: # caso não, l2 tem o primeiro elemento adicionado a l3.
    while len(l3) != (n+m):
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

def bubble_medias(nomes, medias):

    n = len(medias)

    for a in range(n):
        for b in range(0, n - a - 1):
            if medias[b] > medias[b+1]:
                medias[b], medias[b+1] = medias[b+1], medias[b]
                nomes[b], nomes[b+1] = nomes[b+1], nomes[b]
    l3 = [(v, medias[i]) for i, v in enumerate(nomes)]
    return l3


n = int(input())  # valor n.
nomes, medias = [], [] # listas de nomes e medias.

for i in range(n):
    nome, nota1, nota2, nota3 = input(), int(input()), int(input()), int(input()) # os input()s necessários de acordo com os n alunos.
    nomes.append(nome) # nome adicionado à lista de nomes.
    medias.append((nota1 + nota2 + nota3) / 3) # média adicionado à lista de médias.

# para unir os nomes com suas respectivas médias, criar uma terceira lista intercalando valores como no exemplo anterior poderia ser uma solução,
# usar a função enumerate() também, considerando que a lista de nomes e média possuem o mesmo tamanho, bastava iterar sobre uma usando seu índice
# e sobre a outra iterar sobre ela própria num mesmo loop.

candidatos = sorted(zip(nomes, medias), key=lambda item: item[1])

# todavia, resolvi experimentar o zip(), um iterador de tuplas, que desempenha o mesmo papel de um jeito pythonico.
# utilizando o lambda para que o sorted() enxergue a ordenação pelo segundo elemento da tupla, que é a nota, e não pelo nome, de forma crescente.

# mas, também é válido usar um tipo de ordenação, como um bubble sort, para que sejam alteradas ao mesmo tempo, como requisitado mo item (b).
# para isso fiz a função bubble_medias() para demonstração nesse caso em específico de listas intercaladas.

        # x = bubble_medias(nomes, medias)

        # for v in x:
        #     print(f'NOME: {v[0]:<8}  |  MEDIA: {v[1]:.2f}')

for c in candidatos:
    print(f'NOME: {c[0]:<8}  |  MEDIA: {c[1]:.2f}') # o output de tabela.

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

agenda = [] # lista da agenda.

for a in range(100):
    num = int(input())
    agenda.append(num) # adiciono valor.
    agenda.sort() # ordeno valor na lista.
    print(agenda) # imprimo.

# esse é o caso de uso de um tipo de ordenação que poupe processamento, como um insertion sort, ao invés de um método .sort().
# para diferenciação, farei com insertion aqui abaixo:

agenda = [] # lista da agenda.

for a in range(100):

    num = int(input())

    agenda.append(num)

    j = len(agenda) - 2 # é necessária para acessar à partir do penúltimo elemento da lista.

    chave = num # essencial para guardar o elemento num durante as trocas e comparações do loop.

    while j >= 0 and agenda[j] > chave: # permitindo que j seja menor que 0, acabaríamos acessando o último elemento da lista indevidamente.

        agenda[j+1] = agenda[j] # quando o penúltimo elemento é maior, o último recebe o penúltimo.
                                # e assim regressivamente, caso necessrário.

        j -= 1 # o processo é repetido n vezes até que a chave seja de fato o menor elemento da lista, então percorremos com o índice j, que deixa de ser o penúltimo item.
               # e quando/se j vira -1, o loop acaba.

    agenda[j+1] = chave # quando então, os elementos maiores vão sendo copiados à direita de agenda[j], o loop termina quando j = -1, ou agenda[j] já é menor ou igual à chave
                        # e aí entra o [j + 1], já que j não pode ser -1, e [j + 1] se trata de uma cópia feita dentro do loop para possivelmente ocupar a chave.
    print(agenda)

