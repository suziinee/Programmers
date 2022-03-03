def solution(rows, columns, queries) :

    arr = [[]]
    for i in range(1, rows + 1) :
        arr.append([])
        arr[i].append([])
        for j in range(1, columns + 1) :
            arr[i].append((i-1) * columns + j)

    def border(x1, y1, x2, y2) : #border 좌표를 구해주고 회전해줌
        b_dict = {}
        for i in range(y1, y2 + 1) :
            b_dict[(x1, i)] = 0
        for i in range(x1, x2 + 1) :
            b_dict[(i, y1)] = 0
        for i in range(x1, x2 + 1) :
            b_dict[(i, y2)] = 0
        for i in range(y1, y2 + 1) :
            b_dict[(x2, i)] = 0
        
        for i in range(y1, y2) :
            b_dict[(x1, i)] = (x1, i + 1)
        for i in range(x1, x2) :
            b_dict[(i, y2)] = (i + 1, y2)
        for i in range(y1 + 1, y2 + 1) :
            b_dict[(x2, i)] = (x2, i - 1)
        for i in range(x1 + 1, x2 + 1) :
            b_dict[(i, y1)] = (i - 1, y1)
        return b_dict

    ans = []
    for q in queries :
        b_dict = border(q[0], q[1], q[2], q[3])
        import copy
        copy = copy.deepcopy(arr)
        nums = []
        for k, v in b_dict.items() :
            nums.append(arr[v[0]][v[1]])
            arr[v[0]][v[1]] = copy[k[0]][k[1]]
        ans.append(min(nums))

    return ans        

