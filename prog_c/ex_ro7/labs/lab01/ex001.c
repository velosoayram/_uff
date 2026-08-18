/*(1) Implemente um programa que, infinitamente, leia um número n e a sequência de n elementos e retorne o número de vezes em que essa sequência deixou de ser estritamente crescente. Esse programa para quando n ≤ 0;*/

#include <stdio.h>
int main(void) {

    int n, a;

    while(1) {

        int temp, cont = 0, flag = 1;

        scanf("%d", &n);

        if (n <= 0) break;

        for (int i = 0; i < n; i++) {

            scanf("%d", &a);

            if (i == 0) temp = a;
        
            if (a > temp && flag == 0) {
            
                cont++;
                flag = 1;

            } else flag = 0;

            temp = a;
        }

        printf("%d vezes estritamente crescente.\n", cont);
    }

    printf("FIM DO PROGRAMA");

    return 0;
}
