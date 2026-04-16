# VECTOR A.
 
vet, pos, semrep = [], [], []
for x in range(20):
    resp = int(input())
    if resp not in pos:
        semrep += [resp]
    vet += [resp]
    if resp > 0:
        pos += [resp]
print(f'vet    = {vet}\n'
      f'pos    =  {pos}\n'
      f'semrep = {semrep}')
