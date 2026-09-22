/*Q1) Uma forma simples e eficiente de calcular todos os números primos até um certo valor n é o
método da Peneira de Eratosthenes. O processo é simples: escrevem-se todos os valores entre 2
e n (limite máximo). Em seguida, faz-se um círculo em volta do 2, marcando como primo e riscam-
se todos os seus múltiplos. Continua-se a fazer círculos em volta do menor inteiro que se
encontra, eliminando todos os seus múltiplos. Quando não restarem números sem terem círculos
à volta ou traços por cima, os números com círculos à volta representam todos os primos até n. A
figura seguinte apresenta o método para n = 40.

Escreva um programa que implemente a Peneira de Eratosthenes. Você deve ler o valor n e
mostrar todos os números primos encontrados.*/

#include <stdio.h>
void imp_primo(int n) {

	if (n < 2) {
		printf("\nNÃO HÁ PRIMOS\n");
		return;
	}

	int array[n+1];

	for (int i = 0; i <= n; i++) {
		array[i] = 1;
	}

	array[0] = 0;
	array[1] = 0;

	for (int i = 2; i*i <= n; i++) {
		if (array[i] == 1) {
			for (int j = i*i ; j <= n ; j += i) {
				array[j] = 0;
			}
		}
	}

	for (int i = 2; i <= n; i++) {
		if (array[i] == 1) printf("%d ", i);
	}
	return;
}


int main(void) {

	int n;
	printf("DIGITE UM No: ");
	scanf("%d", &n);
	imp_primo(n);
	printf("\nFIM DO PROGRAMA\n");
	return 0;
}
