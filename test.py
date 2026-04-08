'''
4) Faça um programa que determina se dois valores inteiros e positivos A e B são “Bros” (dois números
inteiros são ditos “Bros”, caso não exista divisor comum aos dois números diferente de 1).
Dica: O método de Euclides é um dos algoritmos mais antigos (300 a.C.) e um dos mais
eficientes para calcular o Máximo Divisor Comum (M.D.C) de dois números inteiros
O algoritmo se baseia na seguinte propriedade:
MDC(A,B) = MDC(B, A%B)
que deve ser explorada iterativamente até que A%B seja 0 e B seja considerado o
MDC. Por exemplo, MDC(252,105) = MDC(105,42) = MDC(42,21) = 21, pois 42%21
é igual a zero. Portanto MDC(252,105) = 21.
'''