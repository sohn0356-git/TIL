// 1<=N<=100000
#include <string>
#include <set>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int solution(vector<int> weights) {
    int answer = 1;
    multiset<pair<long long,int>>pw;    //weight, cnt
    sort(weights.begin(), weights.end());
    for(int i=0;i<weights.size();i++)
    {
        pw.insert({weights[i],-1});
    }
    for(auto itr = pw.begin();;itr++)
    {
        long long fw = itr->first;
        int fc = itr->second;
        itr++;
        if(itr==pw.end())
        {
            break;
        }
        long long sw = itr->first;
        int sc = itr->second;
        if(fw==sw)
        {
            pw.insert({sw+fw,sc+fc});
            if(answer<-(sc+fc))
            {
                answer = -(sc+fc);
            }
        }
        else
        {
            itr--;
        }
    }


    return answer;
}