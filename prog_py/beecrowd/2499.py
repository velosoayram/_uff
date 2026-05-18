# TRIÂNGULO INTERNO.

while True:

    s, n, m = map(int, input().split())
    if s == n == m == 0:
        break
    c1, c2, c3 = map(int, input().split())
    numerador = s * abs(c2 - c3) * c1
    denominador = (m + 1) * (n + 1)
    resultado = numerador // denominador
    print(resultado)
