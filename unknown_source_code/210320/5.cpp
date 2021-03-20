// program: string
// 1 <= program의 길이 <= 10
// 실행할 프로그램의 이름입니다.
// 공백처리는 하지 않아도 됩니다.
// flag_rules: [flag_rule]
// 1 <= flag_rules의 길이 <= 100
// flag_rule: "<flag_name> <flag_argument_type>"
// flag_name: string
// 2 <= flag_name의 길이 <= 10
// flag_name은 '-'(dash)로 시작하고, 영어 대소문자로만 이루어져 있습니다.
// 동일한 flag_name에 대한 처리는 하지 않아도 됩니다.
// flag_argument_type: "NULL" | "NUMBER" | "STRING"
// "NULL": flag argument를 받지 않습니다.
// "NUMBER": 0부터 9까지의 숫자로만 이루어진 flag argument를 받습니다.
// "STRING": 알파벳 대소문자로만 이루어진 flag argument를 받습니다.
// commands: [command]
// 1 <= commands의 길이 <= 100
// 1 <= command의 길이 <= 100
// command는 하나의 program과 여러 flag가 string 형태로 이어져 있고, 이들은 공백으로 구분됩니다.
// 연속되는 공백도 공백처리를 하지 않아도 됩니다.
// 출력 형식
// answer: boolean[]
// commands의 순서대로 각 command를 판단하여 boolean 배열을 반환합니다.
// command가 아래 조건을 모두 만족하면 True, 만족하지 않으면 False를 반환합니다.
// program으로 시작합니다.
// 각 flag argument는 대응하는 flag의 flag_argument_type과 일치합니다.
// 각 flag는 0번이나 1번 나타납니다.
// flag_rules에 존재하는 flag만 나타납니다.

#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <iostream>


using namespace std;

map<string,string> rules;
map<string, int> flag_cnt;
vector<string> split(string input, char delimiter);

vector<bool> solution(string program, vector<string> flag_rules, vector<string> commands) {
    vector<bool> answer;

    for(int i=0;i<flag_rules.size();i++)
    {
        vector<string> rule = split(flag_rules[i],' ');
        flag_cnt.insert({rule[0], -1});
        rules.insert({rule[0], rule[1]});
    }
    for(int i=0;i<commands.size();i++)
    {
        vector<string>command = split(commands[i],' ');
        if(command[0]!=program)
        {
            answer.push_back(false);
            continue; 
        }       
        for(int j=1;j<command.size();j+=2)
        {
            if(rules.find(command[j])==rules.end())
            {
                answer.push_back(false);
                break;
            }
            string cur = rules[command[j]];
            if(flag_cnt[command[j]]==i)
            {
                answer.push_back(false);
                break;
            }
            if(cur=="STRING")
            {
                flag_cnt[command[j]] = i;
                bool isString = true;
                for(int k=0;k<command[j+1].length();k++)
                {
                    if('a'<= command[j+1][k] && command[j+1][k] <= 'z')
                    {
                        continue;
                    }
                    else if('A'<= command[j+1][k] && command[j+1][k] <= 'Z')
                    {
                        continue;
                    }
                    else
                    {
                        isString = false;
                        break;
                    }
                }
                if(!isString)
                {
                    answer.push_back(false);
                    break;
                }
            }
            else if(cur=="NUMBER")
            {
                flag_cnt[command[j]] = i;
                bool isNum = true;
                for(int k=0;k<command[j+1].length();k++)
                {
                    if('0'<= command[j+1][k] && command[j+1][k] < '9')
                    {
                        continue;
                    }
                    else
                    {
                        isNum = false;
                        break;
                    }
                }
                if(!isNum)
                {
                    answer.push_back(false);
                    break;
                }
            }
            else
            {
                flag_cnt[command[j]] = i;
                j--;
            }
        }
        if(i+1>answer.size())
        {
            answer.push_back(true);
        }
    }
    return answer;
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