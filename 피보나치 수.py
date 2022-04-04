def solution(n):
    
    import sys
    sys.setrecursionlimit(10**7)
    
    d = [0] * 100001
    
    for i in range(n + 1) :
        if i == 1 or i == 2 :
            d[i] = 1
        else :
            d[i] = d[i-1] + d[i-2]
    
    return d[n] % 1234567