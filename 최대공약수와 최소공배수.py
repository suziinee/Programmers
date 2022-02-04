def solution(n, m):
    answer = []
    
    #최대공약수
    max_temp = 0
    for i in range(1, min(n, m) + 1) :
        if n % i == 0 and m % i == 0 :
            max_temp = i
    answer.append(max_temp)
    
    #최소공배수
    min_temp = 1
    while (min_temp % n != 0) or (min_temp % m != 0) :
        min_temp += 1
    answer.append(min_temp)
    
    return answer