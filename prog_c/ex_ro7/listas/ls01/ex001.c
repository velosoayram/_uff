/* Q1) Implemente um programa que, infinitamente, receba, como parâmetro de entrada, um número
n e retorne os n primeiros números primos existentes. Seu programa para quando n for menor ou
igual a zero. */

#include <stdio.h> 
int fprimo(int n) {

    if (n < 2) return 0;
    else {
        int i;
        for (i = 2; i * i <= n; i++) {
            if (n % i == 0) return 0;
        }
    }
    return 1;
}


int main(void) {
    while(1) {
        int c_ind = 2;
        int c_tot = 0;
        int num;
        scanf("%d", &num);
        if (num <= 0) break;
        while(c_tot < num) {
            if (fprimo(c_ind)) {
                printf("%d ", c_ind);
                c_tot++;
            }
            c_ind++;
            if (c_tot == num) printf("\n");
        }
    }
    return 0;
}
