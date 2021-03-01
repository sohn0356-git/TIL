//#include <stdio.h>
//
//int myarr[4];
//void inputdata(int* p_arr[]);
//void printdata(int* p_arr[]);
//
//int main()
//{
//	int myarr1[4] = { 10,20,30,100 };
//	int myarr2[4] = { 40,50,60,70 };
//	int myarr3[4] = { 80,90,100,110 };
//	int* p_arr[10] = { myarr1,myarr2,myarr3,myarr1 };
//	inputdata(p_arr);
//	printdata(p_arr);
//	return 0;
//}
//
//
//void inputdata(int* p_arr[])
//{
//	for (int i = 0; i < 4; i++)
//	{
//		scanf_s("%d", &myarr[i]);
//	}
//	p_arr[4] = myarr;
//}
//
//void printdata(int* p_arr[])
//{
//	for (int i = 0; i < 5; i++)
//	{
//		for (int j = 0; j < 4; j++)
//		{
//			printf("%d ", p_arr[i][j]);
//		}
//		printf("\n");
//	}	
//}