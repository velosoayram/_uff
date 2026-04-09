'''
7) Faça um jogo de pedra, papel, tesoura, spock e lagarto (de onde vem isso?), onde o jogador e o
computador escolhem entre “0-pedra 1-spock 2-paper 3-lagarto 4-tesoura” (a jogada do computador é
aleatória). Ganha o jogo quem vencer 3 vezes primeiro (As regras de vitória estão descritas na figura
abaixo).
'''

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
