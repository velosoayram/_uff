# OVERFLOW.

n = int(input())
eq = input().split()
if eq[1] == '*':
    print('OVERFLOW') if int(eq[0]) * int(eq[-1]) > n else print('OK')
else:
    print('OVERFLOW') if int(eq[0]) + int(eq[-1]) > n else print('OK')
