//#include <stdio.h>
//
//char getGrade(int score);
//
//int main()
//{
//	int score;
//	scanf_s("%d", &score);
//	char res = getGrade(score);
//	if (res == 'X') {
//		printf("�߸��� �Է��Դϴ�.\n");
//	} else {
//		printf("%c�����Դϴ�\n", res);
//	}
//	return 0;
//}
//
//char getGrade(int score)
//{
//	char res = 'X';
//	if (0 <= score && score <= 100)
//	{
//		switch (score / 10) {
//		case 10:
//		case 9:
//			res = 'A';
//			break;
//		case 8:
//			res = 'B';
//			break;
//		case 7:
//			res = 'C';
//			break;
//		case 6:
//			res = 'D';
//			break;
//		default:
//			res = 'F';
//			break;
//		}
//	}
//	return res;
//}