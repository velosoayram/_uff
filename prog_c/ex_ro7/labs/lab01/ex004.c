/*(4) Implemente um programa que, infinitamente, leia um número n e retorne todos os seus divisores. Esse programa para quando n < 2;*/

#include <stdio.h>
#include <math.h>
int divisores(int n) {

    for (int i = 1; i <= n; i++) {

        if (n % i == 0) {
            printf("%d\n", i);
        }
    }

    return 0;
}


int main(void) {

    int n;

    while (1) {

        printf("DIGITE O NO: ");
        scanf("%d", &n);
        if (n < 2) break;
        else divisores(n);
    }

    printf("FIM DO PROGRAMA\n");
}
