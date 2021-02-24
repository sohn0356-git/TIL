#include <stdio.h>


int flag = 1;
int calc(int n1, int n2, char op);

int main()
{
	int n1, n2;
	char op;
	scanf_s("%d %d %c", &n1, &n2, &op);
	int res = calc(n1, n2, op);
	if (flag)
	{
		printf("%d %c %d = %d�Դϴ�.\n", n1, op, n2, res);
	}
	else
	{
		printf("�߸��� �Է��� �ϼ̽��ϴ�.\n");
	}
	return 0;
}

int calc(int n1, int n2, char op)
{
	int res = 0;
	switch (op)
	{
	case '+':
		res = n1 + n2;
		break;
	case '-':
		res = n1 - n2;
		break;
	case '*':
		res = n1 * n2;
		break;
	case '/':
		if (n2 == 0)		{
			flag = 0;
		}		else		{
			res = n1 / n2;
		}
		break;
	default:
		flag = 0;
		break;
	}
	return res;
}