def solution(info, query) :

    info_dict = {}
    ans = []

    for i, v in enumerate(info) :
        info_dict[i] = v.split()
    
    query = [[x for x in q.split() if x not in ['and', '-']] for q in query]

    # 점수 정렬
    info_dict = sorted(info_dict.items(), key = lambda x : int(x[1][-1]))

    # 점수만 따로 빼기
    scores = [int(x[1][-1]) for x in info_dict]

    from bisect import bisect_left
    
    for q in query :
        score = int(q.pop())
        idx = bisect_left(scores, score)
        cnt = 0
        for x in info_dict[idx:] :
            if set(q) - set(x[1]) == set() :
                cnt += 1
        ans.append(cnt)

    return ans