# INSTRUÇÕES DO ROBÔ.

testes = int(input())
for i in range(testes):
    p = 0
    m = []
    casos = int(input())
    for j in range(casos):
        coord = input()
        if coord == 'LEFT':
            p += -1
            m.append(coord)
        elif coord == 'RIGHT':
            p += 1
            m.append(coord)
        else:
            num = coord.split()
            num = (int(num[-1]) - 1)
            if m[num] == 'LEFT':
                p += -1
                m.append('LEFT')
            elif m[num] == 'RIGHT':
                p += 1
                m.append('RIGHT')
    print(p)
    