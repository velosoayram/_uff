'''
1) Interpretar e traduzir para Python a sequência de comandos em Português a seguir:


    Algoritmo {escrita dos termos de Fibonacci menores que L}
    leia o valor L
    {Processamento dos dois primeiros termos}
    Atribua o valor 1 ao termo1
    se ele for menor do que L então
    escreva-o
    fim se
    Atribua o valor 1 ao termo2
    se ele for menor do que L então
    escreva-o
    fim se
    {Processamento dos termos restantes}
    enquanto novo termo1 mais termo2 for menor ou igual a L faça
    Calcule o novo termo somando os 2 anteriores
    escreva o termo
    Atribua termo2 a termo1
    Atribua termo a termo2
    fim enquanto
    Fim algoritmo.
'''

# a explicação desse código se dá basicamente pelo enunciado todo dele.
# ao pé da letra seria exatamente o código abaixo, embora fizesse mais sentido rodar o código dentro de um loop com contador, ou igualando os "termos <= L".
# ex1: se L == 2, o output sairá "1 1 2" ao invés de "1 1" | ex2: se L == 1, o output sairá "1 1" ao invés de "1".

L = int(input())
termo1 = termo2 = 1 # declaração encadeada.
if termo1 < L: # se termo1 menor que L mostre na tela.
    print(termo1, end = ' ')
if termo2 < L: # se termo2 menor que L mostre na tela.
    print(termo2, end = ' ')
while termo1 + termo2 <= L: # enquanto soma deles menor ou igual a L.
    novo = termo1 + termo2
    print(novo, end = ' ') # mostre na tela.
    termo1 = termo2 # substituição dos termos para a sequencia rodar progressivamente.
    termo2 = novo

'''
2) Faça um programa em Python que:

a) Escreva um programa que permita que o usuário indique um número de inteiros “n” a serem
lidos (entre 1 e 30). Após a leitura dos “n” números, escreva na tela a média, a soma, o produto,
o menor valor e o maior valor.
'''

n = int(input(r'QUANTOS "n" VALORES QUER LER (1 a 30): ')) # input para ler até "n" números.
maior = menor = media = soma = produto = 0 # declaração encadeada.
for x in range(n): # no raio dos "n" números.
    num = int(input(f'DIGITE O {x+1}° NÚMERO: ')) # digite um número da sua sequéncia de "n" números.
    if x == 0: # verificação inicial do contador, necessária para impedir que alguma equação, como a *, seja feita por 0.
        produto = soma = num # se a variável soma fosse declarada com valor 1, teria um excedente no seu resultado.
        maior = menor = num # se igualando tudo à variável num, o risco de multiplicar 0 some.
    else: # se não o primeiro item, faça as operações.
        produto *= num
        soma += num
        if num > maior: # declaração do maior por comparação.
            maior = num
        elif num < menor: # declaração do menor por comparação.
            menor = num
print(f'MAIOR   | {maior}\n'
      f'MENOR   | {menor}\n'
      f'SOMA    | {soma}\n'
      f'MEDIA   | {(soma/n):.1f}\n'
      f'PRODUTO | {produto}')

'''
b) Faça um programa para construir a tabela de multiplicação de números de 1 a 10 (ex.: 1 x 1 = 1,
1 x 2 = 2, ....,2 x 1 = 2, 2 x 2 = 4, ...., etc.).
'''

# loops aninhados para que ocorra todas as possibilidades de multiplicações até 10, entre os números de 1 a 10.

for x in range(1, 10+1):  # no raio de "x".
    print(f'TABUADA DO {x}\n') # "x" sendo o contador do loop [1] = TABUADA DO 1.
    for y in range(1, 10+1): # "y" é o número pelo qual está sendo multiplicado "x".
        print(f'{x:>2} * {y:>2} = {x*y:>2}') # formatação de string para melhor visual.
    print() # espaço em branco para separar os outputs.

'''
c) gerar os cinquenta primeiros termos da série: 1 + N, 5 * N, 9 + N, 13 * N, ..., onde N é um valor
lido.
'''

N = int(input())
termo = 1
for seq in range(50): # no raio dos 50 termos.
    if seq == 0 or seq % 2 == 0: # há um pequeno detalhe, toda vez que o contador for par, em equivalência, na sequéncia será uma soma.
        print(termo + N, end = ' ')
    else: # toda vez que o contador for ímpar, em equivalência, na sequéncia será uma multiplicação.
        print(termo * N, end = ' ')
    termo += 4 # a razão entre os termos inteiros definidos na sequência é de 4 em 4: [1, 5, 9, 13, ...].

'''
d) determinar todos os números de 3 algarismos, cujas somas dos cubos dos algarismos sejam
iguais ao próprio número. Exemplo: 153 = 1**3 + 5**3 + 3**3.
'''

for x in range(100, 999+1): # no raio de todos os números de três algarismos.
    if ((x // 100)**3) + ((x % 100 // 10)**3) + ((x % 100 % 10)**3) == x: # a validação matemática, isolando as centenas, dezenas e unidades e operando sobre elas.
        print(x)

# o isolamento.
# CENTENA: a divisão inteira de 123 // 100 = 1 centena.
# DEZENA: o resto da divisão de 123 % 100 = 23 | 23 // 10 = 2 dezenas.
# UNIDADE: o resto da divisão de 123 % 100 = 23 | 23 % 10 = 3 unidades.

'''
e) Um número inteiro é considerado triangular se este for o produto de 3 números inteiros
consecutivos, como, por exemplo, 120 = 4 x 5 x 6. Elabore um programa que, após ler um
número n do teclado, verifique se n é triangular.
'''

n = int(input())
termo = produto = 1 # declaração encadeada.
while produto <= n: # enquanto o produto não ultrapassar o termo "n".
    produto = (termo) * (termo+1) * (termo+2) # produto é a multiplicação de três termos consecutivos.
    if produto == n: # se produto chegar ao exato valor de "n", mostre e pare.
        print(f'{n} é triangular.')
        break
    termo += 1 # garantia do término do loop.
else: # se não for triangular, o loop quebra por produto ser maior que o termo "n".
    print(f'{n} não é triangular.')

'''
f) Escreva um programa que imprime na tela os n primeiros números perfeitos. Um número
perfeito é aquele que é igual à soma dos seus divisores (tirando ele mesmo). Por exemplo, 6 = 1
+ 2 + 3 é perfeito.
'''

n = int(input())
flag = cont = 1 
while flag <= n:
    soma_div = 0
    for x in range(1, (cont//2)+1): # o raio vai até a metade do número da vez: se eu não preciso do próprio número na soma, e nenhum divisor "x" é
        if cont % x == 0:           # maior que o dobro do dividendo, é possível definir o raio como a metade do valor, otimizando as operações.
            soma_div += x
    if soma_div == cont: # se soma dos divisores obtidos igual ao número da vez, mostre.
        print(soma_div)
        flag += 1 # a flag é o que define quantos números perfeitos apareceram, então o loop acaba.
    cont += 1 # contador que corresponde ao número da vez dentro do loop.

'''
g) Suponha que um jogador A de PokemonGO tenha 800 pokemons com uma taxa de anual de
crescimento/captura de 3% e que o jogador B tem 2000 pokemons com uma taxa de
crescimento/captura de 1.5%. Faça um programa que calcule e retorne o número de anos
necessários para que o jogador A ultrapasse ou iguale o número de pokemons do jogador B,
mantidas as taxas de crescimento.
'''

anos = 0
jg_a = 800
jg_b = 2000
while jg_a < jg_b: # condição de parada até que o jogador A alcance o jogador B.
    jg_a += jg_a * (3/100) # porcentagens aplicadas sobre o valor de acordo com o enunciado.
    jg_b += jg_b * (1.5/100)
    anos += 1 # anos que se passam a cada porcentagem aplicada sobre o valor da vez.
if jg_a == jg_b:
    print(f'Necessitou {anos} ano(s) para que P1 ({jg_a:.0f}) igualasse P2 ({jg_b:.0f}).')
else:
    print(f'Necessitou {anos} ano(s) para que P1 ({jg_a:.0f}) ultrapassasse P2 ({jg_b:.0f}).')

'''
h) Fazer um programa que lê n números inteiros do teclado, e no final informa se os números lidos
estão ou não em ordem crescente.
Dica: guarde o número anterior gerado, se em alguma iteração o número fornecido atual for menor
que o número anterior, a ordem não é crescente.
'''

# o enunciado não abordou nada sobre números negativos, mas calhou de otimizar.

qtd = int(input())
num_ant = None # declaração vazia.
crescente = True # ou é crescente, ou não (ou 0 ou 1).
for x in range(qtd): # no raio da quantidade, coloque os números da sequência.
    num = int(input())
    if x > 0: # graças a essa condição, o "x" inicia em 0, então pula e define a variável "num_ant" como int() no primeiro loop, evitando conflito do None > num.
        if num_ant > num: # type: ignore 
            crescente = False
    num_ant = num # por quê? se iniciasse "num_ant" como 0, ao escrever uma sequência com números negativos, ela já seria False na primeira iteração (-n < 0).
if crescente:
    print('True')
else:
    print('False')

'''
3) Escreva um programa para gerar dois valores aleatórios inteiros “x” e “y” entre 1 e 100, que
representam o poder e a resistência de uma carta de Magic (para gerar o número aleatório usar randint).
Após isso, deve-se gerar a seguinte mensagem: “quanto é o poder x multiplicado pela resistencia y da
carta ?”, substituindo os números gerados por “x” e “y”. Depois da mensagem, deve ser lida uma resposta
do teclado e deve ser exibido uma mensagem indicando acerto ou erro. O programa deve implementar um
laço que obrigue o jogador a acertar pelo menos três vezes a resposta
'''

# esse desafio é o puro suco do sadismo, pior que acertar na mega-sena:

from random import randint

cont = 0 # flag do loop, quando acertar 3 vezes, acaba.
while True:
    if cont == 3:
        print('Parabens! Voce terminou o desafio.')
        break
    poder_x = randint(1, 100)
    resis_y = randint(1, 100)
    mul = poder_x * resis_y # valor questionado no enunciado - do poder pela multiplicação.
    resp = int(input('Quanto é o poder x multiplicado pela resistencia y da carta ? '))
    if resp == mul: # se acertar a multiplicação, soma 1.
        print(f'Voce acertou | {mul} era a resposta.')
        cont += 1 
    else: # se errar a multiplicação, mostra o valor correto e depois no decorrer do loop se altera o valor novamente.
        print(f'Voce errou | {mul} era a resposta.')

'''
4) Faça um programa que determina se dois valores inteiros e positivos A e B são “Bros” (dois números
inteiros são ditos “Bros”, caso não exista divisor comum aos dois números diferente de 1).
Dica: O método de Euclides é um dos algoritmos mais antigos (300 a.C.) e um dos mais
eficientes para calcular o Máximo Divisor Comum (M.D.C) de dois números inteiros
O algoritmo se baseia na seguinte propriedade:
MDC(A,B) = MDC(B, A%B)
que deve ser explorada iterativamente até que A%B seja 0 e B seja considerado o
MDC. Por exemplo, MDC(252,105) = MDC(105,42) = MDC(42,21) = 21, pois 42%21
é igual a zero. Portanto MDC(252,105) = 21.
'''

# BROS - números primos entre si.

resto = 1
maior = menor = 0
A, B = int(input()), int(input()) # declaração múltipla

if A > B: # aqui eu faço um bloco de controle de maior/menor | ajuda na visualização e na comparação do bloco abaixo.
    maior, menor = A, B
else: # seria possível resolver a atribuição de variáveis com as funções max([A, B]) e min([A, B]).
    maior, menor = B, A

while True: # no loop, preciso verificar igualdades e trocar o valor de variáveis conforme as operações ocorrem.

    resto = maior%menor # aqui é onde se instala a variável temporária, que se atualiza a cada iteração.

    if resto == 0: # como no enunciado, se a divisão do maior termo pelo menor obtiver resto 0, concluímos o objetivo.
        break # graças ao break, na última iteração permanecemos com o valor "menor" sendo o MDC da última iteração.
    maior = menor
    menor = resto

if menor == 1:
    print(f'{A} e {B} ARE BROS | MDC: {menor}')
else:
    print(f'{A} e {B} NOT BROS | MDC: {menor}')

'''
5) Faca um programa que imprima os N (inteiro fornecido pelo usuário) primeiros números da série do
Kirito A série inicia com os números 2,2, 3 e 3, e cada número posterior equivale a diferença entre a soma
dos 2 números anteriores multiplicado por 2, e a multiplicação dos 2 números antes destes anteriores (ex:
o próximo número da série eh (2*(3+3))-(2*2)=8). No fim, pergunte se o usuário quer entrar com outro N
e repetir o processo.
'''

# não há muito aqui, um loop com operações conforme a quantidade de "N" lida.

while True:
    N = int(input())
    termo1 = termo2 = 2
    termo3 = termo4 = 3 # definição dos primeiros 4 termos da sequência (2, 2, 3, 3).
    if N == 1:
        print(termo1)
    elif N == 2:
        print(termo1, termo2)
    elif N == 3:
        print(termo1, termo2, termo3)
    elif N == 4:
        print(termo1, termo2, termo3, termo4)
    else: # se "N" for maior que 4 roda, mostram todos os termos e roda um loop.
        print(termo1, termo2, termo3, termo4, end = ' ')
        for x in range(N-4): # consequentemente, com os 4 termos mostrados, o raio do loop deve ser subtraído em 4.
            pos = ((termo3 + termo4) * 2) - (termo1 * termo2) # a operação exigida para os termos.
            print(pos, end = ' ')
            termo1 = termo2
            termo2 = termo3
            termo3 = termo4
            termo4 = pos # a troca em sequência dos termos substituindo um ao outro pelo seu sucessor.
    resp = str(input("DESEJA CONTINUAR? [S/N]: ")).strip().upper()
    while resp not in ['S', 'N']: # uso do operador "in" para validar se o usuário quer continuar o processo.
        resp = str(input("DESEJA CONTINUAR? [S/N]: ")).strip().upper()
    if resp == 'N':
        break

'''
6) Calcule a soma da série S de Saitama, dado valores inteiros n e m fornecidos pelo usuário. No fim,
pergunte se o usuário quer repetir a operação.
'''

while True:
    S = 0 # a variável da soma total
    n, m = int(input()), int(input())

    for i in range(1, n+1): # basicamente, o somatório de i=1 a "n" do somatório abaixo.
        for j in range(1, m+1): # o somatório de j=1 a "m" da expressão abaixo.
            S += ((i**2) * j) / ((3**i) * (j * (3**i) + i * (3**j))) # a expressão requisitada variando os valores de "i" e "j".

    print(f'O RESULTADO S = {S} | COM m = {m}, n = {n}')
    
    resp = str(input('DESEJA REPETIR? [S/N]: ')).upper().strip()
    while resp not in ['S', 'N']: # repetição da operação
        resp = str(input('ERRO | [S/N]: ')).upper().strip()
    if resp == 'N':
        break

'''
7) Faça um jogo de pedra, papel, tesoura, spock e lagarto (de onde vem isso?), onde o jogador e o
computador escolhem entre “0-pedra 1-spock 2-paper 3-lagarto 4-tesoura” (a jogada do computador é
aleatória). Ganha o jogo quem vencer 3 vezes primeiro (As regras de vitória estão descritas na figura
abaixo).
'''

# um JO-KEN-PO um pouco modificado, uma série de comparações dentro de um while.
# fazer com listas otimizaria.

from random import randint


cont_pc = cont_player = 0
while True:
    print('0 - PEDRA\n'
        '1 - SPOCK\n'
        '2 - PAPEL\n'
        '3 - LAGARTO\n'
        '4 - TESOURA')
    pc = randint(0, 4)
    player = int(input('ESCOLHA SEU NUM (0 A 4): '))
    while player not in [0, 1, 2, 3, 4]:
        player = int(input('ERRO | ESCOLHA SEU NUM (0 A 4): '))
    print()
    if pc == 0: # pedra
        if player == 0:
            print('EMPATE! AMBOS ESCOLHERAM PEDRA')
        elif player == 1:
            print('GANHOU! PONTO PRO PLAYER (SPOCK)     | PC: PEDRA.')
            cont_player += 1
        elif player == 2:
            print('GANHOU! PONTO PRO PLAYER (PAPEL)     | PC: PEDRA.')
            cont_player += 1
        elif player == 3:
            print('PERDEU! PONTO PRO PC (PEDRA)         | VOCE: LAGARTO.')
            cont_pc += 1
        else:
            print('PERDEU! PONTO PRO PC (PEDRA)         | VOCE: TESOURA')
            cont_pc += 1
    elif pc == 1: # spock
        if player == 0:
            print('PERDEU! PONTO PRO PC (SPOCK)         | VOCE: PEDRA.')
            cont_pc += 1
        elif player == 1:
            print('EMPATE! AMBOS ESCOLHERAM SPOCK')
        elif player == 2:
            print('GANHOU! PONTO PRO PLAYER (PAPEL)     | PC: SPOCK.')
            cont_player += 1
        elif player == 3:
            print('GANHOU! PONTO PRO PLAYER (LAGARTO)   | PC: SPOCK.')
            cont_player += 1
        else:
            print('PERDEU! PONTO PRO PC (SPOCK)         | VOCE: TESOURA.')
            cont_pc += 1
    elif pc == 2: # papel
        if player == 0:
            print('PERDEU! PONTO PRO PC (PAPEL)         | VOCE: PEDRA.')
            cont_pc += 1
        elif player == 1:
            print('PERDEU! PONTO PRO PC (PAPEL)         | VOCE: SPOCK.')
            cont_pc += 1
        elif player == 2:
            print('EMPATE! AMBOS ESCOLHERAM PAPEL')
        elif player == 3:
            print('GANHOU! PONTO PRO PLAYER (LAGARTO)   | PC: PAPEL.')
            cont_player += 1
        else:
            print('GANHOU! PONTO PRO PLAYER (TESOURA)   | PC: PAPEL.')
            cont_player += 1
    elif pc == 3: # lagarto
        if player == 0:
            print('GANHOU! PONTO PRO PLAYER (PEDRA)     | PC: LAGARTO.')
            cont_player += 1
        elif player == 1:
            print('PERDEU! PONTO PRO PC (LAGARTO)       | VOCE: SPOCK.')
            cont_pc += 1
        elif player == 2:
            print('PERDEU! PONTO PRO PC (LAGARTO)       | VOCE: PAPEL.')
            cont_pc += 1
        elif player == 3:
            print('EMPATE! AMBOS ESCOLHERAM LAGARTO')
        else:
            print('GANHOU! PONTO PRO PLAYER (TESOURA)   | PC: LAGARTO.')
            cont_player += 1
    else: # tesoura
        if player == 0:
            print('GANHOU! PONTO PRO PLAYER (PEDRA)     | PC: TESOURA.')
            cont_player += 1
        elif player == 1:
            print('GANHOU! PONTO PRO PLAYER (SPOCK)     | PC: TESOURA.')
            cont_player += 1
        elif player == 2:
            print('PERDEU! PONTO PRO PC (TESOURA)       | VOCE: PAPEL.')
            cont_pc += 1
        elif player == 3:
            print('PERDEU! PONTO PRO PC (TESOURA)       | VOCE: LAGARTO.')
            cont_pc += 1
        else:
            print('EMPATE! AMBOS ESCOLHERAM TESOURA')
    print()
    if cont_pc == 3 or cont_player == 3:
        break
if cont_pc == 3:
    print(f'PC GANHOU!')
else:
    print('VOCE GANHOU!')
