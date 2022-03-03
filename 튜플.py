def solution(s):
    
    s = s[2:-2]
    s = s.split('},{')
    
    s = [list(map(int, i.split(','))) for i in s]
    s = sorted(s, key = lambda x : len(x))
    
    ans = []
    for i in s :
        ans.append(list(set(i) - set(ans))[0])
    return ans
    