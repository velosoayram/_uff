# JOKENPO (MELHOR DE TRÊS).

from random import randint

cont1 = cont2 = 0
ganhou = False
while not ganhou:
    pc = randint(1, 3)
    pr = int(input('JO-KEN-PO!\n1 - PEDRA\n2 - PAPEL\n3 - TESOURA\nSUA ESCOLHA: '))
    if pc == 1:
        if pr == 1:
            print(f'VOCÊ: PEDRA\nPC: PEDRA\nEMPATE!')
        elif pr == 2:
            print(f'VOCÊ: PAPEL\nPC: PEDRA\nGANHOU!')
            cont1 += 1
        else:
            print(f'VOCÊ: TESOURA\nPC: PEDRA\nPERDEU!')
            cont2 += 1
        print()
    elif pc == 2:
        if pr == 1:
            print(f'VOCÊ: PEDRA\nPC: PAPEL\nPERDEU!')
            cont2 += 1
        elif pr == 2:
            print(f'VOCÊ: PAPEL\nPC: PAPEL\nEMPATE!')
        else:
            print(f'VOCÊ: TESOURA\nPC: PAPEL\nGANHOU!')
            cont1 += 1
        print()
    else:
        if pr == 1:
            print(f'VOCÊ: PEDRA\nPC: TESOURA\nGANHOU!')
            cont1 += 1
        elif pr == 2:
            print(f'VOCÊ: PAPEL\nPC: TESOURA\nPERDEU!')
            cont2 += 1
        else:
            print(f'VOCÊ: TESOURA\nPC: TESOURA\nEMPATE!')
        print()
    if cont1 == 3 or cont2 == 3:
        if cont1 == 3:
            print('SIM, VOCÊ VENCEU!')
        else:
            print('É RAPAZ, PERDEU!')
        ganhou = True
