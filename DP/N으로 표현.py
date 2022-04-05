"""
문제 풀이 방법
- 주어진 N을 1번 사용할 때부터 최대 8번 사용할 때까지 반복해서 사칙연산을 한다.
    1번 사용할 때는 그냥 N
    2번 사용할 때, ex: N=5, 5*5, 5+5, 5-5, 5/5 가 되므로
    2번일 때는 1번 (op) 1번 : op -> +, -, *, /
    3번일 때는 1번 (op) 2번, 2번 (op) 1번 ** 반대도 해주어야 빼기와 나누기가 계산됨
    4번일 때는 1번 (op) 3번, 2번 (op) 2번, 3번 (op) 1번
    N일 때는 1 (op) N-1, 2 (op) N-2, 3 (op) N-3,... N-1 (op) 1 까지 계산해 준다.
    매번 계산 할 때마다 결과를 set()에 넣어 주어 중복값을 없앤다.

- 1번에 계산된 값을 2번에서 사용하고 2번에 계산된 값을 3에서 사용하는 방법으로 계산
- 큰 값을 잘게 나누어 계산 하고 그 결과를 재사용할 수 있으며, 계산되는 값들이 겹치므로 DP에 해당.
"""

def solution(N, number) :

    if number == N :
        return 1

    def calculate_n(X, Y) :
        n_set = set()
        for x in X :
            for y in Y :
                n_set.add(x + y)
                n_set.add(x - y)
                n_set.add(x * y)
                if y != 0 :
                    n_set.add(x // y) # 어짜피 모두 나누어 떨어짐
        return n_set
    
    answer = -1
    result = {} # N을 key번 사용했을때 나오는 연산 결과 set, value
    result[1] = {N}

    for n in range(2, 9) : 
        i = 1
        temp_set = {int(str(N) * n)}
        while i < n :
            temp_set.update(calculate_n(result[i], result[n - i]))
            i += 1
        if number in temp_set :
            answer = n 
            break 
        result[n] = temp_set
    
    return answer
    