# SUPER PRIMOS: ATIVAR!

primos = [2, 3, 5, 7]
while True:
    try:
        sentinela = 2
        n = int(input())
        while n < 2:
            print('Nada')
            n = int(input())
        for x in range(2, int(n**(1/2) + 1)):
            if n % x == 0:
                sentinela += 1
                break
        if sentinela > 2:
            print('Nada')
        else:
            flag = False
            palavra = str(n)
            for p in palavra:
                if int(p) not in primos:
                    flag = True
                    break
            if flag: print('Primo')
            else: print('Super') 
    except EOFError:
        break
