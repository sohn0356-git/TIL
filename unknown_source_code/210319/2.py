def solution(gift_cards, wants):
    answer = 0
    cards = {}
    for g in gift_cards:
        if cards.get(g):
            cards[g] += 1
        else:
            cards[g] = 1
    for w in wants:
        if cards.get(w):
            if cards[w]>0:
                cards[w] -= 1
            else:
                answer += 1
        else:
            answer += 1
    return answer