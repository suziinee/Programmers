def solution(tickets):
    
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
    
    res = []
    
    from collections import deque
    def bfs(graph, start, tickets) :
        q = deque([start])
        while tickets :
            now = q.popleft()
            res.append(now)
            for after in graph[s.index(now)] :
                if [now, after] in tickets :
                    q.append(after)
                    tickets.remove([now, after])
                    break
                    
        res.append(q.popleft())
   
                        
    bfs(graph, 'ICN', tickets)
    return res