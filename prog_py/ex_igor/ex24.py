# NORMALIZAÇÃO DE NOTAS.

def normaliza(p):

    """
    Função de receber uma lista e retornar seus valores num intervalo de 0 a 1.
    """

    l = []
    mai, men = max(p), min(p) 
    for x in p:
        nota_normalizada = (x - men) / (mai - men)
        l.append(nota_normalizada)
    return l


lista = [50, 70, 100, 80, 60, 90]
print(lista)
print(normaliza(lista))
