def solution(participant, completion) :

    hash = set(participant) - set(completion)
    from collections import defaultdict
    p_hash = defaultdict(int)

    if len(hash) == 1 :
        return list(hash)[0]
    else :
        for p in participant :
            p_hash[p] += 1
        for k, v in p_hash.items() :
            if v == 2 :
                return k
