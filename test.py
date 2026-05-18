# from random import randint
# from sys import maxsize

# vetor = [randint(1, 100) for _ in range(100)]
# media = sum(vetor) / 100
# dif, menor = 0, maxsize



# if media in vetor:
#     print(f'VETOR: {vetor}\nMEDIA: {media}\nVALOR MAIS PROX: {menor}')
# else:
#     for x in vetor:
#         dif = abs(x - media)
#         if dif < menor:
#             menor = x
#     print(f'VETOR: {vetor}\nMEDIA: {media}\nVALOR MAIS PROX: {menor}')


from random import randint
from math import trunc
from sys import maxsize

vetor = [randint(1, 100) for _ in range(100)]
media = trunc(sum(vetor) / 100)
dif = maxsize

if media in vetor:
    print()

else:
    menor = 0
    for x in vetor:
        if x > menor:
            dif =
        else:
            dif =