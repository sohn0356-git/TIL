// N=8

#include<vector>
#include <iostream>
using namespace std;

vector<vector<int> > board;
int dirR[8] = {-1,-1,0,1,1,1,0,-1};
int dirC[8] = {0,1,1,1,0,-1,-1,-1};
const int board_size = 8;

int calc(int r, int c);

int solution(vector<vector<int> > _board)
{
    board = _board;
    int answer = 0;
    for(int i=0;i<board_size;i++)
    {
        for(int j=0;j<board_size;j++)
        {
            if(board[i][j]==0)
            {
                int t = calc(i,j);            
                if(answer < t)
                {
                    answer = t;
                }
            }
        }        
    }
    return answer;
}

int calc(int r, int c)
{
    int ret = 0;
    for(int d=0;d<8;d++)
    {
        int cnt = 0;
        int nR = r + dirR[d];
        int nC = c + dirC[d];
        if(nR>=0 && nR<board_size && nC>=0 && nC<board_size)
        {
            if(board[nR][nC]==2)
            {
                cnt++;
                while(1)
                {
                    nR += dirR[d];
                    nC += dirC[d];
                    if(nR>=0 && nR<board_size && nC>=0 && nC<board_size)
                    {
                        if(board[nR][nC]==2)
                        {
                            cnt++;
                        }
                        else if(board[nR][nC]==0)
                        {
                            cnt=0;
                            break;
                        }
                        else if(board[nR][nC]==1)
                        {
                            break;
                        }
                    }
                    else
                    {
                        cnt = 0;
                        break;
                    }
                }
            }
        }
        ret += cnt;
    }
    return ret;
}