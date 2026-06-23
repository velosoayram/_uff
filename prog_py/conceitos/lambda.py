# LAMBDA.

lista = [[900, 'Bruno'], [489, 'jOse'], [98, 'FabriciO']]

correcao = sorted([[nome.capitalize(), pont] for pont, nome in lista], key=lambda item: item[1])

print(correcao)
print(lista)