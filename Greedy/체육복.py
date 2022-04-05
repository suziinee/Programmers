def solution(n, lost, reserve):
    all = list(range(1, n + 1))
    
    # reserve도, lost도 아닌 애들
    default = list(set(all) - set(lost) - set(reserve))

    # 여벌이 있는 애가 lost 했다면 여벌, lost에서 제외하기
    for i in reserve[:] :
        if i in lost[:] :
            reserve.remove(i)
            lost.remove(i)
            default.append(i)

    # all = list(set(all) - set(default))
    reserve.sort()
    lost.sort()

    for i in reserve[:] :
        print(i)
        if i != 1 :
            if i-1 in lost :
                # i-1이 우선권을 가짐
                lost.remove(i-1)
                reserve.remove(i)
                default.append(i)
                default.append(i-1)
                continue
            elif i+1 in lost :
                lost.remove(i+1)
                reserve.remove(i)
                default.append(i)
                default.append(i+1)
                continue
        elif i == 1 :
            if 2 in lost :
                lost.remove(2)
                reserve.remove(1)
                default.append(1)
                default.append(2)
              
    # 여벌에 있는 양수 애들 default에 넣어주기
    for i in reserve :
        default.append(i)
    
		return len(default)