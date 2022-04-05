* dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

def solution(triangle):

    n = len(triangle)
    dp = []
    for i in range(n) :
        dp.append([])
        for j in range(i + 1) :
            dp[i].append(0)

    for i in range(n) :
        for j in range(i + 1) :
            if i == 0 :
                dp[i][j] = triangle[i][j]
            else :
                if j == 0 : left = 0
                else : left = dp[i-1][j-1]
                    
                if j == i : right = 0
                else : right = dp[i-1][j] 

                dp[i][j] = max(left, right) + triangle[i][j]

    return max(dp[-1])