/*(5) Implemente um programa que, infinitamente, receba como parâmetro de entrada um número n e retorne todos os primos menores ou iguais a n. Seu programa para quando n < 2.*/

#include <stdio.h>
#include <math.h>
int primo(int n) {

    for (int i = 2; i < n; i++) {
        if (n % i == 0) return 0;
    }

    return 1;
}


int main(void) {

    int n;

    while(1) {

        printf("DIGITO PRIMO LIMITE: ");
        scanf("%d", &n);
        if (n < 2) break;

        for (int i = 2; i <= n; i++) {
            if (primo(i)) printf("%d\n", i);
        }

    }

    printf("FIM DO PROGRAMA.");

    return 0;
}
