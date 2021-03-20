#include <string>
#include <vector>
#include <map>
#include <set>
using namespace std;

map<char,int>m;
set<int>res;
vector<int> solution(string inp_str) {
    vector<int> answer;
    int upper = 0;
    int lower = 0;
    int num = 0;
    int special = 0;
    //1
    if(inp_str.size()<8 || inp_str.size()>15)
    {
        res.insert(1);
    }

    for(int i=0;i<inp_str.size();i++)
    {
        //2
        char cur = inp_str[i];
        if('a'<=cur && cur <= 'z')
        {
            lower = 1;
        }
        else if('A'<=cur && cur <= 'Z')
        {
            upper = 1;
        }
        else if('0'<=cur && cur <= '9')
        {
            num = 1;
        }
        else if(cur=='~' || cur=='!' || cur=='@' || cur=='#' || cur=='$' || cur=='%' ||cur=='^' ||cur=='&' ||cur=='*')
        {
            special = 1;
        }
        else
        {
            res.insert(2);
        }
        //4
        if(i>2 && inp_str[i]==inp_str[i-1] && inp_str[i]==inp_str[i-2] && inp_str[i] == inp_str[i-3])
        {
            res.insert(4);
        }
        //5
        if(m.find(cur)==m.end())
        {
            m.insert({cur,1});
        }
        else
        {
            m[cur]++;
            if(m[cur]==5)
            {
                res.insert(5);
            }
        }
    }
    if(upper+lower+num+special<3)
    {
        res.insert(3);
    }
    if(res.size()==0)
    {
        answer.push_back(0);
    }
    else
    {
        for(auto itr = res.begin(); itr!=res.end(); itr++)
        {
            answer.push_back(*itr);
        }
    }    
    return answer;
}