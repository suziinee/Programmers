def solution(clothes) :

    from collections import defaultdict
    d = defaultdict(int)

    for c in clothes :
        d[c[1]] += 1
    
    combs = set()
    from itertools import combinations
    for i in range(1, len(d) + 1) :
        combs |= set(combinations(d.keys(), i))
    
    combs = list(combs)
    ans = 0
    for c in combs :
        mul = 1
        for i in c :
            mul *= d[i]
        ans += mul
        
    return ans

