//#include <stdio.h>
//
//
//int ParkingMenu(void);
//void InParking();
//void NowParking(int (*parr)[10]);
//void CheckParking(int(*parr)[10]);
//
//int main()
//{
//	int Parkingarr[3][10];
//	int (*parr)[10] = Parkingarr;
//	int menuIndex = 0;
//
//	while ((menuIndex = ParkingMenu()) != 0)
//	{
//		switch (menuIndex)
//		{
//		case 1:
//			printf("1. ����\n");
//			InParking();
//			break;
//		case 2:
//			printf("2. ����\n");
//			//OutParking();
//			break;
//		case 3:
//			printf("3. ������Ȳ ���\n");
//			NowParking(parr);
//			break;
//		case 4:
//			printf("4. ���� �� ���� ���� Ȯ���ϱ�\n");
//			CheckParking(parr);
//			break;
//		default:
//			printf("�߸�����\n");
//			break;
//		}
//	}
//	printf("����");
//	return 0;
//}
//
//
//int ParkingMenu(void)
//{
//	int inputValue = 0;
//	printf("--------------���������ý���---------------\n\n");
//	printf("1. ����\t2. ����\t3. ������Ȳ ���\t4. ���� �� ���� ���� Ȯ���ϱ�\t0. ����\n");
//	printf("��ȣ ���� : ");
//	scanf_s("%d", &inputValue);
//	return inputValue;
//}
//
//void InParking()
//{
//	int num1, num2, num3, num4;
//	printf("������ ���� �Է�(���� 4�ڸ�) : ");
//	scanf_s("%d", &num1);
//	printf("�۾� ��ȣ �Է�(�ٸ��� 0, ��� -1) : ");
//	scanf_s("%d", &num2);
//	switch (num2)
//	{
//	case 0:
//		printf("1. B1�� 2. B2�� 3. B3��\n");
//		printf("�������� �����ϼ��� : ");
//		scanf_s("%d", &num3);
//		printf("���� ��ȣ �Է� : ");
//		scanf_s("%d", &num4);
//
//
//		printf("�����Ǿ����ϴ�.\n");
//		break;
//	case -1:
//		break;
//
//	default:
//		printf("�����Ǿ����ϴ�.\n");
//		break;
//	}
//
//
//}
//
//
//void NowParking(int(*parr)[10])
//{
//	for (int i = 0; i < 3; i++)
//	{
//		printf("-------------------------------B%d��-------------------------------\n\n", i + 1);
//		for (int j = 0; j < 10; j++)
//		{
//			printf("%d\t", *(parr[i] + j));
//		}
//		printf("\n\n");
//	}
//}
//
//void CheckParking(int(*parr)[10])
//{
//	int check;
//	printf("���� �Է��ϼ���(B1�� = 1, B2�� = 2, B3�� = 3 : ");
//	scanf_s("%d", &check);
//	if (check == 1)
//	{
//		printf("-----------------B1��---------------\n\n");
//		for (int i = 0; i < 10; i++)
//		{
//
//			printf("%d\t", parr[0][i]);
//		}
//		printf("\n");
//	}
//	else if (check == 2)
//	{
//		printf("-----------------B2��---------------\n\n");
//		for (int i = 0; i < 10; i++)
//		{
//
//			printf("%d\t", *parr[i]);
//		}
//		printf("\n");
//	}
//	else
//	{
//		printf("-----------------B3��---------------\n\n");
//		for (int i = 0; i < 10; i++)
//		{
//
//			printf("%d\t", parr[2][i]);
//		}
//		printf("\n");
//	}
//}