# BANCO IMOBILIÁRIO.

i, n = map(int, input().split())
d = e = f = i
for x in range(n):
    resp = input().split()
    if resp[0] == 'C':
        if resp[1] == 'D':
            d -= int(resp[-1])
        elif resp[1] == 'E':
            e -= int(resp[-1])
        else:
            f -= int(resp[-1])
    elif resp[0] == 'V':
        if resp[1] == 'D':
            d += int(resp[-1])
        elif resp[1] == 'E':
            e += int(resp[-1])
        else:
            f += int(resp[-1])
    else:
        if resp[1] == 'D' and resp[2] == 'E':
            d += int(resp[-1])
            e -= int(resp[-1])
        elif resp[1] == 'D' and resp[2] == 'F':
            d += int(resp[-1])
            f -= int(resp[-1])
        elif resp[1] == 'E' and resp[2] == 'D':
            e += int(resp[-1])
            d -= int(resp[-1])
        elif resp[1] == 'E' and resp[2] == 'F':
            e += int(resp[-1])
            f -= int(resp[-1])
        elif resp[1] == 'F' and resp[2] == 'D':
            f += int(resp[-1])
            d -= int(resp[-1])
        elif resp[1] == 'F' and resp[2] == 'E':
            f += int(resp[-1])
            e -= int(resp[-1])
print(d, e, f)
