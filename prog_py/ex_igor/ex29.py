# FUNÇÃO PRODUTÓRIO.

# faça uma função produtorio que multiplica todos elementos de uma lista. Caso a lista esteja vazia, retorne 1.
# Exemplo: produtorio([2,3,2]) retorna 12

def produtorio(lista):

    if len(lista) == 0:

        return 1

    return lista[0] * produtorio(lista[1:])

    
lista = [2, 3, 2]
print(produtorio(lista))
