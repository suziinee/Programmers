def solution(m, n, puddles) :

    # dp[i][j] : (0, 0)부터 (i, j)까지의 최단거리 경로 수
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]

    dp = [[0] * m for _ in range(n)]
    puddles = [[p[0] - 1, p[1] - 1] for p in puddles]

    for i in range(n) :
        for j in range(m) :
            if [j, i] in puddles :
                dp[i][j] = 0
                continue
                
            if i == 0 and j == 0 :
                dp[i][j] = 1
                continue

            if i == 0 : up = 0
            else : up = dp[i-1][j]
            if j == 0 : left = 0
            else : left = dp[i][j-1]
            dp[i][j] = left + up
            
    return dp[n-1][m-1] % 1000000007
        



