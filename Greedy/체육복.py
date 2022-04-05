def solution(n, lost, reserve) :
    
    lost = set(lost)
    reserve = set(reserve)

    # rest : 체육복 문제가 해결된 아이들
    rest = set(range(1, n + 1))

    # lost에 있는 아이들 빼기
    rest -= lost

    # lost에 있는 아이들 중에 reserve가 있는 아이들은 빌려줄 수 없음
    lost_reserve = set([x for x in lost if x in reserve])
    lost -= lost_reserve 
    reserve -= lost_reserve
    rest.update(lost_reserve)

    # lost_dict {lost : [lost + 1, lost - 1]}
    lost_dict = {x : [x-1, x+1] for x in lost}
    for l in list(lost) :
        if lost_dict[l][0] in reserve :
            lost -= set([l])
            reserve -= set([l - 1])
            rest.update(set([l]))
            continue
        elif lost_dict[l][1] in reserve :
            lost -= set([l])
            reserve -= set([l + 1])
            rest.update(set([l]))
            continue
    
    return len(rest)