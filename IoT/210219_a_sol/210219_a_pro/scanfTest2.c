#include <stdio.h>

int main()
{
	int age = 0;
	printf("나이를 입력하세요 : ");
	scanf_s("%d%*c", &age);
	printf("%d\n", age);

	char name[10] = { 0 };
	printf("이름을 입력하세요 : ");
	gets_s(name, sizeof(name));
	printf("%s", name);
	return 0;
}