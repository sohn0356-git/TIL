int sum_arr[1551], N, M;
vector<vector<int>> grid;
int calc(int r, int c, int d)
{
    int sum = 0;
    for(int i=0;i<=d;i++)
    {
        sum+=grid[r+i][r+d];
    }
    for(int j=0;j<=d;j++)
    {
        sum+=grid[r+d][c+j];
    }
    sum-=grid[r+d][c+d];

    return sum;
}

int largestSubgrid(vector<vector<int>> _grid, int maxSum) {
    grid = _grid;
    N = grid.size();
    M = grid[0].size();
    int mid = N;
    if(mid>M)
    {
        mid = M;
    }
    int kLength = mid;
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<M;j++)
        {
            int tmp = 0;
            for(int k=0;k<kLength;k++)
            {
                if(i+k<N && j+k<M)
                {
                    tmp += calc(i,j,k);
                    if(sum_arr[k+1] < tmp)
                    {
                        sum_arr[k+1] = tmp;
                    }
                    if(maxSum<tmp)
                    {
                        kLength = k;
                        break;
                    }
                }
                else {
                    // cout<<'\n';
                    break;
                }
            }
        }
    }
    for(int l=1;l<=mid;l++)
    {
        if(sum_arr[l]>maxSum)
        {
            return l-1;
        }
    }
    return mid;
}