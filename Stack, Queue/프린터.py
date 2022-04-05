def solution(priorities, location):

    priorities = [(i, v) for i, v in enumerate(priorities)]

    res = []
    while len(priorities) >= 2 :
        pr_first = priorities.pop(0)
        if any(pr_first[1] < p[1] for p in priorities) :
            priorities.append(pr_first)
        else :
            res.append(pr_first)
    res.append(priorities[0])

    for comb in res :
        if comb[0] == location :
            return res.index(comb) + 1
