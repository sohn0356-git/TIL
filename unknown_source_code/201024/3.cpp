#include <iostream>
#include <sstream>
#include <string>
#include <stack>
#include <map>

using namespace std;

stack<int>pos;
map<int, int>connected;
string transform(string str);
void print(string str, int start, int end, bool opened, char open_char);

void solution(int numOfOrder, string* orderArr) {
    // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
    for (int i = 0; i < numOfOrder; i++)
    {
        connected.clear();
        string target = orderArr[i];
        for (int i = 0; i < target.length(); i++)
        {
            if (target[i] == '(')
            {
                pos.push(i);
            }
            else if (target[i] == ')')
            {
                int prev = pos.top();
                pos.pop();
                connected.insert({ prev,i });
            }
        }
        cout << transform(target);
        cout << '\n';
    }
}

string transform(string str)
{
    string ret = str;
    for (auto itr = connected.rbegin(); itr != connected.rend(); itr++)
    {
        int op_start = itr->first;
        if (ret[op_start - 1] >= 'A' && ret[op_start - 1] <= 'Z')
        {
            string target = ret.substr(op_start - 1, 1);
            ret.erase(ret.begin() + op_start);
            while (ret[op_start+1] != ')')
            {
                op_start++;
                ret.insert(op_start, target);
                op_start++;
            }
            ret.erase(ret.begin() + op_start+1);
        }
        else
        {
            int op_end =-1;
            for (int j = op_start + 1; j < str.length(); j++)
            {
                if (str[j] == ')')
                {
                    op_end = j;
                    break;
                }
            }
            if (op_end != -1)
            {
                string target = ret.substr(op_start + 1, op_end - op_start - 1);
                int cnt = ret[op_start - 1] - '0' - 1;
                ret.erase(ret.begin() + op_end);
                ret.erase(ret.begin() + op_start);
                ret.erase(ret.begin() + op_start - 1);
                
                while (cnt--)
                {
                    ret.insert(op_start-1, target);
                }
            }
        }
    }
    return ret;
}

void print(string str, int start, int end, bool opened, char open_char)
{
    for (int i = start; i <= end; i++)
    {
        if (opened)
        {
            cout << open_char;
        }
        if (str[i] >= 'A' && str[i] <= 'Z')
        {
            cout << str[i];
        }
        else if (str[i] == '(')
        {
            if (str[i - 1] >= 'A' && str[i - 1] <= 'Z')
            {
                print(str, str[i], connected[str[i]],true,str[i-1]);
            }
            
        }
        else if (str[i] == ')')
        {
            continue;
        }
        else
        {
            if (str[i + 1] >= 'A' && str[i + 1] <= 'Z')
            {
                for (int j = 0; j < str[i] - '0'; j++)
                {
                    cout << str[i + 1];
                }
                i++;
            }
            else
            {
                for (int j = 0; j < str[i] - '0'; j++)
                {
                    print(str, i + 1, connected[i + 1], false, 'A');
                }
                i = connected[i + 1];
            }
        }
   }
}

struct input_data {
    int numOfOrder;
    string* orderArr;
};

void process_stdin(struct input_data& inputData) {
    string line;
    istringstream iss;

    getline(cin, line);
    iss.str(line);
    iss >> inputData.numOfOrder;

    inputData.orderArr = new string[inputData.numOfOrder];
    for (int i = 0; i < inputData.numOfOrder; i++) {
        getline(cin, line);
        iss.clear();
        iss.str(line);
        iss >> inputData.orderArr[i];
    }
}

int main() {
    struct input_data inputData;
    process_stdin(inputData);

    solution(inputData.numOfOrder, inputData.orderArr);
    return 0;
}
