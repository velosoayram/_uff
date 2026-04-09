vencedores = []
while True:
    temp = []
    n = int(input())
    if n == 0:
        break
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
