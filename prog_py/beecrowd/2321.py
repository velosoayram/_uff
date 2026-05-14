# DETECTANDO COLISÕES.

x0, y0, x1, y1 = map(int, input().split())
a0, b0, a1, b1 = map(int, input().split())
if x0 > a1 or x1 < a0 or y0 > b1 or y1 < b0:
    print(0)
else:
    print(1)
