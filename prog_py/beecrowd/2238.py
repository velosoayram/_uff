# DIVISORES.

a, b, c, d = map(int, input().split())
candidatos, flag = list(), False
for i in range(1, int(c**(1/2)) + 1):
    if c % i == 0:
        candidatos.append(i)
        if i != c // i:
            candidatos.append(c // i)
for i in sorted(candidatos):
    if i % a == 0 and i % b != 0 and d % i != 0:
        print(i)
        flag = True
        break
if not flag: print(-1)
