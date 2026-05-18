# MARATONA.

n, m = map(int, input().split())
pontos = list(map(int, input().split()))
flag = True
if (42195 - pontos[-1]) > m: flag = False
else:
    for i in range(n-1):
        dif = pontos[i+1] - pontos[i]
        if dif > m:
            flag = False
            break
print('S' if flag else 'N')
