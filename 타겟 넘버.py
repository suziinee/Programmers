def solution(numbers, target):
    
    numbers = [[x, -x] for x in numbers]
    
    n = len(numbers)
    from itertools import product
    prods = list(product([0, 1], repeat = n))
    
    ans = 0
    for prod in prods :
        res = sum([numbers[i][prod[i]] for i in range(n)])
        if res == target :
            ans += 1
        
    return ans
                 