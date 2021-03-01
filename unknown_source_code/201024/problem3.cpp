///
/*
길이가 N인 vector A가 있다.
vector A에 1,2,3,...,N까지 모든 숫자가 있었으면 좋겠다.
vector A에 있는 숫자를 +1 or -1을 하여 이 조건을 만족시키는 최소횟수를 return하시오
1000000000보다 답이 클 경우 -1을 return하시오
1<=N<=200000
tmi)맞게 푼건지는 모르겠다.
*/
///


#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int solution(vector<int>&A) {
    // write your code in C++14 (g++ 6.2.0)
    int answer = 0;
    sort(A.begin(),A.end());
    for(int i=1;i<=A.size();i++)
    {
        answer += abs(A[i-1]-i);
        if(answer>1000000000)
        {
            answer = -1;
            break;
        }
    }
    return answer;
}
