# ETIQUETAS COLORIDAS.

R, G, B = int(input(), 16), int(input(), 16), int(input(), 16)
ng, nb = (R//G) * (R//G), (G//B) * (G//B)
print(hex(1 + ng + (ng * nb))[2:])
