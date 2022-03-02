def solution(expression) :

    # 쪼개기
    ex = []
    nums = []
    res = ''
    for e in expression :
        if e.isdigit() :
            res += e
        else :
            nums.append(int(res))
            ex.append(e)
            res = ''
    nums.append(int(res))


    combs = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 1, 0], [2, 0, 1]]
    symbol = ['*', '-', '+']
    ans = []

    from collections import deque
    for c in combs :
        res = 0
        copy_nums = deque(nums.copy())
        copy_ex = ex.copy()
        stack_nums = [copy_nums.popleft()]
        stack_ex = []

        for e in copy_ex[:] : 
            stack_nums.append(copy_nums.popleft())
            if e == symbol[c[0]] :
                res = eval(str(stack_nums.pop(-2)) + e + str(stack_nums.pop(-1)))
                stack_nums.append(res)
                copy_ex.remove(e)
            else : 
                stack_ex.append(copy_ex.pop(0))
        
        copy_nums = deque(stack_nums)
        copy_ex = stack_ex
        stack_nums = [copy_nums.popleft()]
        stack_ex = []
        for e in copy_ex[:] : 
            stack_nums.append(copy_nums.popleft())
            if e == symbol[c[1]] :
                res = eval(str(stack_nums.pop(-2)) + e + str(stack_nums.pop(-1)))
                stack_nums.append(res)
                copy_ex.remove(e)
            else :
                stack_ex.append(copy_ex.pop(0))
        
        copy_nums = deque(stack_nums)
        copy_ex = stack_ex
        stack_nums = [copy_nums.popleft()]
        stack_ex = []
        for e in copy_ex[:] :
            stack_nums.append(copy_nums.popleft())
            if e == symbol[c[2]] :
                res = eval(str(stack_nums.pop(-2)) + e + str(stack_nums.pop(-1)))
                stack_nums.append(res)
                copy_ex.remove(e)
            else :
                stack_ex.append(copy_ex.pop(0))

        ans.append(abs(stack_nums[0]))

    return max(ans)


