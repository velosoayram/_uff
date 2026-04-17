# FROTA DE TÁXI

valor = input().split()
vA, vG, rA, rG = float(valor[0]), float(valor[1]), float(valor[2]), float(valor[3])
if vA == vG:
    if rG >= rA:
        print('G')
    else:
        print('A')
else:
    if vA < vG:
        x = vG/vA
        if rA * x > rG:
            print('A') 
        else:
            print('G')
    else:
        x = vA/vG
        if rG * x >= rA:
            print('G')
        else:
            print('A')
