def solution(table, languages, preference):
    answer = ''
    tables = {}
    scores = {}
    result = []
    for l in range(len(languages)):
        scores[languages[l]] = preference[l]
    for t in table:
        t = t.split()
        k = t[0]
        v = t[1:]
        d = {}
        for idx, val in enumerate(v):
            d[val] = len(v)-idx
        tables[k] = d
    for k, v in tables.items():
        score = 0
        for ks, vs in scores.items():
            if v.get(ks):
                score += v[ks]*vs
        result.append((score,k))
    result = sorted(result, key=lambda x : (-x[0],x[1]))
    answer = result[0][1]
    return answer