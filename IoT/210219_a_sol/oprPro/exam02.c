#include <stdio.h>

int main()
{
	int a, b, c;
	scanf_s("%d %d %d", &a, &b, &c);
	printf("Max : %d", ((a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c)));
	return 0;
}