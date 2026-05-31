# BUBBLE SORT: é um tipo de ordenação puramente didático já que seu desempenho apresenta uma complexidade 
# quadrática de desempenho em relaçao ao tempo, logo, não é tão interessante para aplicações reais.

# possui o nome que possui pois sua analogia é de itens que são organizados como bolhas num aquário, flutuam para cima (fim do vetor).
# é com base na comparação de um elemento e do seu vizinho que o bubble sort funciona.

# itera sobre um vetor inteiro a fim de organizá-lo, comparando seus pares.

def bubble_sort(lista):

    n = len(lista)

    for i in range(n):

        for j in range(0, n - i - 1):

            if lista[j] > lista[j+1]:

                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista


lista = [9, 8, 10, 5, 2, -32, -322]
print(bubble_sort(lista))


# BUBBLE OTIMIZADO:
