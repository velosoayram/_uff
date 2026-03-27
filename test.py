centavos = int(input())
moeda100 = centavos//100
moeda050 = (centavos - moeda100 * 100) // 50
moeda025 = ((centavos - moeda100 * 100) - moeda050 * 50) // 25
moeda001 = (((centavos - moeda100 * 100) - moeda050 * 50) - moeda025 * 25) // 1
print(f'MOEDAS 1,00 R$: {moeda100}\n'
f'MOEDAS 0.50 R$: {moeda050}\n'
f'MOEDAS 0.25 R$: {moeda025}\n'
f'MOEDAS 0.01 R$: {moeda001}')


centavos = int(input())
moeda100 = centavos//100
moeda050 = centavos%100//50
moeda025 = centavos%100%50//25
moeda001 = centavos%100%50%25//1
print(f'MOEDAS 1,00 R$: {moeda100}\n'
f'MOEDAS 0.50 R$: {moeda050}\n'
f'MOEDAS 0.25 R$: {moeda025}\n'
f'MOEDAS 0.01 R$: {moeda001}')