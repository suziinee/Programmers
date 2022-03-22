def solution(n, computers) :

    graph = [[] for i in range(n)]
    visited = [False] * n

    for i in range(n) :
        for j in range(n) :
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)
    
    def dfs(x) :
        if visited[x] == True :
            return False
        if visited[x] == False :
            visited[x] = True
            for i in graph[x] :
                dfs(i)
            return True

    res = 0
    for i in range(n) :
        if dfs(i) == True :
            res += 1
        
    return res