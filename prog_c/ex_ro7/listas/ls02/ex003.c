/*Q3) Implemente um programa que, infinitamente, receba, como parâmetro de entrada, um número
n e retorne a representação binária de n. Por exemplo, se n é igual a 12, a resposta deste
programa deve ser “1100”. Seu programa para quando n for menor que zero.*/

// versão iterativa:

#include <stdio.h>
#include <math.h>
int main(void) {

    while(1) {

        int n, q, b = 0;

        printf("DIGITE UM No: ");
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

#include <stdio.h>
int main(void) {

    int n;

    while(1) {

        printf("DIGITE UM No: ");
        scanf("%d", &n);

        if (n < 0) break;

        if (n == 0) {
            
            printf("0 | binary: 0");
            printf("\n\n");
            continue;

        }

        int x = n;
        int binario[32];
        int i = 0;

        while(x > 0) {

            binario[i] = x % 2;
            x /= 2;
            i++;

        }

        printf("%d | binary: ", n);

        for (int j = i - 1; j >= 0; j--) {

            printf("%d", binario[j]);
        }

        printf("\n\n");

    }
    return 0;
}

// versão recursiva: