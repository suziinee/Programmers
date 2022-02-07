def solution(n):
    
    def three(n) : # n은 int
        ans = ''
        while n >= 3 :
            ans += str(n%3)
            n = n//3
        ans += str(n)
        return ans
    
    n = three(n)[::-1]
    
    def rollback(n) : # n은 string
        ans = 0
        for i in range(len(n)) :
            ans += (3 ** i) * int(n[i])
        return ans
    
    return rollback(n)