# TEMPERATURA LUNAR.

n, m = map(int, input().split())
teste = 0

while n != 0 and m != 0:

    medias, temperaturas = [], []

    teste += 1

    for temps in range(n):

        temperaturas.append(int(input()))  

    # TLE.
 
    # maior = menor = 0

    # for x in range(len(temperaturas) - m + 1):

    #     soma = 0

    #     for y in range(m):

    #         soma += temperaturas[x + y]

    #     medias.append(int(soma / m))

    # print(f'Teste {teste}\n{min(medias)} {max(medias)}\n')


    # SLIDING WINDOW - calcule o primeiro da sequência, siga somando o próximo e subtraindo o inicial.

    soma_atual = sum(temperaturas[:m])
    media_atual = maior = menor = int(soma_atual / m)

    for i in range(m, n):

        soma_atual = soma_atual + temperaturas[i] - temperaturas[i - m]
        media_atual = int(soma_atual / m)

        if media_atual > maior: maior = media_atual
        if media_atual < menor: menor = media_atual

    print(f'Teste {teste}\n{menor} {maior}\n')

    n, m = map(int, input().split())
