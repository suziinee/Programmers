def solution(participant, completion) :

    hash = set(participant) - set(completion)
    from collections import defaultdict
    p_hash = defaultdict(int)
    c_hash = defaultdict(int)

    if len(hash) == 1 :
        return list(hash)[0]
    else :
        for p in participant :
            p_hash[p] += 1
        for c in completion :
            c_hash[c] += 1
        
        for k in p_hash.keys() :
            if p_hash[k] != c_hash[k] :
                return k
        
