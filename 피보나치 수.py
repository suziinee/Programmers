def solution(n):
    
    d = [0] * 100

    def fibo(x) :
        if x == 1 or x == 2 :
            d[x] = 1
        if d[x] != 0 :
            return d[x]
        d[x] = d[x-1] + d[x-2]
        return d[x]
    
    fibo(n)