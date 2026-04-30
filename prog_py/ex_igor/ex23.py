# FUNÇÃO SOMA ÍMPAR EM ÍNDICE PAR.

def soma_par_impar(p):

    """
    Função de somar números ímpares dentro de posições pares do vetor.
    """

    if len(p) == 0:
        return
    soma = 0
    for x in range(len(p)):
        if x % 2 == 0 and p[x] % 2 != 0:
            soma += p[x]
    return soma


lista = [1,1,3,1,8,1]
print(lista)
print(soma_par_impar(lista))
