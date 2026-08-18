/* Q2) Implemente um programa que, infinitamente, receba, como parâmetro de entrada, um número
n e retorne os n primeiros números primos existentes depois de n. Por exemplo, se n = 2, a
resposta será os primos 3 e 5. É necessário salientar que n não precisa ser primo. Seu programa
para quando n for menor ou igual a zero. */

#include <stdio.h>
int fprimo(int n) {

    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }

    return 1;
}


int main(void) {

    while(1) {
        int n;
        scanf("%d", &n);
        if (n <= 0) break;
        int i = n + 1;
        int cont = 0;
        while (cont < n) {
            if (fprimo(i)) {
                printf("%d ", i);
                cont++;
            }
            i++;
        }
        printf("\n");
    }

    printf("FIM DE PROGRAMA.");
    return 0;
}
