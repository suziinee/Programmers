def solution(numbers, target):
    
    for i in range(len(numbers)) :
        numbers[i] = [numbers[i], -numbers[i]]
    
    c = [0, 1]
    n = len(numbers)
    from itertools import product
    prods = list(product(c, repeat = n))
    
    ans = 0
    for prod in prods :
        res = 0
        for i in range(n) :
            res += numbers[i][prod[i]]
        if res == target :
            ans += 1
        
    return ans
                 