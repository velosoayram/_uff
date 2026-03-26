# JOKENPO.

from random import randint

while True:
    pc = randint(1, 3)
    pr = int(input('JO-KEN-PO!\n1 - PEDRA\n2 - PAPEL\n3 - TESOURA\nSUA ESCOLHA: '))
    if pc == 1:
        if pr == 1:
            print(f'VOCÊ: PEDRA\nPC: PEDRA\nEMPATE!')
        elif pr == 2:
            print(f'VOCÊ: PAPEL\nPC: PEDRA\nGANHOU!')
            break
        else:
            print(f'VOCÊ: TESOURA\nPC: PEDRA\nPERDEU!')
    if pc == 2:
        if pr == 1:
            print(f'VOCÊ: PEDRA\nPC: PAPEL\nPERDEU!')
        elif pr == 2:
            print(f'VOCÊ: PAPEL\nPC: PAPEL\nEMPATE!')
        else:
            print(f'VOCÊ: TESOURA\nPC: PAPEL\nGANHOU!')
            break
    else:
        if pr == 1:
            print(f'VOCÊ: PEDRA\nPC: TESOURA\nGANHOU!')
            break
        elif pr == 2:
            print(f'VOCÊ: PAPEL\nPC: TESOURA\nPERDEU!')
        else:
            print(f'VOCÊ: TESOURA\nPC: TESOURA\nEMPATE!')
