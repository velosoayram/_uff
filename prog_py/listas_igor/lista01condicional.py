# 1) V | F.

'''
a) Uma variável é uma posição na memória do computador que pode receber diversos
valores ao longo da execução do programa. VERDADEIRO

b) Uma mesma variável pode receber diferentes tipos de valores (alfanuméricos,
numéricos, lógicos) durante a execução do programa. VERDADEIRO

c) Variáveis de tipos diferentes podem ser usadas para troca de valores, com uso de
conversão de tipos. VERDADEIRO

d) Cada variável utilizada pode ser acessada em qualquer parte do programa. 

FALSO -> Se uma variável é criada somente numa situação de aninhamento, ela não pode ser acessada posteriormente fora do "ninho".

e) Não é permitido utilizar duas variáveis com o mesmo nome. 

FALSO -> É permitido o "amarramento" de variáveis, que mudam seu valor e permanecem com um mesmo nome.

f) A operação aritmética soma é a única com o mesmo nível de precedência da
multiplicação. 

FALSO -> Somas possuem o mesmo nível de precedência de subtrações, já as multiplicações são juntas com as divisões.

g) Quando uma expressão aritmética apresenta parênteses aninhados, sempre o conjunto
mais interno é avaliado primeiro. VERDADEIRO

h) Os comentários permitem que o texto após o caractere "#" seja impresso na tela. 

FALSO -> O interpretador desconsidera completamente qualquer trecho do código a seguir do "#".

i) Duas variáveis definidas como “teste” e “Teste” são consideradas como idênticas. 

FALSO -> O interpretador é "Case Sensitive", então um valor muda completamente se a caixa está alta ou baixa.

j) Os operadores ( * + - / ) tem todos a mesma precedência. 

FALSO -> Somas possuem o mesmo nível de precedência de subtrações, já as multiplicações são juntas com as divisões.
'''

# 2) DETALHE O PROGRAMA ABAIXO:

x = 2
y = 3
z = 0.5
print(x + x * x ** (y * x) / z)

'''
1 - a primeira operação a ser resolvida está nos parênteses (y * x)                               | (3 * 2) = 6
2 - devemos agora fazer a operação de maior precedência '**' com a equação (2 + 2 * 2 ** 6 / 0.5) | (2 ** 6) = 64
3 - continuamos a resolver com a maior precedência '*' e '/' com a equação (2 + 2 * 64 / 0.5)     | (2 * 64) = 128 -> 128/0.5 = 256.0
4 - por último, a operação restante '+' com a equação (2 + 256)                                   | (2 + 256) = 258.0
5 - resultado = 258.0
'''

print(not x + z < y or x + x * z >= y and True)

'''
1 - temos uma ordem de precedência Aritmética, Comparativa e Lógica, respectivamente:
2 - realizando as operações matemáticas da expressão print(not 2 + 0.5 < 3 or 2 + 2 * 0.5 >= 3 and True)
''' 
print(not 2.5 < 3 or 3.0 >= 3 and True)
print(not True or True and True)

'''
3 - precisamos testar as afirmações lógicas com a ordem de precedência 'not', 'and', 'or' na expressão print(not True or True and True) 
'''

not True = False      | False or True and True
True and True = True  | False or True
False or True = True  | True
    
'''
No fim, o programa irá printar '258.0' e 'True':
    258.0
    True
'''

# 3) PROGRAMAS EM PYTHON QUE:


'''
a) calcular a área do cubo.
'''

aresta = int(input('DIGITE O TAMANHO DA ARESTA DO SEU CUBO: '))
base = aresta * aresta
area_tot = base * 6
print(f'A ÁREA TOTAL DO CUBO: {area_tot}')

'''
b) Escreva um programa que recebe três inteiros como entrada do teclado e escreva na
tela a média, a soma, o produto, o menor valor e o maior valor, usando uma linha para
cada resultado.
'''

n1 = int(input())
n2 = int(input())
n3 = int(input())

maior = menor = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
    
print(f'SOMA:    {n1 + n2 + n3}')
print(f'MEDIA:   {(n1 + n2 + n3)/3}')
print(f'PRODUTO: {n1 * n2 * n3}')
print(f'MENOR:   {menor}') # min(n1, n2, n3)
print(f'MAIOR:   {maior}') # max(n1, n2, n3)

'''
c) Em uma loja e CD ́s existem apenas quatro tipos de preços que estão associados a
cores. Assim os CD ́s que ficam na loja não são marcados por preços e sim por cores.
Desenvolva o algoritmo que a partir a entrada da cor o software mostre o preço. A loja
está atualmente com a seguinte tabela de preços.

i. Cor Preço
ii. Verde R$ 10,00
iii. Azul R$ 20,00
iv. Amarelo R$ 30,00
v. Vermelho R$ 40,00
'''
verde, azul, amarelo, vermelho = 10, 20, 30, 40
cor = str(input('COR DO SEU CD: ')).strip().upper()
if cor == 'VERDE':
    print(f'PREÇO: {verde}')
elif cor == 'AZUL':
    print(f'PREÇO: {azul}')
elif cor == 'AMARELO':
    print(f'PREÇO: {amarelo}')
elif cor == 'VERMELHO':
    print(f'PREÇO: {vermelho}')

'''
d) Escreva um programa que recebe três números e retorna a soma deles, porém se
houver números repetidos o valor deles não é contabilizado. Por exemplo, na entrada
(1,2,3) a resposta é 6, na entrada (3,2,3) a resposta é 2 e na entrada (3,3,3) a resposta
é 0.
'''

n1, n2, n3 = int(input('N1: ')), int(input('N2: ')), int(input('N3: '))
soma = 0
if n1 != n2 and n1 != n3:
    soma += n1
if n2 != n1 and n2 != n3:
    soma += n2
if n3 != n1 and n3 != n2:
    soma += n3
print(f'RESULTADO: {soma}')

'''
e) Escreva um programa que receba três números. O programa deve imprimir a palavra
“soma” se a soma de dois deles for igual ao outro número, caso contrário, o programa
deve imprimir a palavra “multi” se a multiplicação de dois deles for igual ao outro
número. Caso nenhuma das duas possibilidades for verdade, então imprimir a palavra
“par” se a soma dos três números for par, e imprimir a palavra “impar” caso contrário.
Por exemplo, na entrada (8,3,5) a resposta é “soma”, na entrada (3,3,1) a resposta é
“multi”, na entrada (8,4,9) a resposta é “impar”.
'''

n1, n2, n3 = int(input('N1: ')), int(input('N2: ')), int(input('N3: '))
if n1 + n2 == n3 or n1 + n3 == n2 or n2 + n3 == n1:
    print('soma')
elif n1 * n2 == n3 or n1 * n3 == n2 or n2 * n3 == n1:
    print('multi')
elif (n1 + n2 + n3) % 2 == 0:
    print('par')
else:
    print('impar')

'''
f) Faça um programa que leia três coordenadas num espaço 2D e indique se formam um
triângulo, juntamente com o seu tipo (equilátero, isósceles e escaleno):

i. Equilátero: todos os lados iguais
ii. Isósceles: dois lados iguais
iii. Escaleno: todos os lados diferentes

Condição de existência) um triângulo com lados de tamanho a,b,c existe se :
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
'''

c1, c2, c3 = int(input('C1: ')), int(input('C2: ')), int(input('C3: '))
if c1 + c2 > c3 and c1 + c3 > c2 and c2 + c3 > c1:
    if c1 == c2 and c2 == c3:
        print('EQUILATERO')
    elif c1 == c2 or c1 == c3 or c2 == c3:
        print('ISOSCELES')
    else:
        print('ESCALENO')
else:
    print('IMPOSSIVEL FORMAR')

'''
g) Faça um programa que a partir de um número informado em centavos (inteiro), indique
a menor quantidade de moedas que representa esse valor. Considere moedas de 1,25
e 50 centavos e 1 real (100 centavos). Exemplo: 290 centavos é representado por 2
moedas de 1 real, 1 de 50c, 1 de 25c, 15 de 1c.

Dica) Podemos usar as operações de divisão inteira (//) e resto da divisão (%) para
saber quantas moedas de um tipo podem ser usadas no troco.

Ex: Para um valor de 142 centavos e a moeda de 25 centavos, temos que 142//25=5,
logo podemos dar 5 moedas de 25 centavos no troco. Além disso, veja que
142%25=17, logo depois de dar o troco de 5 moedas de 25 centavos, ainda restaria 17
centavos para dar de troco em moedas de valor menor.
'''

# JEITO //
centavos = int(input())
moeda100 = centavos//100
moeda050 = (centavos - moeda100 * 100) // 50
moeda025 = ((centavos - moeda100 * 100) - moeda050 * 50) // 25
moeda001 = (((centavos - moeda100 * 100) - moeda050 * 50) - moeda025 * 25) // 1
print(f'MOEDAS 1,00 R$: {moeda100}\n'
f'MOEDAS 0.50 R$: {moeda050}\n'
f'MOEDAS 0.25 R$: {moeda025}\n'
f'MOEDAS 0.01 R$: {moeda001}')

# JEITO %
centavos = int(input())
moeda100 = centavos // 100
moeda050 = centavos % 100 // 50
moeda025 = centavos % 100 % 50 // 25
moeda001 = centavos % 100 % 50 % 25 // 1
print(f'MOEDAS 1,00 R$: {moeda100}\n'
f'MOEDAS 0.50 R$: {moeda050}\n'
f'MOEDAS 0.25 R$: {moeda025}\n'
f'MOEDAS 0.01 R$: {moeda001}')