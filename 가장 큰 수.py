def solution(numbers) :
    
    def changing(n) :
        n = str(n)
        if len(n) == 1 :
            n = n * 4
        elif len(n) == 2 :
            n = n * 2
        elif len(n) == 3 :
            n = n + n[0]
        return n #string
    
    from collections import defaultdict
    d = defaultdict(list) #string : [원래 숫자]
    for x in numbers :
        d[changing(x)].append(x)
    
    for k, v in d.items() :
        d[k] = ''.join(list(map(str, v)))

    res = sorted(d.items(), reverse = True)
    
    ans = ''
    for r in res :
        ans += str(r[1])
    
    return str(int(ans))