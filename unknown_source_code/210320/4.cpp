#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;

struct str{
    string name;
    int id;
    int parent;
    vector<int> k;
    str(){}
    str(string _name, int _id, int _parent, vector<int> _k):name(_name), id(_id), parent(_parent), k(_k){}
};

int indegree[1001];
string word;
bool cmp(str left, str right);
vector<string> split(string str, char delimiter);
vector<int> make_nested(string P);
vector<int> KMP(string S, string P);
vector<str> datas;
str tree[1001];
vector<string> solution(vector<string> data, string _word) {
    vector<string> answer;
    word = _word;
    for (int i = 0; i < data.size(); i++)
    {
        vector<string> result = split(data[i], ' ');
        vector<int>k = KMP(result[1], word);
        tree[stoi(result[0])] = str(str(result[1], stoi(result[0]), stoi(result[2]), k));
        datas.push_back(str(str(result[1], stoi(result[0]), stoi(result[2]), k)));
        indegree[stoi(result[2])]++;
    }
    sort(datas.begin(), datas.end(), cmp);
    for (int i = 0; i < data.size(); i++)
    {
        vector<string>tmp;
        string answer_tmp = "";
        if (datas[i].k.size() > 0 && indegree[datas[i].id]==0)
        {
            str cur = datas[i];
            tmp.push_back(cur.name);
            while(cur.parent!=0)
            {
                cur = tree[cur.parent];
                tmp.push_back(cur.name);
            }
            while(!tmp.empty())
            {
                answer_tmp += tmp.back()+"/";
                tmp.pop_back();
            }
            answer_tmp.pop_back();
            answer.push_back(answer_tmp);
        }
    }
    if (answer.empty())
    {
        answer.push_back("Your search for (" + word + ") didn't return any results");
    }
    return answer;
}


vector<int> make_nested(string P)
{
    int len_P = P.length();
    int idx = 0;
    vector<int> nested(len_P);
    for (int i = 1; i < len_P; i++)
    {
        while (idx > 0)
        {
            if (P[i] == P[idx])
            {
                break;
            }
            idx = nested[idx - 1];
        }
        if (P[i] == P[idx])
        {
            nested[i] = ++idx;
        }
    }
    return nested;
}
vector<int> KMP(string S, string P)
{
    int idx = 0;
    int len_S = S.length();
    int len_P = P.length();
    vector<int>nested = make_nested(P);
    vector<int>ans;
    for (int i = 0; i < len_S; i++)
    {
        while (idx > 0)
        {
            if (S[i] == P[idx])
            {
                break;
            }
            idx = nested[idx - 1];
        }
        if(S[i]==P[idx])
        {
            if (idx == len_P - 1)
            {
                ans.push_back(i - (len_P - 1));
                idx = nested[idx];
            }
            else
            {
                idx++;
            }
        }
    }
    return ans;
}

vector<string> split(string input, char delimiter) {
    vector<string> answer;
    stringstream ss(input);
    string temp;

    while (getline(ss, temp, delimiter)) {
        answer.push_back(temp);
    }

    return answer;
}

bool cmp(str left, str right)
{
    if(left.k.size()>0 && right.k.size()>0)
    {
        if(word.length()==left.name.length() && word.length()==right.name.length())
        {
            return left.id<right.id;
        }
        else if(word.length()==left.name.length())
        {
            return true;
        }
        else if(word.length()==right.name.length())
        {
            return false;
        }
        if(left.k.size()>right.k.size())
        {
            return true;
        }
        else if(left.k.size()<right.k.size())
        {
            return false;
        }
        for(int i=0;i<left.k.size();i++)
        {
            if(left.k[i]<right.k[i])
            {
                return true;
            }
            else if(left.k[i]>right.k[i])
            {
                return false;
            }
        }
        return left.id<right.id;
    }
    else if(left.k.size()>0)
    {
        return true;
    }
    else if(right.k.size()>0)
    {
        return false;
    }
    else
    {
        return false;
    }
}