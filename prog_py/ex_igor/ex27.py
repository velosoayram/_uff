# INTERSEÇÃO DE LISTAS.

def intersecao(l1, l2):
    
    """
    Função que pega apenas os elementos que aparecem em ambas as listas.
    """

    resultado = []
    for x in l1:
        if x in l2:
            resultado.append(x)
    return resultado


l1, l2 = [1, 2, 3, 4, 5], [3, 5, 7, 9, 2]
print(intersecao(l1, l2))
