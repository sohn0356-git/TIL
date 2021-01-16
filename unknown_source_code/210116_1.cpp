#include <map>

map<int,long> jeans;
map<int,long> shoes;
map<int,long> skirts;
map<int,long> tops;

void init(vector<int> priceOfJeans, vector<int> priceOfShoes, vector<int> priceOfSkirts, vector<int> priceOfTops) {
    for(int i=0;i<priceOfJeans.size();i++)
    {
        if(jeans.find(priceOfJeans[i])==jeans.end())
        {
            jeans[priceOfJeans[i]]=1;
        }
        else
        {
            jeans[priceOfJeans[i]]++;
        }
    }
    for(int i=0;i<priceOfShoes.size();i++)
    {
        if(shoes.find(priceOfShoes[i])==shoes.end())
        {
            shoes[priceOfShoes[i]]=1;
        }
        else
        {
            shoes[priceOfShoes[i]]++;
        }
    }
    for(int i=0;i<priceOfSkirts.size();i++)
    {
        if(skirts.find(priceOfSkirts[i])==skirts.end())
        {
            skirts[priceOfSkirts[i]]=1;
        }
        else
        {
            skirts[priceOfSkirts[i]]++;
        }
    }
    for(int i=0;i<priceOfTops.size();i++)
    {
        if(tops.find(priceOfTops[i])==tops.end())
        {
            tops[priceOfTops[i]]=1;
        }
        else
        {
            tops[priceOfTops[i]]++;
        }
    }
}

long getNumberOfOptions(vector<int> priceOfJeans, vector<int> priceOfShoes, vector<int> priceOfSkirts, vector<int> priceOfTops, int budgeted) {
    long answer = 0;
    init(priceOfJeans,priceOfShoes,priceOfSkirts,priceOfTops);
    for(auto itr1 = jeans.begin();itr1!=jeans.end();itr1++)
    {
        int newBudget = budgeted - itr1->first;
        if(newBudget>0)
        {
            for(auto itr2 = shoes.begin();itr2!=shoes.end();itr2++)
            {
                int newBudget1 = newBudget - itr2->first;
                if(newBudget>0)
                {
                    for(auto itr3 = skirts.begin();itr3!=skirts.end();itr3++)
                    {
                        int newBudget2 = newBudget1 - itr3->first;
                        if(newBudget>0)
                        {
                            for(auto itr4 = tops.begin();itr4!=tops.end();itr4++)
                            {
                                int newBudget3 = newBudget2 - itr4->first;
                                if(newBudget3>=0)
                                {
                                    answer += (itr1->second)*(itr2->second)*(itr3->second)*(itr4->second);
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return answer;
}