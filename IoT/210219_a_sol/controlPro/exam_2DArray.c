//#include <stdio.h>
//
//int main()
//{
//	int myarr[5][5];
//	int sumarr[6] = { 0 };
//	for (int i = 0; i < 5; i++)
//	{
//		int sum = 0;
//		for (int j = 0; j < 5; j++)
//		{
//			myarr[i][j] = i * 5 + (j + 1);
//			sum += myarr[i][j];
//			printf("%d ", myarr[i][j]);
//			sumarr[j] += myarr[i][j];
//		}
//		printf("%d\n", sum);
//		sumarr[5] += sum;
//	}
//	for (int i = 0; i < 6; i++)
//	{
//		printf("%d ", sumarr[i]);
//	}
//	return 0;
//}