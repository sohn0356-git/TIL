//#include <stdio.h>
//
//int main()
//{
//	int score;
//	char grade;
//	scanf_s("%d", &score);
//	switch (score/10)
//	{
//	case 10:
//		if (score == 100) {
//			grade = 'A';
//		} else {
//			grade = 'X';
//		}
//		break;
//	case 9:
//		grade = 'A';
//		break;
//	case 8:
//		grade = 'B';
//		break;
//	case 7:
//		grade = 'C';
//		break;
//	case 6:
//		grade = 'D';
//		break;
//	case 5: case 4: case 3: case 2: case 1: case 0:
//		grade = 'F';
//		break;
//	default:
//		grade = 'X';
//		break;
//	}
//	if (score<0 || grade == 'X') {
//		printf("잘못된 입력을 하셨습니다.");
//	} else {
//		printf("%c학점입니다.", grade);
//	}
//	return 0;
//}