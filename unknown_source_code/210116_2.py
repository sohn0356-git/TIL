from collections import deque

def longestChain(words):
    # Write your code here
    answer = 0
    words.sort(key=lambda x:len(x), reverse=True)
    queue = deque()
    # print(words)
    for w in words:
        # if len(w)==1:
        queue.append((1,w))
    while queue:
        cur, word = queue.popleft()
        # print(cur, word)
        if answer < cur:
            answer = cur
        # print('------------')
        # print(word)
        for w in words:
            # print("this time ",w)
            if len(w)>len(word)+1:
                continue
            elif len(w)==len(word)+1:
                d = set(w)-set(word)
                # print(d, word)
                if len(d)<=1:
                    queue.append((cur+1,w))
            else:
                break
    return answer
