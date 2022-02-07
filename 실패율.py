def solution(N, stages):
    answer = {}
    n = len(stages)
    
    for i in range(1, N + 1) :
        if n == 0 :
            answer[i] = 0
        else :
            answer[i] = stages.count(i) / n
            n -= stages.count(i)
                
    import operator
    answer = dict(sorted(answer.items(), key = operator.itemgetter(1), reverse = True))
    
    return list(answer.keys())