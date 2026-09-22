/*Q3) Um número a é dito permutação de um número b se os dígitos de a formam uma permutação
dos dígitos de b. Exemplo: 5412434 é uma permutação de 4321445, mas não é uma permutação
de 4312455. Faça um programa que receba a e b e responda se a é permutação de b. Obs.:
Considere que o dígito 0 (zero) não deve aparecer nos números.*/

#include <stdio.h>
#include <stdlib.h>
int contador(int x) {

	if (x == 0) return 1;
	if (x < 0) x = -x;
	int count = 0;
	while (x > 0) {
		count++;
		x /= 10;
	}
	return count;
}


int* int_array(int x, int n) {

	int *array = (int *) malloc(n * sizeof(int));
	if (array == NULL) return NULL;
	for (int i = (n-1); i >= 0; i--) {
		array[i] = x % 10;
		x /= 10;
	}
	return array;
}


void quicksort(int *array, int n) {

	if (n <= 1) return;
	int a = 0, b = (n-2), pivot = (n-1), temp;

	while (a <= b) {
		while (a <= b && array[a] < array[pivot]) a++;
		while (a <= b && array[b] > array[pivot]) b--;
		if (a < b) {
			temp = array[a];
			array[a++] = array[b];
			array[b--] = temp;
		}
	}
	temp = array[pivot];
	array[pivot] = array[a];
	array[a] = temp;	
	
	quicksort(array, a);
	quicksort(array + a + 1, n - a - 1);
}


int main(void) {

	int a;
	printf("DIGITE O No A: ");
	scanf("%d", &a);
	int qtd_a = contador(a);
	int b;
	printf("DIGITE O No B: ");
	scanf("%d", &b);
	int qtd_b = contador(b);
	if (qtd_a != qtd_b) printf("VALORES DISTINTOS | FIM DO PROGRAMA.\n");
	
	else {

		int flag = 0;
		int *vet_a = int_array(a, qtd_a);
		int *vet_b = int_array(b, qtd_b);
		quicksort(vet_a, qtd_a);
		quicksort(vet_b, qtd_b);
		for (int i = 0; i < qtd_a; i++) {
			if (vet_a[i] != vet_b[i]) {
				printf("NÃO SÃO PERMUTAÇÃO UM DO OUTRO.");
				flag = 1;
				break;
			}
		}
		if (!flag) printf("SÃO PERMUTAÇÃO UM DO OUTRO.");
		free(vet_a);
		free(vet_b);
		printf("\n");				
	}
	return 0;
}

// versão otimizada:
#include <stdio.h>
int permuta(int a, int b) {

	int array[10] = {0};
	while (a > 0) {
		array[a % 10]++;
		a /= 10;
	}
	while (b > 0) {
		array[b % 10]--;
		b /= 10;
	}
	for (int i = 0; i < 10; i++) {
		if (array[i] != 0) return 0;
	}
	return 1;
}


int main(void) {

	int a, b;
	scanf("%d %d", &a, &b);
	if (permuta(a, b)) {
		printf("É PERMUTAÇÃO.\n");
	} else {
		printf("NÃO É PERMUTAÇÃO.\n");
	}
	return 0;
}
