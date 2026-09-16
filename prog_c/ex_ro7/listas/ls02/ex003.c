/*Q3) Implemente um programa que, infinitamente, receba, como parâmetro de entrada, um número
n e retorne a representação binária de n. Por exemplo, se n é igual a 12, a resposta deste
programa deve ser “1100”. Seu programa para quando n for menor que zero.*/

// versão iterativa:

#include <stdio.h>
#include <math.h>
int main(void) {

    while(1) {

        int n, q, b = 0;

        scanf("%d", &n);

        if (n < 0) break;

        int x = n;

        for (int i = 0; i <= n; i++) {

            q = x % 2;
            x /= 2;
            b += q * pow(10, i);

        }

        printf("%d | binary: %d\n", n, b);
    }

    return 0;
}

// versão vetor:
