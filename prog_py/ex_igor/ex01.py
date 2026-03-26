# OBTER OS DIVISORES DE UM NÚMERO n.
 
n = int(input('DIGITE UM NÚMERO: '))
for x in range(n):
    if x == 0:
        pass
    elif n % (x+1) == 0:
        print(x+1)
