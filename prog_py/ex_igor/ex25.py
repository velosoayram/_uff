# INTERCALAÇÃO DE LISTAS ORDENADAS.

def intercala(a, b):

    """
    Função que intercala valores sequenciais de duas listas.
    """

    l = []
    c = i = 0
    while c < int((len(a) + len(b))/2):
        l.append(a[i])
        l.append(b[i])
        c += 1
        i += 1
    if (len(a) + len(b)) % 2 != 0:
        if len(a) > len(b):
            l.append(a[(i)])
        else:
            l.append(b[(i)])
    l = sorted(l)
    return l


l1 = [1, 3, 5, 7]
l2 = [2, 4, 8, 6]
print(intercala(l1, l2))
