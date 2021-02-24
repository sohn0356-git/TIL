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
//		printf("잘못된 입력입니다.\n");
//	} else {
//		printf("%c학점입니다\n", res);
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