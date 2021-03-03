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
	printf("********주차관리시스템**********\n1. 주차\n2. 출차\n3. 주차현황 출력\n4. 층별 빈 주차 공간 확인하기\n0. 종료\n");
	scanf_s("%d", &ret);
	return ret;
}

void parking(int** parking_lot)
{
	int floor = 0;
	int num, option;
	printf("주차할 차번 입력(숫자 4자리) : ");
	scanf_s("%d", &num);

	printf("****************주차 가능 공간 : ");
	for (int i = 0; i < height; i++)
	{
		printf("B%d층[%d대] ", i + 1, width - remain[i]);
	}
	printf("\n");

	while (1)
	{
		print_floor(parking_lot, floor);
		printf("\n\n작업 번호 입력:(다른층 0, 취소 -1) : ");
		scanf_s("%d", &option);
		if (option == 0)
		{
			while (1)
			{
				printf("\n1. B1층 2. B2층 3. B3층\n주차층을 선택하세요 : ");
				scanf_s("%d", &floor);
				floor--;
				if (floor >= 0 && floor < 3)
				{
					break;
				}
				printf("잘못된 입력입니다.\n");
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
				printf("이미 주차된 차량이 존재합니다.\n");
				continue;
			}
		}
		else
		{
			printf("잘못된 입력입니다.\n");
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
		printf("차량 숫자를 입력해주세요 : ");
		scanf_s("%d", &num);
		if (parking_num[num][0] == -1 || parking_num[num][1] == -1)
		{
			printf("해당하는 차량이 존재하지 않습니다. 다시 입력하시려면 1 종료하시려면 0을 눌러주십시오. ");
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
			printf("출차되었습니다.\n");
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
		printf("몇 층을 보기 원하시나요?[B1~B%d] B", height);
		scanf_s("%d", &floor);
		if (floor >= 0 && floor <= height)
		{
			floor--;
			print_floor(parking_lot, floor);
			break;
		}
		printf("해당하는 층이 존재하지 않습니다. 다시 입력하시려면 1 종료하시려면 0을 눌러주십시오. ");
		scanf_s("%d", floor);
		if (floor == 0)
		{
			break;
		}
	}
}

void print_floor(int** parking_lot, int floor)
{
	printf("\n[B%d층]============================\n", floor + 1);
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