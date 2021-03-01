//#include <iostream>
//#include <algorithm>
//#include <string>
//#include <stack>
//
//using namespace std;
//
//int N;
//string M, K;
//int from[10001][10];
//stack < pair<int, int>>st;
//int DP[10001][10];
//int solve(int stage, int cum);
//
//int main()
//{
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//	for (int i = 0; i < 10001; i++)
//	{
//		for (int j = 0; j < 10; j++)
//		{
//			DP[i][j] = -1;
//			from[i][j] = -1;
//		}
//	}
//	cin >> N >> M >> K;
//	cout << solve(0, 0)<<'\n';
//	for (int i = 1; i <= N; i++)
//	{
//		
//	}
//	
//	return 0;
//}
//
//int solve(int stage, int cum)
//{
//	if (stage == N)
//	{
//		return 0;
//	}
//	int& res = DP[stage][cum];
//	if (res != -1)
//	{
//		return res;
//	}
//	int ms = M[stage] - '0';
//	int ks = K[stage] - '0';
//	ms += cum;
//	ms %= 10;
//	int sub1 = ks - ms;
//	//turn left
//	if (sub1 < 0)
//	{
//		sub1 += 10;
//	}
//	int tl = sub1 + solve(stage + 1, (cum + sub1) % 10);
//	//turn right
//	int sub2 = ms - ks;
//	if (sub2 < 0)
//	{
//		sub2 += 10;
//	}
//	int tr = sub2 + solve(stage + 1, cum);
//	if (tr < tl)
//	{
//		from[stage+1][cum] = cum;
//	}
//	else
//	{
//		from[stage+1][cum] = (cum + sub1) % 10;
//	}
//	res = min(tr, tl);
//	return res;
//}