def solution(name) :

    n = len(name)
    ans = 0

    def toA(alphabet) :
        return min(ord(alphabet) - ord("A"), ord("Z") - ord(alphabet) + 1)

    forward = count[1:]
    backward = count[1:][::-1]

    if forward[-1] == 0 :
        f = sum(forward) + n - 1 - 1
    else :
        f = sum(forward) + n - 1

    if backward[-1] == 0 :
        b = sum(backward) + n - 1 - 1
    else :
        b = sum(backward) + n - 1
    
    return ans + min(f, b)
        

