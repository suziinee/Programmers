def solution(orders, course) :

    from itertools import combinations
    from collections import Counter
    ans = []

    for n in course :
        combs = []
        for order in orders :
            if len(order) >= n :
                combs.extend(list(combinations(order, n)))
        if combs : 
            combs = [''.join(sorted(list(c))) for c in combs]
            C = Counter(combs)
            max_value = max(C.values())
            if max_value == 1 :
                continue
            else :
                res = [k for k, v in C.items() if v == max_value]
                ans.extend(res)
    
    ans.sort()
    return ans