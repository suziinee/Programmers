def solution(citations):
    
    citations.sort()
    ans = []
    from bisect import bisect_left
    
    if citations[0] >= len(citations) :
        return len(citations)
    
    for h in range(citations[0], citations[-1] + 1) :
        index = bisect_left(citations, h)
        if (index <= h) and ((len(citations) - index) >= h) :
            ans.append(h)
    
    return max(ans)