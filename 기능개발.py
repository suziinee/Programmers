def solution(progresses, speeds) : 
    answer = []

    while progresses :
        cnt = 0 
        progresses = [x - y for x, y in zip(progresses, speeds)]
        for i in progresses[:] :
            if cnt == 0  and i > 0 :
                break 
            elif i <= 0 :
                cnt += 1
                progresses.pop(0)
                continue 
            elif cnt >= 1 and i > 0 :
                answer.append(cnt)
                break 
    answer.append(cnt)
                
    return answer