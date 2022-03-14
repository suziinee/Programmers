def solution(p):
    from collections import deque
    
    def proof(s) :
        s = deque(list(s))
        stack = [s.popleft()]
        while s :
            now = s.popleft()
            if stack :
                if now == ')' :
                    if stack[-1] == '(' :
                        stack.pop()
                        continue
            stack.append(now)

        if stack :
            return False
        else :
            return True
        
    u = []
    v = []
    ans = ''
    
    if not p :
        return ''
    else :
        p = deque(list(p))
        u.append(p.popleft())
        while p :
            if u.count('(') == u.count(')') :
                break
            u.append(p.popleft())
        v = p.copy()
    
    if proof(u) :
        u = ''.join(u)
        v = solution(v)
        return u + v
    else :
        ans += '('
        ans += solution(v)
        ans += ')'
        for i in range(len(u)) :
            if u[i] == '(' :
                u[i] = ')'
            else :
                u[i] = '('
        ans += ''.join(u[1:-1])
        return ans