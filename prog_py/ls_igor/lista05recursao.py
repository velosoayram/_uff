'''
7) Implemente uma funcao recursiva “eh_palindromo” que recebe um string e retorna
verdadeiro, caso seja palindromo, ou falso, caso contrário.

Exemplos:
eh_palindromo(“ana”) retorna True
eh_palindromo(“radar”) retorna True
eh_palindromo(“python”) retorna False

Dica I: Considere que um string vazio é palindromo.
Dica II: Considere parametros auxiliares na funcao recursiva, como o inicio de fim do string: eh_palindromo(s, inicio, fim), tal que inicio=0 e fim=len(s)-1
Dica III: Teste a função para palavras de tamanho par e de tamanho ímpar.
'''

def eh_palindromo(palavra, inicio = 0, fim = None):

    if inicio == 0: # caso a primeira recursão, definimos o fim como o último índice da palavra escolhida.
        fim = len(palavra) - 1

    if inicio >= fim: 
        return True
    
    # quando o índice chegar ao valor do final, significa que, durante as recursões, diminuímos
    # a ponto de iterarmos sobre a mesma letra e, caso isso, uma única letra é palíndromo dela mesma.
    # então retornamos True.

    if palavra[inicio] != palavra[fim]:
        return False
    
    # basicamente, se a letra do ínicio for diferente da do final, já não é palíndromo
    # então retorna False.

    return eh_palindromo(palavra, inicio + 1, fim - 1)

    # aqui ocorre as trocas de índices, diminuindo a palavra durante as recursões.
    # ex: 'radar' -> 'ada' -> 'd' : palíndromo.



def eh_palindromo2(palavra):

    # executa a mesma função que a anterior, mas usando slicing (quis inventar sem parâmetros auxiliares).

    if palavra[0] != palavra[-1]:
        return False
    
    if len(palavra) <= 1:
        return True
    
    # ao invés de compararmos por índices, fazemos por len() da palavra, já que durante as recursões estamos iterando sobre 
    # cópias reduzidas da mesma palavra, então se a cópia chegar ao ponto de ter len() = 1, significa que é um palíndromo.

    return eh_palindromo2(palavra[1:-1])

    # as cópias recursivas.

x = input()
print(eh_palindromo2(x)) 


'''
8) Faça uma função recursiva soma_bignum(s1, s2) que efetua a soma de dois
números gigantes s1 e s2 representados como strings de decimais como little endian,
ou seja, começando dos números menores ao invés dos maiores (o contrário do que
estamos acostumados).

Exemplos:
soma_bignum("321", "490") retorna "3601"
# pois 123 + 940 = 1063, em little endian: "3601"
soma_bignum("9", "1") retorna "01"
# pois 9 + 1 = 10, em little endian: "01"
soma_bignum("5", "7"), retorna "21”
soma_bignum("321", "49") retorna "712"

Dica I: considere que os números nunca são vazios
Dica II: considere parametros auxiliares na função recursiva, como um índice i
(inicialmente zero), e um parâmetro “vaium” (inicialmente zero)
Dica III: comece por strings que tenham um mesmo tamanho, depois expanda a solução
para strings com tamanhos distintos
'''

def soma_bignum(s1 = str, s2 = str, i = 0, vaium = 0):

    if i >= len(s1) and i >= len(s2) and vaium == 0:
        return ''
    
    # as recursões só ocorrem até onde os índices são possíveis e não há excedente (vaium = 0).

    digito1 = int(s1[i]) if i < len(s1) else 0
    digito2 = int(s2[i]) if i < len(s2) else 0

    # os dígitos são definidos enquanto os índices são menores que o len() das strings,
    # caso um dígito não seja possível, ele se tranforma em zero, possibilitando a soma do mesmo jeito.

    soma = digito1 + digito2 + vaium
    
    # as somas são os digitos acima e o excedente.

    atual  = soma % 10

    # nosso dígito da recursão atual é definido pelo resto da divisão de 10, já que os digitos possíveis numa casa decimal
    # é o intervalo de 0 a 9.

    vaium_novo = soma // 10

    # caso haja excedente, ele será considerado para recursões futuras num novo argumento.

    return str(atual) + soma_bignum(s1, s2, (i + 1), vaium_novo) 

    # as recursões levam o digíto atual concatenados ao resultados dos dígitos futuros.
    # ao chegar no caso base, os números são enfim concatenados da direita para a esquerda.

s1, s2, i, vaium = '9', '1', 0, 0
print(soma_bignum(s1, s2, i, vaium))


'''
9) Considere a função de ordem superior mapear, definida no material de aula.

9.a) Explique o que acontece na seguinte expressão: dados = mapear(int, input(“digite uma lista de entrada:”).split())
9.b) Escreva uma função media(a,b,c), que calcula a média entre 3 elementos
9.c) Escreva uma função de ordem superior chamada suavizar, que recebe uma função de entrada e uma lista, aplicando a função na lista a cada três elementos consecutivos (exceto o primeiro e o último)

Exemplos:
print(suavizar(media, [1, 3, 7, 9, 4]))
# [1, 3.666, 6.333, 6.666, 4]
# Pois, (1+3+7)/3 = 3.666, (3+7+9)/3=6.333, (7+9+4)/3=6.666 print(suavizar(media, [10, 20, 30, 40, 50]))
# [10, 20.0, 30.0, 40.0, 50]
'''

# dada a função mapear abaixo:

def mapear(f, lista):

    resultado = []
    for x in lista:
        resultado.append(f(x))
    return resultado

# 9.a)

dados = mapear(int, input('digite uma lista de entrada: ').split())

# uma variavel dados recebe a execução da função mapear() criada, passando dois argumentos, a função int() e a lista,
# que é gerada ao digitar números no input() e então subdividida em partes de acordo com o espaço entre os números
# digitados, com a ajuda do método split() que executa esse papel.

# 9.b)

def media(a, b, c):

    return round((a + b + c) / 3, 3)

# a função média

# 9.c)

def suavizar(f, lista):

    resultado = lista[:]
    
    # aqui precisamos criar uma lista de cópia, já que iremos manipular apenas alguns valores seletos da lista original,
    # sem alteração do primeiro e último termo.

    for i in range(1, len(lista) - 1):
        resultado[i] = f(lista[i-1], lista[i], lista[i+1])

    # resultado[i] é o equivalente ao intervalo dos números de lista, sem os seus extremos.
    # lista[i-1] garante que iremos pegar o primeiro extremo para 'suavizar' ele.
    # lista[i+1] garante o mesmo para a extremidade final.
    
    return resultado # aqui retornamos a lista final.
        
        
print(suavizar(media, [1, 3, 7, 9, 4]))
