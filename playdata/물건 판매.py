def solution(self, price, cost) :

    # 매 가격에 대해서 해당 가격의 물건을 살 수 있는 고객에게서 이윤을 구함
    from collections import defaultdict
    d = defaultdict(list)
    profit = 0
    

    for i in range(len(price)) :

        # 새 가격이 나올때마다 이윤 초기화
        profit = 0

        for j in range(len(cost)) :
            if (price[i] <= price[j]) and (price[i] >= cost[j]) :
                profit += (price[i] - cost[j])
        
        d[profit].append(price[i])
    
    # 더 작은 가격으로 sort
    d = {key : sorted(value) for key, value in d.items()}

    # 최대 이윤의 가장 적은 가격 추출
    return d[max(d.keys())][0]