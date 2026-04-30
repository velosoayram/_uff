# PIVOTEAMENTO DE LISTA.

def pivoteia(l, p):

    """
    Função que retorna listas com números: menores, iguais e maiores que o pivô
    """

    menor, igual, maior = [], [], []
    for x in l:
        if x < p:
            menor.append(x)
        elif x == p:
            igual.append(x)
        else:
            maior.append(x)
    saida = menor, igual, maior
    return saida


pivo = 10
lista = [9, 3, 5, 7, 2, 5, 8]
print(pivoteia(lista, pivo))
