//#include <stdio.h>
//#include <windows.h>
//
//int cnt;
//int students[50][5];
//int sub_score[5];
//int stu_score[50];
//char printMenu();
//void addStudent();
//void showStudent();
//void searchStudent(char name);
//void subjectAvg();
//void studentAvg();
//
//int main()
//{
//	int menuIndex;
//	char name;
//	while (1) {
//		menuIndex = printMenu();
//		if (menuIndex == '6')
//		{
//			break;
//		}
//		printf("\n");
//		switch (menuIndex)
//		{
//		case '1':
//			addStudent();
//			printf("성공적으로 등록되었습니다.\n");
//			Sleep(3000);
//			system("cls");
//			break;
//		case '2':
//			showStudent();
//			break;
//		case '3':
//			printf("찾으시는 학생의 이름을 입력하세요 : ");
//			scanf_s(" %c", &name);
//			searchStudent(name);
//			break;
//		case '4':
//			subjectAvg();
//			break;
//		case '5':
//			studentAvg();
//			break;
//		default:
//			printf("잘못된 입력입니다.\n");
//			Sleep(3000);
//			system("cls");
//			break;
//		}
//		printf("\n");
//	}
//	printf("종료");
//	return 0;
//}
//
//char printMenu()
//{
//	char inputValue;
//	printf("*******************학사관리 시스템*******************\n");
//	printf("1. 학생등록\n2. 전체학생조회\n3. 학생검색\n4. 과목별평균점수\n5. 학생별평균\n6. 종료\n");
//	printf("원하는 메뉴를 선택하세요 : ");
//	scanf_s(" %c", &inputValue);
//	return inputValue;
//}
//
//void addStudent()
//{
//	if (cnt >= 50)
//	{
//		printf("시스템이 꽉 찼습니다.\n");
//	}
//	printf("*******학생을 등록하세요*******\n");
//	printf("학생명 : ");
//	scanf_s(" %c", &students[cnt][0]);
//	printf("python : ");
//	scanf_s("%d", &students[cnt][1]);
//	stu_score[cnt] += students[cnt][1];
//	sub_score[1] += students[cnt][1];
//	printf("c : ");
//	scanf_s("%d", &students[cnt][2]);
//	stu_score[cnt] += students[cnt][2];
//	sub_score[2] += students[cnt][2];
//	printf("Raspberry : ");
//	scanf_s("%d", &students[cnt][3]);
//	stu_score[cnt] += students[cnt][3];
//	sub_score[3] += students[cnt][3];
//	printf("mongodb : ");
//	scanf_s("%d", &students[cnt][4]);
//	stu_score[cnt] += students[cnt][4];
//	sub_score[4] += students[cnt][4];
//	cnt++;
//}
//
//void showStudent()
//{
//	for (int i = 0; i < cnt; i++)
//	{
//		printf("학생명 : %c\n", students[i][0]);
//		printf("python : %d\n", students[i][1]);
//		printf("C : %d\n", students[i][2]);
//		printf("Raspberry : %d\n", students[i][3]);
//		printf("mongodb : %d\n", students[i][4]);
//		printf("\n\n");
//	}
//}
//
//void searchStudent(char name)
//{
//	for (int i = 0; i < cnt; i++)
//	{
//		if (students[i][0] == name)
//		{
//			printf("학생명 : %c\n", students[i][0]);
//			printf("python : %d\n", students[i][1]);
//			printf("C : %d\n", students[i][2]);
//			printf("Raspberry : %d\n", students[i][3]);
//			printf("mongodb : %d\n", students[i][4]);
//		}
//	}	
//}
//
//void subjectAvg()
//{
//	printf("python평균 : %d\n", sub_score[1] / cnt);
//	printf("C평균 : %d\n", sub_score[2] / cnt);
//	printf("Raspberry평균 : %d\n", sub_score[3] / cnt);
//	printf("mongodb평균 : %d\n", sub_score[4] / cnt);
//}
//
//void studentAvg()
//{
//	for (int i = 0; i < cnt; i++)
//	{
//		printf("%c : %d\n", students[i][0], stu_score[i] / 4);
//	}
//}