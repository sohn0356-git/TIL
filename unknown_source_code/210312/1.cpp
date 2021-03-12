// x,y 2^31-1

#include <iostream>

using namespace std;

int gcd(int x, int y);

bool solution(int x,int y)
{
    bool answer = true;

    int t = gcd(x,y);
    if(t!=1)
    {
        answer = false;
    }

    return answer;
}

int gcd(int x, int y)
{
    if(x<y)
    {
        int tmp = x;
        x = y;
        y = tmp;
    }
    while(y>0)
    {
        int tmp = x%y;
        x = y;
        y = tmp;
    }
    return x;
}