
# 1) Interpretar e traduzir para Python a sequência de comandos em Português a seguir:

'''
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

# 2) Faça um programa em Python que:

'''
a) Escreva um programa que permita que o usuário indique um número de inteiros “n” a serem
lidos (entre 1 e 30). Após a leitura dos “n” números, escreva na tela a média, a soma, o produto,
o menor valor e o maior valor.
'''

'''
b) Faça um programa para construir a tabela de multiplicação de números de 1 a 10 (ex.: 1 x 1 = 1,
1 x 2 = 2, ....,2 x 1 = 2, 2 x 2 = 4, ...., etc.).
'''

'''
c) gerar os cinquenta primeiros termos da série: 1 + N, 5 * N, 9 + N, 13 * N, ..., onde N é um valor
lido.
'''

'''
d) determinar todos os números de 3 algarismos, cujas somas dos cubos dos algarismos sejam
iguais ao próprio número. Exemplo: 153 = 1**3 + 5**3 + 3**3.
'''

'''
e) Um número inteiro é considerado triangular se este for o produto de 3 números inteiros
consecutivos, como, por exemplo, 120 = 4 x 5 x 6. Elabore um programa que, após ler um
número n do teclado, verifique se n é triangular.
'''

'''
f) Escreva um programa que imprime na tela os n primeiros números perfeitos. Um número
perfeito é aquele que é igual à soma dos seus divisores (tirando ele mesmo). Por exemplo, 6 = 1
+ 2 + 3 é perfeito.
'''

'''
g) Suponha que um jogador A de PokemonGO tenha 800 pokemons com uma taxa de anual de
crescimento/captura de 3% e que o jogador B tem 2000 pokemons com uma taxa de
crescimento/captura de 1.5%. Faça um programa que calcule e retorne o número de anos
necessários para que o jogador A ultrapasse ou iguale o número de pokemons do jogador B,
mantidas as taxas de crescimento.
'''

'''
h) Fazer um programa que lê n números inteiros do teclado, e no final informa se os números lidos
estão ou não em ordem crescente.
Dica: guarde o número anterior gerado, se em alguma iteração o número fornecido atual for menor
que o número anterior, a ordem não é crescente.
'''

'''
3) Escreva um programa para gerar dois valores aleatórios inteiros “x” e “y” entre 1 e 100, que
representam o poder e a resistência de uma carta de Magic (para gerar o número aleatório usar randint).
Após isso, deve-se gerar a seguinte mensagem: “quanto é o poder x multiplicado pela resistencia y da
carta ?”, substituindo os números gerados por “x” e “y”. Depois da mensagem, deve ser lida uma resposta
do teclado e deve ser exibido uma mensagem indicando acerto ou erro. O programa deve implementar um
laço que obrigue o jogador a acertar pelo menos três vezes a resposta'''
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

'''
5) Faca um programa que imprima os N (inteiro fornecido pelo usuário) primeiros números da série do
Kirito A série inicia com os números 2,2, 3 e 3, e cada número posterior equivale a diferença entre a soma
dos 2 números anteriores multiplicado por 2, e a multiplicação dos 2 números antes destes anteriores (ex:
o próximo número da série eh (2*(3+3))-(2*2)=8). No fim, pergunte se o usuário quer entrar com outro N
e repetir o processo.
'''

'''
6) Calcule a soma da série S de Saitama, dado valores inteiros n e m fornecidos pelo usuário. No fim,
pergunte se o usuário quer repetir a operação.
'''

'''
7) Faça um jogo de pedra, papel, tesoura, spock e lagarto (de onde vem isso?), onde o jogador e o
computador escolhem entre “0-pedra 1-spock 2-paper 3-lagarto 4-tesoura” (a jogado do computador é
aleatória). Ganha o jogo quem vencer 3 vezes primeiro (As regras de vitória estão descritas na figura
abaixo).
'''