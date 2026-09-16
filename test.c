#include <stdio.h>

void teste(int *x, int y) {

    for(int i = 0; i < y; i++){
        (*x)++;
        printf("%d\n", *x);
    } 

}

int main(void) {

    int valor = 1;
    int teto = 20;

    teste(&valor, teto);

    printf("%d\n", valor);

    return 0;

}
