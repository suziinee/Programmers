def solution(priorities, location):

    from collections import deque
    p = deque(priorities)

    for i in range(len(priorities)) :
        priorities[i] = [priorities[i], i] # [value, index]

    res = []
    while len(p) >= 2 :
        first = p.popleft()
        pr_first = priorities.pop(0)
        if max(p) > first :
            p.append(first)
            priorities.append(pr_first)
        else :
            res.append(pr_first)
    res.append(priorities[0])

    for comb in res :
        if comb[1] == location :
            return res.index(comb) + 1
