# ALUNOS IRREGULARES.

PROG1, PROG2, PROG3, irregular = [], [], [], []
for a in range(5):
    PROG1.append(int(input()))
for b in range(7):
    PROG2.append(int(input()))
for c in range(7):
    PROG3.append(int(input()))
for x in PROG1:
    if x in PROG2 and x in PROG3:
        irregular += [x]
for y in irregular:
    print(f'aluno {y} irregular')
print(f'total = {len(irregular)}')
