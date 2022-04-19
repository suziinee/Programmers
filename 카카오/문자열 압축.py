def solution(s) :

    from itertools import groupby

    def cut(string, n) :
        lst = list(map(''.join, zip(*[iter(string)]*n)))
        rest = string[n * len(lst):]
        
        # n개씩 자른 lst에 대해서 groupby로 개수 세기
        idx = [k for k, g in groupby(lst)]
        v = [len(list(g)) for k, g in groupby(lst)]

        ans = ""
        for i in range(len(idx)) :
            if v[i] == 1 :
                ans += str(idx[i])
            else :
                ans += str(v[i]) + str(idx[i])
        
        return ans + rest
    
    n = len(s)
    ans = []
    for i in range(1, n + 1) :

        ans.append(len(cut(s, i)))
    
    return min(ans)
