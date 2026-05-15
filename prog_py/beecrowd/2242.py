# HUAAUHAHHUAHAU. (teste)

# c, vogais, risada = 0, ['a', 'e', 'i', 'o', 'u'], input()
# for letra in risada:
#     if letra in vogais: c += 1
# if c >= (len(risada)//2): print('S')
# else: print('N')

# HUAAUHAHHUAHAU.

vogais, ordem, risada = ['a', 'e', 'i', 'o', 'u'], [], input()
for letra in risada:
    if letra in vogais:
        ordem.append(letra)
ordem = ''.join(ordem)
ordem_dec = ordem[::-1]
print('S' if ordem == ordem_dec else 'N')
