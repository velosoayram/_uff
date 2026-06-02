# FUNÇÃO PERMUTAÇÃO. / refazer /

# 4) defina uma função que gera todas permutações:
# print(permutacoes("ab"))   # ['ab', 'ba']
# print(permutacoes("abc"))  # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

def fat(num: int):

    resultado = 1

    for n in range(2, num + 1):

        resultado *= n 

    return resultado


def permutacao(palavra: str, lista = []):

    if len(lista) == fat(len(palavra)):

        return lista
    
    lista.append(palavra)
    
    return permutacao(palavra[1:] + palavra[0], lista)

print(permutacao('abc'))
