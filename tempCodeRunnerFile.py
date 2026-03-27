n1, n2, n3 = int(input('N1: ')), int(input('N2: ')), int(input('N3: '))
if n1 + n2 == n3:
    print('soma')
if n1 + n3 == n2:
    print('soma')
if n2 + n3 == n1:
    print('soma')
else:
    if n1 * n2 == n3 or n1 * n3 == n2 or n2 * n3 == n1:
        print('multi')
    else:
        if (n1 + n2 + n3) % 2 == 0:
            print('par')
        else:
            print('impar')
