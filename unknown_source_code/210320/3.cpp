#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;


map<int,int>me;
map<int,int>ml;
int graph[1001][1001];

vector<int> solution(vector<int> enter, vector<int> leave) {
    vector<int> answer;
    for(int i=0;i<enter.size();i++)
    {
        me.insert({enter[i],i});
        ml.insert({leave[i],i});
    }
    for(int i=0;i<enter.size();i++)
    {
        int lastIdx = i;
        for(int j=i+1;j<enter.size();j++)
        {
            if(ml[enter[i]]>ml[enter[j]])
            {
                lastIdx = j;
            }
        }
        if(lastIdx != i)
        {
            for(int j=i+1;j<=lastIdx;j++)
            {
                graph[enter[i]][enter[j]] = 1;
                graph[enter[j]][enter[i]] = 1;
            }
        }
    }
    for(int i=0;i<enter.size();i++)
    {
        int sum = 0;
        for(int j=0;j<enter.size();j++)
        {
            sum+=graph[i+1][j+1];
        }
        answer.push_back(sum);
    }
    return answer;
}