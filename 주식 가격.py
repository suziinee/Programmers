def solution(prices):
    answer = []
    
    for i in prices[:] :
        if len(prices) == 1 :
            answer.append(0)
            break
        elif prices[0] <= min(prices[1:]) :
            answer.append(len(prices) - 1)
            prices.pop(0)
            continue
        else :
            for j in prices[1:] :
                if j < i :
                    answer.append(prices.index(j))
                    prices.pop(0)
                    break
                    
    return answer