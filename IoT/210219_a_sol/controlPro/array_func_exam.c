//#include <stdio.h>
//
//void inputArray(double* ptr);
//double getMax(double* ptr, int size);
//
//int main()
//{
//	double num[5] = { 0.0 };
//	inputArray(num);
//	printf("%lf", getMax(num, sizeof(num) / sizeof(double)));
//	return 0;
//}
//
//void inputArray(double* ptr)
//{
//	for (int i = 0; i < 5; i++)
//	{
//		scanf_s("%lf", ptr + i);
//	}
//}
//
//double getMax(double* ptr, int size)
//{
//	int maxIdx = 0;
//	for (int i = 1; i < size; i++)
//	{
//		if (ptr[maxIdx] < ptr[i])
//		{
//			maxIdx = i;
//		}
//	}
//	return ptr[maxIdx];
//}