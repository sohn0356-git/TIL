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
//		printf("%d %c %d의 연산 결과는 %d입니다.", a, op, b, a + b);
//		break;
//	case '-':
//		printf("%d %c %d의 연산 결과는 %d입니다.", a, op, b, a - b);
//		break;
//	case '*':
//		printf("%d %c %d의 연산 결과는 %d입니다.", a, op, b, a * b);
//		break;
//	case '/':
//		if (b == 0)
//		{
//			printf("잘못된 입력입니다.\n");
//		} else {
//			printf("%d %c %d의 연산 결과는 %lf입니다.", a, op, b, (double)a / b);
//		}
//		break;
//	default:
//		printf("잘못된 입력입니다.\n");
//		break;
//	}
//	return 0;
//}