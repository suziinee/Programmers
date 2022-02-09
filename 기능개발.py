def solution(progresses, speeds) : 
    answer = []
    cnt = 0
    
    progresses = [100-x for x in progresses]

    while progresses :
        progresses = [x - y for x, y in zip(progresses, speeds)]
        for i in progresses[:] :
            if i <= 0 :
                cnt += 1
                progresses.pop(0)
                continue
            else :
                break
        if cnt >= 1 :
            answer.append(cnt)
            cnt = 0
                
    return answer

