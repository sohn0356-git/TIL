///
/*
길이가 M인 문자열 N개를 담은 vector S가 있다.
N개의 문자열 중에 같은 index에 같은 문자가 있는 서로 다른 문자열을 발견하면
그 위치와 index를 반환한다.
예를들어, S=['abc','adc']이면 0번째 문자열의 0번째 문자와 1번째 문자열의 1번째 문자가 같으므로
[0,1,0] or [1,0,0]을 return 하면 된다. 혹은 [0,1,2] or [1,0,2]를 return해도 된다.
1<=N<=30000
1<=M<=2000
N*M<=30000
*/
///





#include <iostream>
#include <vector>

using namespace std;

vector<int> solution(vector<string> &S) {
    // write your code in C++14 (g++ 6.2.0)
    vector<vector<int>>v[26];
    vector<int> answer;
    int N = S.size();
    for(int i=0;i<26;i++)
    {
        for(int j=0;j<3001;j++)
        {
            vector<int>tmp;
            v[i].push_back(tmp);
        }
    }
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<S[i].length();j++)
        {
            v[S[i][j]-'a'][j].push_back(i);
        }
    }
    
    for(int i=0;i<26;i++)
    {
        for(int j=0;j<v[i].size();j++)
        {
            if(v[i][j].size()>1)
            {
                for(int k=0;k<v[i][j].size();k++)
                {
                    
                    for(int l=k+1;l<v[i][j].size();l++)
                    {
                        answer.push_back(v[i][j][k]);
                        answer.push_back(v[i][j][l]);
                        answer.push_back(j);
                        return answer;
                    }
                }
            }
        }
    }
    
    return answer;
}
