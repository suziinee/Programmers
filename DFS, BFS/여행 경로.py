def solution(tickets):
    
    hash = {t[0] : [] for t in tickets}
    for t in tickets :
        hash[t[0]].append(t[1])
    for value in hash.values() :
        value.sort(reverse = True)
    
    stack = ['ICN']
    path = []
    while stack :
        top = stack[-1]
        if top not in hash :
            path.append(stack.pop())
        elif len(hash[top]) == 0 :
            path.append(stack.pop())
        else :
            stack.append(hash[top].pop())
    
    return path[::-1]








    s = set()
    for t in tickets :
        s |= set(t)
    n = len(s)
    s = list(sorted(s)) 
    
    graph = [[] for i in range(n)]
    
    for t in tickets :
        graph[s.index(t[0])].append(t[1])
        graph[s.index(t[1])].append(t[0])
    
    graph = [sorted(list(set(g))) for g in graph]

    visited = [False] * len(tickets)
    
    res = []
    
    def dfs(graph, v, tickets, visited) :
        res.append(v)
        for after in graph[v] :
            if [v, after] in tickets :
                if visited[tickets.index([v, after])] == False :
                    dfs(graph, after, tickets, visited)


    
    
    from collections import deque
    def bfs(graph, start, tickets) :
        q = deque([start])
        while tickets :
            now = q.popleft()
            res.append(now)
            for after in graph[s.index(now)] :
                if [now, after] in tickets :
                    if (len(tickets) == 1) or (after in [t[0] for t in tickets]) :
                        q.append(after)
                        tickets.remove([now, after])
                        break
                    else :
                        continue
                    
        res.append(q.popleft())
   
                        
    bfs(graph, 'ICN', tickets)
    return res