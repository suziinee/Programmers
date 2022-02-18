def solution(numbers):
    
    d = {int(x[0]) : [] for x in list(map(str, numbers))}
    
    for i in list(map(str, numbers)) :
        d[int(i[0])].append(int(i))
    
    from itertools import permutations
    
    for key, value in d.items() :
        if len(value) != 1 :
            res = []
            perms = list(permutations(value, len(value)))
            for perm in perms :
                res.append(int(''.join(list(map(str, perm)))))
            d[key] = max(res)
        else :
            d[key] = value[0]
            
    ans = ''
    for key in sorted(d.keys(), reverse = True) :
        ans += str(d[key])
        
    return ans