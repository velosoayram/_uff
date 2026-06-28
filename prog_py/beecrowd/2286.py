# PAR OU ÍMPAR.

vencedores = []
while True:
    n = int(input())
    if n == 0:
        break
    temp = []
    p1, p2 = str(input()), str(input())
    for x in range(n):
        r1, r2 = map(int, input().split())
        if (r1 + r2) % 2 == 0:
            temp.append(p1)
        else:
            temp.append(p2)
    vencedores.append(temp)
for y in range(len(vencedores)):
    print(f'Teste {y+1}')
    for z in vencedores[y]:
        print(z)
    print()

# PAR OU ÍMPAR 2.0

cont = 1
n = int(input())
while n != 0:
    p1, p2 = str(input()), str(input())
    print(f'Teste {cont}')
    for x in range(n):
        num0, num1 = map(int, input().split())
        if (num0 + num1)% 2 == 0:
            print(p1)
        else:
            print(p2)
    print()
    cont += 1
    n = int(input())
