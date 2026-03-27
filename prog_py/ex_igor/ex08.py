# CRAPS.

from random import randint

jogo = True
rodada = num = soma = 0
while jogo:
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    soma = dado1 + dado2
    if rodada == 0:
        if soma == 7 or soma == 11:
            print(f'SEUS DADOS FORAM [{dado1, dado2}] | GANHOU POR SER UM NATURAL')
            jogo = False
        elif soma == 2 or soma == 3 or soma == 12:
            print(f'SEUS DADOS FORAM [{dado1, dado2}] | PERDEU')
            jogo = False
        elif soma in [4, 5, 6, 7, 8, 9, 10]:
            rodada += 1
            num = dado1
            print(f'SEUS DADOS FORAM [{dado1, dado2}] | PROXIMA RODADA POR "PONTO"')
            input('PRESSIONE "ENTER" PARA CONTINUAR')
    else:
        if soma == num:
            print(f'SEUS DADOS FORAM [{dado1, dado2}] | GANHOU PELO "PONTO"')
            jogo = False
        elif soma == 7:
            print(f'SEUS DADOS FORAM [{dado1, dado2}] | PERDEU PELO "PONTO" 7')
            jogo = False
        else:
            print(f'SEUS DADOS FORAM [{dado1, dado2}] | PROXIMA RODADA')
            input('PRESSIONE "ENTER" PARA CONTINUAR')
