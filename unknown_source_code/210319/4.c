#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

const int MOD = 1000007;
int N,M,K;
int answer;
int DP[101][101];
int solve(int n, int m);
int solution(int n, int m, int k) {
    N = n;
    M = m;
    K = k;
    for(int i=0;i<101;i++)
    {
        for(int j=0;j<101;j++)
        {
            DP[i][j] = -1;
        }        
    }
    answer = solve(0, 0)%MOD;
    return answer;
}

int solve(int n, int m)
{
    if(n>=N || m>=M)
    {
        if(n==N && m==M)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    if(DP[n][m]!=-1)
    {
        return DP[n][m];
    }
    DP[n][m] = 0;
    for(int i=1;i<=K;i++)
    {
        DP[n][m] += solve(n+1, m+i)%MOD;
        DP[n][m] %= MOD;
    }
    return DP[n][m];
}