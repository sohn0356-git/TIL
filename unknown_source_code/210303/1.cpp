#include <iostream>
#include <string>
#include <vector>
using namespace std;


string change(int p, int num);


int solution(int p, int index) {
    int answer = -1;
    int num = 0;
    string str = "0";
    while (str.length() < index)
    {
        str += change(p, num);
        num++;
    }
    answer = str[index - 1] - '0';
    return answer;
}


string change(int p, int num) {
    string ret = "";
    while (num > 0)
    {
        ret = to_string(num % p) + ret;
        num /= p;
    }
    return ret;
}