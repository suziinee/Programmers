def solution(prices):
    answer = []
    
    from collections import deque
    queue = deque(prices)
    
    while len(queue) >= 2 :
        count = 0
        price = queue.popleft()
        for q in queue :
            if q >= price :
                count += 1
            else :
                answer.append(count + 1)
                break
        else :
            answer.append(count)
    
    answer.append(0)
    
    return answer