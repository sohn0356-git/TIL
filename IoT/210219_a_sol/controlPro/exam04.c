//#include <stdio.h>
//
//int main()
//{
//	int a, b;
//	char op;
//	scanf_s("%d %d %c", &a, &b, &op);
//	switch (op)
//	{
//	case '+':
//		printf("%d %c %d�� ���� ����� %d�Դϴ�.", a, op, b, a + b);
//		break;
//	case '-':
//		printf("%d %c %d�� ���� ����� %d�Դϴ�.", a, op, b, a - b);
//		break;
//	case '*':
//		printf("%d %c %d�� ���� ����� %d�Դϴ�.", a, op, b, a * b);
//		break;
//	case '/':
//		if (b == 0)
//		{
//			printf("�߸��� �Է��Դϴ�.\n");
//		} else {
//			printf("%d %c %d�� ���� ����� %lf�Դϴ�.", a, op, b, (double)a / b);
//		}
//		break;
//	default:
//		printf("�߸��� �Է��Դϴ�.\n");
//		break;
//	}
//	return 0;
//}