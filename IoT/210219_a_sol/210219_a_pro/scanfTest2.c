#include <stdio.h>

int main()
{
	int age = 0;
	printf("���̸� �Է��ϼ��� : ");
	scanf_s("%d%*c", &age);
	printf("%d\n", age);

	char name[10] = { 0 };
	printf("�̸��� �Է��ϼ��� : ");
	gets_s(name, sizeof(name));
	printf("%s", name);
	return 0;
}