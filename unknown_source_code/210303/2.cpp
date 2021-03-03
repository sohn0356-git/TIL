#include <iostream>
#include <string>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

const int MINV = -1500000000;

int solution(int n, vector<int> v) {
    int ans = MINV;
    int maxIdx, minIdx;
    bool asc = true;
    maxIdx = 0;
    minIdx = 0;
    for (int i = 0; i < v.size(); i++)
    {
        if (ans < v[maxIdx] - v[minIdx])
        {
            ans = v[maxIdx] - v[minIdx];
        }
        if (v[minIdx] > v[i])
        {
            minIdx = i;
            asc = false;
        }
        if (v[maxIdx] < v[i])
        {
            maxIdx = i;
            minIdx = i;
        }

    }
    if (ans < v[maxIdx] - v[minIdx])
    {
        ans = v[maxIdx] - v[minIdx];
    }
    if (asc)
    {
        ans = MINV;
        for (int i = 1; i < v.size(); i++)
        {
            if (ans < v[i - 1] - v[i])
            {
                ans = v[i - 1] - v[i];
            }
        }
    }
    return ans;
}