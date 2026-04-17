# CARTAS

cartas = input().split()
c1, c2, c3, c4, c5 = int(cartas[0]), int(cartas[1]), int(cartas[2]), int(cartas[3]), int(cartas[4])
if c1 < c2 < c3 < c4 < c5:
    print('C')
elif c1 > c2 > c3 > c4 > c5:
    print('D')
else:    
    print('N')
