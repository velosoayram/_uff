# BUBBLE SORT: é um tipo de ordenação puramente didático já que seu desempenho apresenta uma complexidade 
# quadrática O(n^2) de desempenho em relaçao ao tempo, logo, não é tão interessante para aplicações reais.

# possui o nome que possui pois sua analogia é de itens que são organizados como bolhas num aquário, flutuam para cima (fim do vetor).
# é com base na comparação de um elemento e do seu vizinho que o bubble sort funciona.

# itera sobre um vetor inteiro a fim de organizá-lo, comparando seus pares.

def bubble_sort(lista):

    n = len(lista) # o número de elementos da lista.

    for i in range(n): # o loop que aplicará o código para cada elemento da lista.

        for j in range(0, n - i - 1): # o loop que iterativamente irá acessar os elementos pares vizinhos até sua posição final.

            # o (n - 1) serve para que não tenhamos index out of range, já que se o len() = 7, uma lista´vai de 0 a 6.
            # o (- i) é a inteligência do código que garante que termos já organizados não sejam comparados novamente, como se fosse range(qtd - passos_dados).

            if lista[j] > lista[j+1]: # se o termo for maior que o sucessor.

                lista[j], lista[j+1] = lista[j+1], lista[j] # inverte a posição deles.

            # então o código anda com o índice e compara o mesmo elemento que mudou de posição com um novo sucessor.

    return lista


lista = [9, 8, 10, 5, 2, -32, -322]
print(bubble_sort(lista))


# BUBBLE OTIMIZADO:
