def solution(s):
    
    s = s[1:-1]
    s = s.split('}')
    s = [i for i in s if i]
    
    for i in range(len(s)) :
        if i == 0 :
            s[i] = s[i][1:]
        else :
            s[i] = s[i][2:]
    
    s = [list(map(int, i.split(','))) for i in s]
    s = sorted(s, key = lambda x : len(x))
    
    ans = []
    for i in s :
        ans.append(list(set(i) - set(ans))[0])
    return ans
    