/*Q1) Alguns números possuem uma propriedade interessante: se você recuperar seus dois
primeiros dı́gitos e seus dois últimos dı́gitos e elevar ao quadrado a soma deles, você obterá a
concatenação desses quatro dı́gitos. Por exemplo, o número 203125 possui essa propriedade,
pois (20 + 25)**2 = 2025. Por outro lado, o mesmo não é observado para 20326, pois (20 + 26)2 = 2116 2026 ≠ .
Escreva uma função que informa se um número possui essa propriedade – int teste(int n) – retornando UM se o
número satisfaz a essa propriedade, e ZERO caso contrário.*/

#include <stdio.h>
int teste(int n) {

    if (n < 1000) return 0;

    int np1 = n;
    int np2 = n % 100;

    while (np1 >= 100) {
        np1 /= 10;
    }

    int concat = (np1 * 100) + np2;

    printf("(%d + %d)² = %d\n", np1, np2, (np1 + np2) * (np1 + np2));

    if (concat == (np1 + np2) * (np1 + np2)) return 1;

    return 0;

}

int main(void) {

    int num;

    printf("Veja se seu número tem uma propriedade especial.\nDigite: ");
    scanf("%d", &num);
    if (teste(num)) {
        printf("%d tem a propriedade especial!", num);
    } else printf("%d não tem a propriedade especial!", num);

    return 0;
}

// #include <stdio.h>
// void extracao(int *n, int *np1, int *np2) {

// 	*np1 = *n;

// 	while (*np1 >= 100) {
// 		*np1 /= 10;
// 	}
	
// 	*np2 = *n % 100;
	
// }


// int teste(int *n) {

// 	if (*n < 1000) return 0;

// 	int np1, np2;

// 	extracao(n, &np1, &np2);

// 	int concat = (np1 * 100) + np2;

// 	if ((np1 + np2) * (np1 + np2) == concat) return 1;
	
// 	return 0;
	
// }


// int main(void) {

// 	int n;
// 	int *p = &n;
		
// 	printf("DIGITE UM NÚMERO: ");
// 	scanf("%d", &n);

// 	if (teste(p)) {
// 		printf("%d possui uma propriedade especial.", *p);
// 	} else {
// 		printf("%d não possui uma propriedade especial.", *p);
// 	}

// 	return 0;
// }
