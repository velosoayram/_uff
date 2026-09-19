/*Q4) [Problema 1533 do URI Online Judge] John Watson, mesmo após anos trabalhando ao lado
de Sherlock Holmes, nunca conseguiu entender como ele consegue descobrir quem é o assassino
com tanta facilidade. Em uma certa noite, porém, Sherlock bebeu mais do que devia e acabou
contando o segredo a John. “Elementar, meu caro Watson”, disse Sherlock Holmes. “Nunca é o
mais suspeito, mas sim o segundo mais suspeito”. Após descobrir o segredo, John decidiu resolver 
um crime por conta própria, só para testar se aquilo fazia sentido ou se era apenas conversa de bêbado.

Dada uma lista com N inteiros, representando o quanto cada pessoa é
suspeita, ajude John Watson a decidir quem é o assassino, de acordo com o método citado.
Haverá diversos casos de teste. Cada caso de teste inicia com um inteiro N (2 ≤ N ≤ 1000),
representando o número de suspeitos. Em seguida haverá N inteiros distintos, onde o i-ésimo
inteiro, para todo 1 ≤ i ≤ N, representa o quão suspeita a i-ésima pessoa é, de acordo com a
classificação dada por John Watson. Seja V o valor do i-ésimo inteiro, 1 ≤ V ≤ 10000. O último
caso de teste é indicado quando N = 0, o qual não deverá ser processado. Para cada caso de
teste imprima uma linha, contendo um inteiro, representando o indice do assassino, de acordo
com o método citado.*/

#include <stdio.h>
#include <limits.h>
int verificador(int n, int *v) {

	int maior = INT_MIN, suspeito = INT_MIN;

	for (int i = 0; i < n; i++) {
		
		if (v[i] > maior) {

			suspeito = maior;
			maior = v[i];
			
		} else if (v[i] > suspeito && v[i] != maior) {

			suspeito = v[i];
			
		}
	}
	
	return suspeito;
}


int main(void) {

	int n;

	while(1) {

		printf("DIGITE UM No: ");
		scanf("%d", &n);
	
		if (n <= 0) break;

		int v[n];
		
		printf("VALORES DOS SUJEITOS: ");

		for (int i = 0; i < n; i++) {

			scanf("%d", &v[i]);
		}
		
		printf("%d sujeitos: ", n);

		for (int i = 0; i < n; i++) {
		
			printf("%d ", v[i]);
		}

		printf("\n");
		printf("suspeito: %d", verificador(n, v));
		printf("\n\n");
					
	}
	
	printf("\n\n");
	printf("FIM DO PROGRAMA");
	printf("\n\n");

	return 0;
}
