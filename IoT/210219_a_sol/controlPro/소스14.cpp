//#include <iostream>
//#include <vector>
//
//using namespace std;
//
//int N, M, K;
//long long a, b, c;
//
//void update(vector<long long>& tree, int idx, long long diff);
//long long sum(vector<long long>& tree, int idx);
//
//int main()
//{
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//	cin >> N >> M >> K;
//	vector<long long> tree(N + 1);
//	for (int i = 0; i < N; i++)
//	{
//		cin >> a;
//		update(tree, i + 1, a);
//	}
//	for (int i = 0; i < M + K; i++)
//	{
//		cin >> a >> b >> c;
//		if (a == 1)
//		{
//			long long target = sum(tree, b) - sum(tree, b - 1);
//			update(tree, b, c - target);
//		}
//		else
//		{
//			cout << sum(tree, c) - sum(tree, b-1) << '\n';
//		}
//	}
//
//	return 0;
//}
//
//void update(vector<long long>& tree, int idx, long long diff)
//{
//	while (idx <= N)
//	{
//		tree[idx] += diff;
//		idx += (idx & -idx);
//	}
//}
//
//long long sum(vector<long long>& tree, int idx)
//{
//	long long ans = 0;
//	while (idx > 0)
//	{
//		ans += tree[idx];
//		idx -= (idx & -idx);
//	}
//	return ans;
//}