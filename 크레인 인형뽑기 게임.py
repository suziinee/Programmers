def solution(board, moves):
    n = len(board)
    
    # 각 칸에 있는 것들 모아담기 : new
    new = []
    for i in range(n) :
        new.append([])
    board = board[::-1]
    for i in range(n) :
        for j in range(n) :
            new[j].append(board[i][j])

    # new에서 빈칸(0) 빼기
    new = [[x for x in y if x != 0] for y in new]

    # move를 하나씩 줄이기
    moves = [x-1 for x in moves]
    print(moves)
  
    # stack 쌓고 중복된거 없애기
    stack = []
    cnt = 0
    for move in moves :
        if new[move] : 
            stack.append(new[move][-1])
            new[move].pop()
            if len(stack) == 1 :
                continue
            elif stack[-2] == stack[-1] :
                stack.pop()
                stack.pop()
                cnt += 2

    return cnt