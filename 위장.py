def solution(clothes) :

    from collections import defaultdict
    d = defaultdict(int)

    for c in clothes :
        d[c[1]] += 1
    
    ans = 1
    for value in d.values() :
        ans *= (value + 1)
    
    return ans - 1

