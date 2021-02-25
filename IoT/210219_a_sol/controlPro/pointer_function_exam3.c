//#include <stdio.h>
//
//void test_sort(int* p1, int* p2, int* p3);
//void swap(int* p1, int* p2);
//
//int main()
//{
//	int n1, n2, n3;
//	scanf_s("%d %d %d", &n1, &n2, &n3);
//	test_sort(&n1, &n2, &n3);
//	printf("%d %d %d", n1, n2, n3);
//	return 0;
//}
//
//void swap(int* p1, int* p2)
//{
//	int tmp = *p1;
//	*p1 = *p2;
//	*p2 = tmp;
//}
//
//void test_sort(int* p1, int* p2, int* p3)
//{
//	if (*p1 < *p2)
//	{
//		swap(p1, p2);
//	}
//	if (*p1 < *p3) 
//	{
//		swap(p1, p3);
//	}
//	if (*p2 < *p3)
//	{
//		swap(p2, p3);
//	}
//}