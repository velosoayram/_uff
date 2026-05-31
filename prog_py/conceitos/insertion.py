# INSERTION SORT: menos pior que o bubble, mas ainda com nível de complexidade quadrático, seu uso
# tem maior serventia caso a ordenação pré-disponha de um vetor semi-organizado, tornando a iteração
# mais eficiente para o código.

# funciona com base na varredura do vetor, inserindo o valor no lugar apropriado ao fazer comparações.

def insertion_sort(lista):

    for i in range(1, len(lista)):

        chave = lista[i]

        j = i - 1

        while j >= 0 and lista[j] > chave:

            lista[j + 1] = lista[j]
            
            j -= 1
            
        lista[j + 1] = chave
        
    return lista


lista = [9, 8, 10, 5, 2, -32, -322]
print(insertion_sort(lista))
