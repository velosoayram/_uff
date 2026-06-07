# MÁQUINA DE CAFÉ.

a1, a2, a3 = int(input()), int(input()), int(input())
possibilidades = [(a2 * 2) + ((a3 + a3) * 2), (a1 * 2) + (a3 * 2), (a2 * 2) + ((a1 + a1) * 2)]
print(min(possibilidades))
