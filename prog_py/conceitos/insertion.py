# INSERTION SORT: menos pior que o bubble, mas ainda com nível de complexidade quadrático O(n^2), seu uso
# tem maior serventia caso a ordenação pré-disponha de um vetor semi-organizado, tornando a iteração
# mais eficiente para o código.

# funciona com base na varredura do vetor, inserindo o valor no lugar apropriado ao fazer comparações entre "sub-listas".
# temos a lista organizada (elemento da esquerda para direita) e a desorganizada (elemento da direita para esquerda).

def insertion_sort(lista):

    for i in range(1, len(lista)): # começamos o range no índice 1, porque o primeiro elemento da sub-lista já está ordenado nele mesmo.

        chave = lista[i] # a chave sempre será o elemento atual da iteração.

        j = i - 1 # precisamos de um índice para o(s) elemento(s) anterior(es) ao atual.

        while j >= 0 and lista[j] > chave: # o loop roda enquanto houverem termos anteriores e maiores ao da chave, quando j = -1, o loop acaba.

            # quando o while não é executado, o insertion passa a ter uma complexidade linear O(n).

            lista[j + 1] = lista[j] # o termo atual da vez recebe o termo anterior da vez.

            j -= 1 # os termos recebem uma redução simultânea para que suas comparações ocorram com os demais, exceto quando j = -1.

        lista[j + 1] = chave # caso j = -1, (j + 1) ao fim do loop será o equivalente a 0, portanto: o primeiro termo da lista receberá o valor da chave.
                             # caso j != -1, mas o termo anterior seja menor ao da chave, entramos na sequência e o termo atual receberá o valor correto.

    return lista


lista = [9, 8, 10, 5, 2, -32, -322]
print(insertion_sort(lista))
