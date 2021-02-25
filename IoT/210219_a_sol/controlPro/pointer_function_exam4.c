//#include <stdio.h>
//
//void rotate(int* p1, int* p2, int* p3);
//
//int main()
//{
//	int n1 = 10;
//	int n2 = 20;
//	int n3 = 30;
//	char op;
//	while ((scanf_s("%c",&op)))
//	{
//		if (op != '\n')
//		{
//			break;
//		}
//		rotate(&n1, &n2, &n3);
//		printf("%d %d %d\n", n1, n2, n3);
//	}
//	return 0;
//}
//
//void rotate(int* p1, int* p2, int* p3)
//{
//	int tmp = *p1;
//	*p1 = *p2;
//	*p2 = *p3;
//	*p3 = tmp;
//}