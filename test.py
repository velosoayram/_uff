'''
7) Faça um programa que simule uma agenda telefônica onde o usuário informe os telefones
(inteiros) e você deverá inserir estes valores de forma ordenada uma lista. O usuário deve ser
capaz de inserir até 100 telefones. A cada número inserido, imprima a agenda.
Ex:
Insere 2211
Agenda=[2211]
Insere 923
Agenda=[923,2211]
Insere 1555
Agenda=[923,1555,2211]
'''

agenda = []
for a in range(100):
    num = int(input())
    agenda.append(num)
    agenda.sort()
    print(agenda)