def solution(brown, yellow):
    
    def division(n) : # n의 약수 list를 구하는 함수
        l = []
        for i in range(1, n + 1) :
            if n % i == 0 :
                l.append(n // i)
        return sorted(l)
    
    y_list = division(yellow)
    if len(y_list) % 2 == 0 :
        y_list = y_list[:len(y_list) // 2]
    else :
        y_list = y_list[:len(y_list) // 2 + 1]
    
    for i in y_list : # i는 세로 길이
        j = int(yellow / i)
        if (i + 2) * (j + 2) - yellow == brown :
            return [j + 2, i + 2]