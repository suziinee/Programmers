def solution(people, limit) :

    from collections import deque
    people.sort(reverse = True)
    people = deque(people)
    ans = 0
    
    while len(people) >= 2 :
        bottom = people.pop()
        top = people.popleft()
        if bottom + top > limit :
            ans += 1
            people.append(bottom)
            continue
        else :
            ans += 1
    
    if people :
        ans += 1
        
    return ans
            
        
    
