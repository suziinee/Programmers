def solution(name) :

    n = len(name)
    ans = 0

    def toA(alphabet) :
        return min(ord(alphabet) - ord("A"), ord("Z") - ord(alphabet) + 1)

    # 첫번째 move는 온전히 왼-오로 가는 거리
    for i in range(n) :
        if name[i] != 'A' :
            move = i 
    
    for i in range(n) :
        if name[i] != 'A' :
            ans += toA(name[i])
            next_i = i + 1

            # A가 아닌 다음 요소가 나올때까지 next_i 초기화
            while next_i < n and name[next_i] == 'A' :
                next_i += 1
            
            # 매 순간 왼-오 경우와 오-꺾 경우를 생각해주기
            move = min(move, i * 2 + (n - next_i))
            
    ans += move
    return ans

        

