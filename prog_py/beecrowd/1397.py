# JOGO DO MAIOR.

n = int(input())
while n != 0:
    pont_a = pont_b = 0
    for x in range(n):      
        a, b = map(int, input().split())
        if a > b:
            pont_a += 1
        elif a < b:
            pont_b += 1
    print(f'{pont_a} {pont_b}')
    n = int(input())
