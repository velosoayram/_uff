/*(Q1) Implemente uma função em C que receba uma string como parâmetro e substitua todas as suas
letras por predecessoras do alfabeto, trocando maiúsculas por minúsculas. Por exemplo, a string
“Amor” seria alterada para “zLNQ”. Esta função deve obedecer o seguinte protótipo: void
shift_troca_string (char *str). A letra ‘a’ deve ser substituída por ‘Z’ (e ‘A’ por ‘z’). Caracteres que não
forem letras devem ser substituídos por ‘!’. Sabe-se que A = 65, Z = 90, a = 97 e z = 122.*/

#include <stdio.h>
void shift_troca_string(char *str) {

	int i = 0;
	while (str[i] != '\0') {
		if ((str[i] >= 65) && (str[i] <= 90)) {
			if (str[i] == 65) str[i] = 122; // A -> z
			else str[i] += 31;
		} else if ((str[i] >= 97) && (str[i] <= 122)) {
			if (str[i] == 97) str[i] = 90; // a -> Z
			else str[i] -= 33;
		} else str[i] = '!';
		i++;
	}
}


int main(void) {

	char str[100];
	scanf("%s", str); // levei um pau, não sabia que o scanf aqui não necessita de &.
	shift_troca_string(str);
	printf("%s", str);		
	return 0;
}
