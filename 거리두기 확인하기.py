def solution(places) :

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    ddx = [-2, 0, 2, 0]
    ddy = [0, 2, 0, -2]
    
    from itertools import product
    xy = list(product([0, 1, 2, 3, 4], repeat = 2))

    ans = []

    def P(x, y, p) :
        for k in range(8) :
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx > 4 or ny > 4 :
                continue
            if p[nx][ny] == "P" :
                if p[nx][y] == "X" and p[x][ny] == "X" :
                    continue
                else :
                    return False
            
        for k in range(4) :
            nx = x + ddx[k]
            ny = y + ddy[k]
            if nx < 0 or ny < 0 or nx > 4 or ny > 4 :
                continue
            if p[nx][ny] == "P" :
                if p[(x + nx)//2][(y + ny)//2] == "X" :
                    continue
                else :
                    return False
        return True

    for p in places :
        for set in xy :
            x = set[0]
            y = set[1]
            if p[x][y] == "P" :
                if not P(x, y, p) :
                    ans.append(0)
                    break
        else :
            ans.append(1)
    
    return ans



    
