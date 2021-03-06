///
/*
길이가 N인 문자열 S가 있다.
문자 사이사이에 aa를 채우고 싶다. a를 넣을 수 있는 최대값을 return하라.
if) aaa in S -> return -1
ex) aa -> return 0
    ab -> return 3 (aabaa)
    bcd -> return 8 (aabaacaadaa)
1<=N<=200000

tmi) 문자열 S가 a로 끝나는 상황의 예외처리만 잘 해주었으면 괜찮을 것같다.
*/
///

#include <string>
using namespace std;

int solution(string &S) {
    // write your code in C++14 (g++ 6.2.0)
    std::string::size_type n;
    n = S.find("aaa");
    int answer = 0;
    if (n != std::string::npos) 
    {
        return -1;
    }
    else
    {
        int cnt=2;
        for(int i=0;i<S.length();i++)
        {
            if(S[i]=='a')
            {
                cnt--;
            }
            else
            {
                answer+=cnt;
                cnt=2;
            }
        }
        if(S.back()!='a')
        {
            answer+=2;
        }
        else 
        {
            if(S.length()==1)
            {
                answer += 1;
            }
            else if(S[S.length()-2]!='a')
            {
                answer += 1
            }
        }
        return answer;
    }
    
}
