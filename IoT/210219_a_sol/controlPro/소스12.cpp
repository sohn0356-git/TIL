//#include <iostream>
//#include <queue>
//
//using namespace std;
//
//int N;
//int visited[1000001];
//
//int main()
//{
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//	cin >> N;
//	queue<pair<int,int>>q;	//cur cnt
//	q.push({ N,0 });
//	while (!q.empty())
//	{
//		pair<int,int> cur = q.front();
//		q.pop();
//		if (cur.first == 1)
//		{
//			cout << cur.second;
//			break;
//		}
//		if (cur.first - 1 > 1)
//		{
//			if (visited[cur.first - 1] == 0)
//			{
//				q.push({ cur.first - 1, cur.second + 1 });
//				visited[cur.first - 1] = 1;
//			}
//		}
//
//		if (cur.first % 2 == 0)
//		{
//			if (visited[cur.first / 2] == 0)
//			{
//				q.push({ cur.first / 2, cur.second + 1 });
//				visited[cur.first / 2] = 1;
//			}
//		}
//
//		if (cur.first % 3 == 0)
//		{
//			if (visited[cur.first / 3] == 0)
//			{
//				q.push({ cur.first / 3, cur.second + 1 });
//				visited[cur.first / 3] = 1;
//			}
//		}
//	}
//	return 0;
//}