# SOMA DE FRAÇÕES.

a, b, c, d = map(int, input().split())
n1 = den = mdc = b * d
n2 = num = (den // b * a) + (den // d * c)
while num % den != 0:
    num, den = den, num % den
    mdc = den
print(n2//mdc, n1//mdc)
