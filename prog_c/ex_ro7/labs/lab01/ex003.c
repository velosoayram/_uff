/*(3) Implemente um programa que, infinitamente, leia um número n e retorne o n-ésimo termo da sequência de Fibonacci, sabendo-se que fib(0) = 1 e fib(1) = 1. Esse programa para quando n < 0;*/

#include <stdio.h>
int fibonacci(int n) {

    int a = 1, b = 1, temp = 1;

    for (int i = 2; i < n; i++) {

        b = a;
        a += temp;
        temp = b;

        printf("%d\n", a);
    }

    return a;
}


int main(void) {

    int f1 = 1, f2 = 1, n, x;
    while (1) {

        scanf("%d", &n);

        if (n < 0) break;

        if (n >= 2) {
            if (n >= 1) printf("%d\n", f1);
            if (n >= 2) printf("%d\n", f2);
            if (n > 2) x = fibonacci(n);

            printf("Seu número n: %d\n", x);
        }
    }

    printf("FIM DO PROGRAMA.");
    return 0;
}
