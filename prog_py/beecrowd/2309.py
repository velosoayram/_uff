# TRUCO.

n = int(input())
seq = {4:1, 5:2, 6:3, 7:4, 11:6,
       12:5, 13:7, 1:8, 2:9, 3:10}
placar = [0, 0]
for x in range(n):
    adal = bern = 0     
    a1, a2, a3, b1, b2, b3 = map(int, input().split())
    if seq[a1] >= seq[b1]:
        adal += 1
    else: bern += 1
    if seq[a2] >= seq[b2]:
        adal += 1
    else: bern += 1
    if seq[a3] >= seq[b3]:
        adal += 1
    else: bern += 1
    if adal > bern: placar[0] += 1
    else: placar[1] += 1
print(placar[0], placar[1])
