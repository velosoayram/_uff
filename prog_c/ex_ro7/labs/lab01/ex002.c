/*(2) Implemente um programa que, infinitamente, leia dois números x e y e retorne o MDC entre eles. Esse programa pára quando x,y ≤ 1;*/

#include <stdio.h>
#include <math.h>
int mdc(int n1, int n2) {

    int resultado, menor;

    if (n1 < n2) {
        menor = n1;
    } else menor = n2;

    for (int i = menor; i > pow(menor, (1/2)) ; i--) {

        if (n1 % i == 0 && n2 % i == 0) return i;

    }
}


int main(void) {

    int n1, n2, x;

    while (1) {

        scanf("%d %d", &n1, &n2);

        if (n1 <= 1 && n2 <= 1) break;
        else x = mdc(n1, n2);

        printf("%d\n", x);

    }

    printf("FIM DO PROGRAMA.");

    return 0;
}
