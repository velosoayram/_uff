# DISTÂNCIA DE MANHATTAN

cood = input().split()
xm, ym, xr, yr = int(cood[0]), int(cood[1]), int(cood[2]), int(cood[3])
print(abs(xr-xm) + abs(yr-ym))
