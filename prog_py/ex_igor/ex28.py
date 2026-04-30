# FILTRAGEM DE NÚMEROS PRIMOS.

def eh_primo(n):

    """
    Função que identifica números primos
    """

    cont = x = 0
    while cont <= 2 and n not in [0, 1]:
        if x > (n/2):
            return 'primo'
        if n % 2 == 0:
            cont += 1
        x += 1
    else:
        return 'não primo'
    

n = int(input())
print(eh_primo(n))
