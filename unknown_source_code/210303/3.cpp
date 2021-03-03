#include <iostream>
#include <string>
#include <vector>
using namespace std;


int days[12] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
string y[7] = { "월", "화", "수", "목", "금", "토", "일" };

vector<int> solution(int day, int k) {
    vector<int> answer;
    k = k % 7;
    int nextday = (day + k + 6) % 7;
    for (int i = 0; i < 12; i++)
    {
        if (nextday == 5 || nextday == 6)
        {
            answer.push_back(1);
        }
        else
        {
            answer.push_back(0);
        }
        nextday = (nextday + days[i] % 7) % 7;
    }
    return answer;
}