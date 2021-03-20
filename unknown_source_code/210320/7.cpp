#include <string>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

map<string, string> rules;
map<string, int> flag_cnt;
vector<string> split(string input, char delimiter);

vector<bool> solution(string program, vector<string> flag_rules, vector<string> commands) {
    vector<bool> answer;

    for (int i = 0; i < flag_rules.size(); i++)
    {
        vector<string> rule = split(flag_rules[i], ' ');
        if (rule.size() == 2)
        {
            rules.insert({ rule[0], rule[1] });
            flag_cnt.insert({rule[0], -1});
        }
        else
        {
            rules.insert({ rule[0], rule[2] });
            flag_cnt.insert({rule[0], -1});
        }
    }
    for (int i = 0; i < commands.size(); i++)
    {
        vector<string>command = split(commands[i], ' ');
        if (command[0] != program)
        {
            answer.push_back(false);
            continue;
        }
        for (int j = 1; j < command.size(); j += 2)
        {
            if (rules.find(command[j]) == rules.end())
            {
                answer.push_back(false);
                break;
            }
            string cmd = rules[command[j]];
            if(flag_cnt[command[j]]==i)
            {
                answer.push_back(false);
                break;
            }
            flag_cnt[command[j]]= i;
            while (rules.find(cmd) != rules.end())
            {
                if(flag_cnt[cmd]==i)
                {
                    break;
                }
                flag_cnt[cmd] = i;
                cmd = rules[cmd];
            }
            if(rules.find(cmd) != rules.end())
            {
                answer.push_back(false);
                break;
            }
            if (cmd == "STRINGS")
            {
                bool isString = true;
                while (j + 1 < command.size())
                {
                    if (rules.find(command[j + 1]) != rules.end()) {
                        j--;
                        break;
                    }
                    for (int k = 0; k < command[j + 1].length(); k++)
                    {
                        if ('a' <= command[j + 1][k] && command[j + 1][k] <= 'z')
                        {
                            continue;
                        }
                        else if ('A' <= command[j + 1][k] && command[j + 1][k] <= 'Z')
                        {
                            continue;
                        }
                        else
                        {
                            isString = false;
                            break;
                        }
                    }
                    j++;
                }
                if (!isString)
                {
                    answer.push_back(false);
                    break;
                }
            }
            else if (cmd == "NUMBERS")
            {
                bool isNum = true;
                while (j + 1 < command.size())
                {
                    if (rules.find(command[j + 1]) != rules.end()) {
                        j--;
                        break;
                    }
                    for (int k = 0; k < command[j + 1].length(); k++)
                    {
                        if ('0' <= command[j + 1][k] && command[j + 1][k] <= '9')
                        {
                            continue;
                        }
                        else
                        {
                            isNum = false;
                            break;
                        }
                    }
                    j++;
                }
                if (!isNum)
                {
                    answer.push_back(false);
                    break;
                }
            }
            else if (cmd == "STRING")
            {
                bool isString = true;
                for (int k = 0; k < command[j + 1].length(); k++)
                {
                    if ('a' <= command[j + 1][k] && command[j + 1][k] <= 'z')
                    {
                        continue;
                    }
                    else if ('A' <= command[j + 1][k] && command[j + 1][k] <= 'Z')
                    {
                        continue;
                    }
                    else
                    {
                        isString = false;
                        break;
                    }
                }
                if (!isString)
                {
                    answer.push_back(false);
                    break;
                }
            }
            else if (cmd == "NUMBER")
            {
                bool isNum = true;
                for (int k = 0; k < command[j + 1].length(); k++)
                {
                    if ('0' <= command[j + 1][k] && command[j + 1][k] < '9')
                    {
                        continue;
                    }
                    else
                    {
                        isNum = false;
                        break;
                    }
                }
                if (!isNum)
                {
                    answer.push_back(false);
                    break;
                }
            }
            else
            {
                j--;
            }
        }
        if (i + 1 > answer.size())
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