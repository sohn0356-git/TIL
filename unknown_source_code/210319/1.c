#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.

const int INF = 987654321;
int DP[200001];
int solve(const char* p, int idx);
int solution(const char* p) {
    int answer = 0;
    for(int i=0;i<200001;i++)
    {
        DP[i] = -1;
    }
    int idx = 0;
    while(p[idx]!='\0')
    {
        int t = solve(p,idx);
        if(t==1)
        {
            answer += 1;
        }
        idx+=1;
    }
    return answer;
}

int solve(const char* p, int idx)
{
    if(idx<0 || p[idx]=='\0')
    {
        return 1;
    }

    if(DP[idx]!=-1)
    {
        return DP[idx];
    }
    DP[idx] = INF;
    if(p[idx]=='<')
    {
        DP[idx] = solve(p, idx-1);
    }
    else
    {
        DP[idx] = solve(p, idx+1);
    }
    return DP[idx];
}