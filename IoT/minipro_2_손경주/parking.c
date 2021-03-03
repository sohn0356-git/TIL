#include <stdio.h>
#include <stdlib.h>

int height = 3, width = 10;
int remain[3];
int parking_num[10000][2];
int menu_select();
void parking(int** parking_lot);
void parking_exit(int** parking_lot);
void parking_detail(int** parking_lot);
void parking_show(int** parking_lot);
void print_floor(int** parking_lot, int floor);
int main()
{
	int menu;
	int** parking_lot;
	parking_lot = (int**)malloc(sizeof(int*) * height);
	for (int i = 0; i < 10000; i++)
	{
		parking_num[i][0] = -1;
		parking_num[i][1] = -1;
	}
	for (int i = 0; i < height; i++) {
		parking_lot[i] = (int*)malloc(sizeof(int) * width);
		for (int j = 0; j < width; j++)
		{
			parking_lot[i][j] = j + 1;
		}
	}
	while (1)
	{
		menu = menu_select();
		switch (menu)
		{
		case 1:
			parking(parking_lot);
			break;
		case 2:
			parking_exit(parking_lot);
			break;
		case 3:
			parking_detail(parking_lot);
			break;
		case 4:
			parking_show(parking_lot);
			break;
		default:
			break;
		}
	}
	return 0;
}

int menu_select()
{
	int ret;
	printf("********���������ý���**********\n1. ����\n2. ����\n3. ������Ȳ ���\n4. ���� �� ���� ���� Ȯ���ϱ�\n0. ����\n");
	scanf_s("%d", &ret);
	return ret;
}

void parking(int** parking_lot)
{
	int floor = 0;
	int num, option;
	printf("������ ���� �Է�(���� 4�ڸ�) : ");
	scanf_s("%d", &num);

	printf("****************���� ���� ���� : ");
	for (int i = 0; i < height; i++)
	{
		printf("B%d��[%d��] ", i + 1, width - remain[i]);
	}
	printf("\n");

	while (1)
	{
		print_floor(parking_lot, floor);
		printf("\n\n�۾� ��ȣ �Է�:(�ٸ��� 0, ��� -1) : ");
		scanf_s("%d", &option);
		if (option == 0)
		{
			while (1)
			{
				printf("\n1. B1�� 2. B2�� 3. B3��\n�������� �����ϼ��� : ");
				scanf_s("%d", &floor);
				floor--;
				if (floor >= 0 && floor < 3)
				{
					break;
				}
				printf("�߸��� �Է��Դϴ�.\n");
			}
			continue;
		}
		else if (option == -1)
		{
			for (int i = 0; i < width; i++)
			{
				if (parking_lot[floor][i] == i + 1)
				{
					parking_lot[floor][i] = num;
					parking_num[num][0] = floor;
					parking_num[num][1] = i;
					remain[floor]++;
					break;
				}
			}
		}
		else if (option >= 1 && option <= width)
		{
			option--;
			if (parking_lot[floor][option] == option + 1)
			{
				parking_lot[floor][option] = num;
				parking_num[num][0] = floor;
				parking_num[num][1] = option;
				remain[floor]++;
			}
			else
			{
				printf("�̹� ������ ������ �����մϴ�.\n");
				continue;
			}
		}
		else
		{
			printf("�߸��� �Է��Դϴ�.\n");
			continue;
		}
		print_floor(parking_lot, floor);
		break;
	}
}

void parking_exit(int** parking_lot)
{
	int num;
	while (1)
	{
		printf("���� ���ڸ� �Է����ּ��� : ");
		scanf_s("%d", &num);
		if (parking_num[num][0] == -1 || parking_num[num][1] == -1)
		{
			printf("�ش��ϴ� ������ �������� �ʽ��ϴ�. �ٽ� �Է��Ͻ÷��� 1 �����Ͻ÷��� 0�� �����ֽʽÿ�. ");
			scanf_s("%d", num);
			if (num == 0)
			{
				break;
			}
		}
		else
		{
			parking_lot[parking_num[num][0]][parking_num[num][1]] = parking_num[num][1] + 1;
			remain[parking_num[num][0]]--;
			parking_num[num][0] = -1;
			parking_num[num][1] = -1;			
			printf("�����Ǿ����ϴ�.\n");
			break;
		}
	}
}

void parking_show(int** parking_lot)
{
	for (int i = 0; i < height; i++)
	{
		print_floor(parking_lot, i);
		printf("\n");
	}
}

void parking_detail(int** parking_lot)
{
	int floor;
	while (1)
	{
		printf("�� ���� ���� ���Ͻó���?[B1~B%d] B", height);
		scanf_s("%d", &floor);
		if (floor >= 0 && floor <= height)
		{
			floor--;
			print_floor(parking_lot, floor);
			break;
		}
		printf("�ش��ϴ� ���� �������� �ʽ��ϴ�. �ٽ� �Է��Ͻ÷��� 1 �����Ͻ÷��� 0�� �����ֽʽÿ�. ");
		scanf_s("%d", floor);
		if (floor == 0)
		{
			break;
		}
	}
}

void print_floor(int** parking_lot, int floor)
{
	printf("\n[B%d��]============================\n", floor + 1);
	for (int i = 0; i < width; i++)
	{
		printf("[%d] ", parking_lot[floor][i]);
		if (i == (width / 2) - 1)
		{
			printf("\n");
		}
	}
	printf("\n\n");
}