# CATÁLOGO DE LIVROS.

p = sorted(list(map(int, input().split()))[1:], reverse=True)
m = sorted(list(map(int, input().split()))[1:], reverse=True)
f = sorted(list(map(int, input().split()))[1:], reverse=True)
q = sorted(list(map(int, input().split()))[1:], reverse=True)
b = sorted(list(map(int, input().split()))[1:], reverse=True)

todas_somas = []

k = int(input())

for precos_a in p:
    for precos_b in m:
        for precos_c in f:
            for precos_d in q:
                for precos_e in b:

                    soma = precos_a + precos_b + precos_c + precos_d + precos_e
                    todas_somas.append(soma)

print(sum(sorted(todas_somas, reverse=True)[:k]))
