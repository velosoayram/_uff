# XADREZ

l, c = int(input()), int(input())
if c % 2 == 0 and l % 2 != 0:
    print(0)
elif c % 2 == 0 and l % 2 == 0:
    print(1)
elif c % 2 != 0 and l % 2 != 0:
    print(1)
else:
    print(0)
