def solution(info, query) :

    info_dict = {}
    ans = []

    for i, v in enumerate(info) :
        info_dict[i] = v.split()
    
    query = [[x for x in q.split() if x not in ['and', '-']] for q in query]
    
    for q in query :
        score = q.pop()
        cnt = 0
        for k, v in info_dict.items() :
            if set(q) - set(v) == set() :
                if int(v[-1]) >= int(score) : 
                    cnt += 1
        ans.append(cnt)
        
    return ans