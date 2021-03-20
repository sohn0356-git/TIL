answer = [0,0]  #인원수, 몸무게 합

def solve(weight, stage,a,b,c):
    global answer
    if stage==len(weight):
        if a and b:
            if sum(a)==sum(b):
                len_sum = len(a) + len(b)
                if answer[0]<=len_sum:
                    if answer[0]==len_sum and answer[1]>sum(a):
                        pass
                    else:
                        answer = [len_sum,sum(a)]
        return
    a.append(weight[stage])
    solve(weight,stage+1,a,b,c)
    a.pop()
    b.append(weight[stage])
    solve(weight,stage+1,a,b,c)
    b.pop()
    c.append(weight[stage])
    solve(weight,stage+1,a,b,c)
    c.pop()

def solution(weight):

    solve(weight, 0,[],[],[])
    return answer