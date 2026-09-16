/*Q2) Implemente um programa que, infinitamente, teste se um número é um palíndromo (Dica: se
uma palavra pode ser lida, indiferentemente, da esquerda para a direita e vice-versa, ela é
considerada um palíndromo). Você deve passar o número a ser testado. O seu programa deverá
imprimir as seguintes mensagens “VERDADEIRO” (caso o número seja um palíndromo) ou
“FALSO” (caso o número não seja um palíndromo) na console. Seu programa para quando o
número for negativo.*/

#include <stdio.h>

int inverter(int n, int acumulador) {

	if (n == 0) return acumulador;

	return inverter(n /10, (acumulador * 10) + (n % 10));
}

int palindromer(int n) {

	if (n < 10) return 1;

	int acumulador = inverter(n, 0);

	return (n == acumulador);
}

int main(void) {

	int n;

    while (1) {
        printf("DIGITE UM NÚMERO: ");
        scanf("%d", &n);

        if (palindromer(n)) {
            printf("VERDADEIRO\n");
        } else {
            printf("FALSO\n");
        }
    }
	
	return 0;	
}
