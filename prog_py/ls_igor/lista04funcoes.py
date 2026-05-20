'''
1) Faça um programa em para calcular as quatro operações, uma calculadora. Crie uma
função que retorne a soma de dois números passados por parâmetro, outra para
subtração, multiplicação e divisão respectivamente. Crie uma função chamada
“interface_calculadora”, onde o programa deverá pedir dois números ao usuário e a
operação desejada, se a a operação for soma deve ser chamado a função soma, e
assim para as outras opções.
'''

def soma(*x): # o parâmetro com asterisco passa todos os valores dentro de uma tupla.
    resultado = 0 # por isso é possível iterar sobre.
    for _ in x: 
        resultado += _
    return resultado


def subtracao(*x): # tomei a liberdade de fazer em todos, porque torna possível a operação entre dois números.
    resultado = x[0] # mas também de ilimitados números.
    for _ in x[1:]: 
        resultado -= _
    return resultado


def multiplicacao(*x):
    resultado = x[0] # os resultados recebem o primeiro valor da tupla como valor inicial.
    for _ in x[1:]: # para que seja possível "adicionar" a operação de maneira sucessiva.
        resultado *= _
    return resultado


def divisao(*x):
    resultado = x[0]
    for _ in x[1:]: # isto é, partiindo de um range que não conta o primeiro valor da tupla, por meio do slicing.
        resultado /= _
    return resultado


def interface_calculadora(func, *x): # o python já passa a própria função, ele não passa como string.
    resultado = func(*x) # por isso é possivel fazer uma variável com esse valor.
    return resultado


print(interface_calculadora(multiplicacao, -1, -3)) 


'''
2) Escreva uma função que receba uma lista de n números inteiros e retorne, para o
usuário, o comprimento da maior sequência crescente.
Ex: na lista a = [6, 11, 4, 3, 5, 8, 10, 9, 6], o comprimento da maior sequência crescente
é 4 (pois 3, 5, 8 e 10 é a maior sequência crescente). Já nesta lista b =[11, 9, 6, 4, 3], o
comprimento da maior sequência é 1.
'''

def sublista_crescente(lista):

    maior_seq = c = 1 # a sequência deve começar em 1, já que a maior sequência mínima possível é o próprio número.
    for l in range(len(lista) - 1): # determino o range como (n - 1), já que irei comparar os seus pares l, (l + 1), evitando index out of range.
        if lista[l] >= lista[l + 1]: # se o termo for maior que o seu superior, automaticamente a sequência é quebrada.
            c = 1 # reseto a contagem sentinela para possíveis outras sequências.
        else : c += 1  # contagem segue.
        if c > maior_seq: # se a contagem ultrapassar a maior sequência já contabilizada.
            maior_seq = c # a maior sequência é atualizada.
    return maior_seq


lista1 = [6, 11, 4, 3, 5, 8, 10, 9, 6]
lista2 = [11, 9, 6, 4, 3]
print(sublista_crescente(lista1), sublista_crescente(lista2) )


'''
3) Faça um programa que solicite ao usuário números e os armazene em um vetor de
20 posições. Crie uma função que recebe o vetor preenchido e substitua todas as
ocorrências de valores negativos por zero, as ocorrências de valores menores do que
10 por 1 e as demais ocorrências por 2.
'''

def substituidor(vetor):

    for i, v in enumerate(vetor):
        if v < 0: # se termo negativo, vira 0.
            vetor[i] = 0
        elif v < 10: # se termo menor que 10, vira 1.
            vetor[i] = 1
        else: # se termo maior que 10, vira 2.
            vetor[i] = 2
    return vetor


vetor = [int(input()) for x in range(20)] # 20 números solicitados.
print(vetor, substituidor(vetor))


'''
4) Crie uma função que retorne o valor da expressão: 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m,
para um valor de n e m definido pelo usuário. No programa, verifique se o valor de n
definido pelo usuário é positivo (antes de chamar a função) e, caso não seja, solicite
outro valor repetidamente até ser fornecido um valor positivo.
'''

def somatorio(n):

    soma, denominador = 0, 1 # ao começar o denominador como 1, posso adentrar no loop à partir do número 3.
    for x in range(2, n+1): # x será o numerador que irá de 2 até n.
        denominador += 2 # denominador ímpar atualizado
        soma += x / denominador # a razão é somada consecutivamente.
    return f'{soma:.3f}'


n = int(input()) # a expressão é definida pelo valor mínimo 2 até o máximo n como numerador.
while n < 2: # já o m é a sequência de todos os ímpares contáveis partindo do 3.
    n = int(input('DIGITE UM NÚMERO POSITIVO: '))
print(somatorio(n))


'''
5) Escreva uma função que recebe uma lista B com n elementos (sem repetições) e um
índice k (onde 0 <= k < n) e tem como saída o índice do elemento mínimo entre B[k],
B[k+1], ..., B[n-1].
Ex: B[6,2,9,4,6,11,2,3] e k=3 → índice 6 (que equivale ao elemento 2)
'''

def k_para_n(lista, k):

    from sys import maxsize

    minimo = maxsize # garantia de que a comparação de qualquer valor será menor que maxsize.
    resultado = 0
    for i, v in enumerate(lista[k:]): # iteramos à partir do índice k para a contagem.
        if v < minimo:
            minimo = v # atualizamos o menor valor à partir do índice k.
            resultado = (f'ÍNDICE: {i + k} | ELEMENTO: {v}')
    return resultado


n = int(input()) # os n valores do vetor.
k = int(input()) # o índice k desejado.
vetor = []
for x in range(n):
    temp = int(input())
    while temp in vetor: # garantia de que não irá adicionar termos repetidos no vetor, embora o exemplo do enunciado esteja incoerente.
        temp = int(input())
    vetor.append(temp)
print(k_para_n(vetor, k)) # entrada do vetor e o índice escolhido.


'''
6) Crie uma função para calcular e imprimir os n primeiros números de Tribonacci. A
série de Tribonacci consiste em: 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504,... Para
calcula-la o primeiro elemento vale 1, o segundo elemento vale 1, o terceiro elemento
vale 2, e daí por diante.
Assim, o i-ésimo elemento vale o (i-1)-ésimo elemento somado ao (i-2)-ésimo elemento
somado ao (i-3)-ésimo elemento. Exemplo, 13=7+4+2. Observe que n deve ser positivo.
'''


def tribonacci(n):

    el1, el2, el3 = 1, 1, 2 # aqui deixamos os elementos declarados para que uma sequência maior que 3 possa ocorrer num loop.
    if n == 1:
        ordem = [el1] 
    elif n == 2:
        ordem = [el1, el2] 
    elif n == 3:
        ordem = [el1, el2, el3] 
    else: # caso n seja maior que 3.
        ordem = [el1, el2, el3] 
        for x in range(3, n+1): # consideramos que já possui seus 3 iniciais valores, portanto, contamos os (n - 3) termos seguintes.
            temp1 = el2 
            temp2 = el3 # variável temporária para que todos os elementos sejam alterados sem conflito.
            if x > 3:
                el3 = el3 + el2 + el1 # el3 vira o próximo termo, que é a própria soma com el2 e el1.
                el2 = temp2 # el2 vira o antigo el3
                el1 = temp1 # el1 pega o antigo el2, que está na variável temporária
                ordem.append(el3)
    return ordem
    

n = int(input()) # os n termos da sequência de tribonacci.
print(tribonacci(n))
