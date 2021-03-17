#include <iostream>
#include <string>

using namespace std;

string runLengthDecoding(string str);

int main()
{
    string str = "10A6BX3Q2P";
    cout << runLengthDecoding(str);
    return 0;
}

string runLengthDecoding(string str)
{
    string ret = "";
    for (int i = 0; i < str.length(); i++)
    {
        int num = 0;
        if (str[i] >= '0' && str[i] <= '9') // 숫자를 만났을 때
        {
            while (str[i] >= '0' && str[i] <= '9')
            {
                num *= 10;
                num += str[i] - '0';
                i++;
            }
            num -= 1;
        }
        for (int j = 0; j <= num; j++)
        {
            ret += str[i];
        }
    }
    return ret;
}