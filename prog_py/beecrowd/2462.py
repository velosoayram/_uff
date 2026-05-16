# VOO.

pa, cb, pb, ca = map(str, input().split())
pa = (int(pa[0:2]) * 60) + int(pa[3:5])
cb = (int(cb[0:2]) * 60) + int(cb[3:5])
pb = (int(pb[0:2]) * 60) + int(pb[3:5])
ca = (int(ca[0:2]) * 60) + int(ca[3:5])
delta_ab = (cb - pa) % 1440
delta_ba = (ca - pb) % 1440
tempo = ((delta_ab + delta_ba) % 1440 ) // 2
fuso = (delta_ab - tempo) // 60
if fuso > 12: fuso -= 24
elif fuso < -11: fuso += 24
print(tempo, fuso)