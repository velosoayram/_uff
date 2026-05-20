# HUAAUHAHHUAHAU. (teste)

vogais, ordem, risada = ['a', 'e', 'i', 'o', 'u'], [], input()
for letra in risada:
    if letra in vogais:
        ordem.append(letra)
ordem = ''.join(ordem)
ordem_dec = ordem[::-1]
print('S' if ordem == ordem_dec else 'N')
