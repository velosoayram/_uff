# JOGO DO ADIVINHA (COM LIMITE DE TENTATIVAS).

from random import randint

tentativas = 0
x = randint(1, 10)
chances = 0
while chances < 3:
    r = int(input('ADIVINHE O NÚMERO DE 1 A 10: '))
    tentativas += 1
    chances += 1
    if r == x:
        print(f'PARABÉNS, ACERTOU EM {tentativas} TENTATIVA(S).')
        break
    elif chances == 3:
        print('YOU RUNNED OUT OF CHANCES')
    else:
        if r > x:
            print('O NÚMERO É MENOR')
        else:
            print('O NÚMERO É MAIOR')
