# JOGO DO ADIVINHA.

from random import randint

tentativas = 0
x = randint(1, 10)
acertou = False
while not acertou:
    r = int(input('ADIVINHE O NÚMERO DE 1 A 10: '))
    tentativas += 1
    if r == x:
        print(f'PARABÉNS, ACERTOU EM {tentativas} TENTATIVA(S).')
        acertou = True
