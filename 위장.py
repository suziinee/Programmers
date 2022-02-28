def solution(clothes) :

    from collections import defaultdict
    d = defaultdict(list)

    for c in clothes :
        d[c[1]].append(d[c[0]])
    d = {key : len(value) for key, value in d.items()}
    
    combs = set()
    from itertools import combinations
    for i in range(1, len(d) + 1) :
        combs |= set(combinations(d.keys(), i))
    
    combs = list(combs)
    ans = 0
    from functools import reduce
    for c in combs :
        c_list = [d[c[i]] for i in range(len(c))]
        ans += reduce(lambda x, y : x * y, c_list)
        
    return ans

