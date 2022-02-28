def solution(numbers, hand) :

    res = ""

    l = (3, 0)
    r = (3, 2)

    d = {1:(0, 0), 2:(0, 1), 3:(0, 2), 4:(1, 0), 5:(1, 1), 6:(1, 2), 
    7:(2, 0), 8:(2, 1), 9:(2, 2), 0:(3, 1)}

    for num in numbers :
        if num in [1, 4, 7] :
            res += "L"
            l = d[num]
        elif num in [3, 6, 9] :
            res += "R"
            r = d[num]
        else :
            x = d[num][0]
            y = d[num][1]

            l_len = abs(l[0] - x) + abs(l[1] - y)
            r_len = abs(r[0] - x) + abs(r[1] - y)

            if l_len > r_len :
                res += "R"
                r = d[num]
            elif l_len < r_len :
                res += "L"
                l = d[num]
            else :
                if hand == "right" :
                    res += "R"
                    r = d[num]
                else :
                    res += "L"
                    l = d[num]
    
    return res


