# AUTORAMA. / wrong answer 5% / refazer.

# k, n, m = map(int, input().split())
# data = []
# for check in range(m):
#     point = list(map(str, input().split()))
#     if point[0] in data:
#         data[(data.index(point[0]) + 1)] += point[1]
#     else:
#         data.append(point[0])
#         data.append([point[1]])
# pares = [data[i:i+2] for i in range(0, len(data), 2)]
# podio = sorted(pares, key=lambda item: item[1], reverse=True)
# for x in range(len(podio)):
#     print(podio[x][0], end=' ')


# AUTORAMA.

k, n, m = map(int, input().split())
data = []
for x in range(n):
    data.append((x+1))
    data.append([0, 1, 0])
for tempo in range(m):
    carro, ponto = map(int, input().split())
    ind = data.index(carro)
    status = data[(ind+1)]
    if ponto == status[1]:
        status[0] += 1    # ganhos
        status[1] += 1    # proximo
        status[2] = tempo # ultimo checkpoint no tempo
        if status[1] > k: status[1] = 1
pares = [data[i:i+2] for i in range(0, len(data), 2)]
ordem = sorted(pares, key=lambda item: (-item[1][0], item[1][2]))
resultado = ' '.join([str(ordem[x][0]) for x in range(len(ordem))])
print(resultado)
