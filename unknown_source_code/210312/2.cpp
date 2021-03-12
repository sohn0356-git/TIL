#include <string>
#include <iostream>
#include <vector>

using namespace std;

vector<string> drum;
int DP[1001][1001][2];
int solve(int r, int c, int t);

int solution(vector<string> _drum) {
    drum = _drum;
    int answer = 0;
    for(int i=0;i<1001;i++)
    {
        for(int j=0;j<1001;j++)
        {
            DP[i][j][0] = -1;
            DP[i][j][1] = -1;
        }
    }
    for(int i=0;i<drum.size();i++)
    {
        answer += solve(0,i,0);
    }
    return answer;
}

int solve(int r, int c, int t)
{
    if(r==drum.size())
    {
        return 1;
    }
    int &res = DP[r][c][t];
    if(res!=-1)
    {
        return res;
    }
    res = 0;
    if(drum[r][c]=='#')
    {
        res = solve(r+1,c,t);
    }
    else if(drum[r][c]=='>')
    {
        res = solve(r, c+1, t);
    }
    else if(drum[r][c]=='<')
    {
        res = solve(r, c-1, t);
    }
    else
    {
        if(t==0)
        {
            res = solve(r+1, c, 1);
        }
        else
        {
            return 0;
        }
    }
    return res;    
}