# SLIDING WINDOW.

lista, soma = [1, 2, 3, 4, 5, 6, 7, 8], 0
intervalo = 4

primeira_soma = sum(lista[:intervalo]) # pega os índices de 0 a 3.
maior = menor = int(primeira_soma / intervalo)

for i in range(intervalo, len(lista)):

    primeira_soma = primeira_soma + lista[i] - lista[i - intervalo] # ínicio: i = 4 | subtração: 4 - 4 = 0  (lista[0], primeiro índice da sequência inicial).
    media = int(primeira_soma / intervalo)

    if media > maior: maior = media
    if media < menor: menor = media

print(menor, maior)
