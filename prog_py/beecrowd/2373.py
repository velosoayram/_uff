# GARÇOM.

n, counter = int(input()), 0
for x in range(n):
    l, c = map(int, input().split())
    if l > c:
        counter += c
print(counter)
