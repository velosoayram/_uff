# FUNÇÃO CONTAR.

# faça uma função “contar” que recebe um valor e uma lista, e retorna quantos vezes o valor aparece na lista
# Exemplo: contar(3, [1,3,3,4,3,2,5,3]) retorna 4
# Dica: funções recursivas podem ter parâmetros auxiliares, caso necessário, ou até mesmo invocar funções auxiliares.

def contar(valor, lista, i=0, resultado=0):

    if i == len(lista):

        return resultado
    
    if valor == lista[i]:

        resultado += 1

    return contar(valor, lista, i + 1, resultado)


print(contar(5, [1, 3, 3, 4, 3, 2, 5, 3, 5]))
