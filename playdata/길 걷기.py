def solution(X, Y, walkTime, sneakTime) :
    
    # 걷기 * 2 < 건너기 : 걷는다
    if walkTime * 2 <= sneakTime :
        return (X + Y) * walkTime
    
    # 걷기 * 2 > 건너기 
    if walkTime * 2 > sneakTime :
        min_ = min(X, Y)
        max_ = max(X, Y)
         
        # 걷기 > 건너기 : 무조건 건넌다
        if walkTime > sneakTime :
             # x, y 합이 짝수이면 큰값만큼 건너기
            if (X + Y) % 2 == 0 :
                 return max_ * sneakTime
            # 홀수면 큰값 - 1만큼 건너고 한번은 걷기
            else :
                return (max_-1) * sneakTime + walkTime
    
        # 걷기 < 건너기 : 건널 수 있으면 건너고 나머지 경우는 걷기
        else :
            # x, y 중 작은값만큼 건너고 나머지는 걷기
            return min_ * sneakTime + (max_ - min_) * walkTime


    