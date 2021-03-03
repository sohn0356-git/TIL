#include <iostream>
#include <string>

using namespace std;


int idx;
string str;

int solve(int stage);

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> str;
	cout << solve(0);
	return 0;
}

int solve(int stage)
{
	if (stage == str.length())
	{
		return 0;
	}
	idx++;
	if (str[stage] == '(')
	{
		int res = 2 * solve(stage + 1);
		return res + solve(idx);
	}
	else if (str[stage] == '[')
	{
		int res = 3 * solve(stage+1);
		return res + solve(idx);
	}
	else if (str[stage] == ')')
	{		
		return 2;
	}
	else if (str[stage] == ']')
	{
		return 3;
	}
}