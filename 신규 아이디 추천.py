def solution(new_id):
    answer = ''
    
    # 1단계
    new_id = new_id.lower()
    new_id = list(new_id)
    
    # 2단계
    for n in new_id[:] :
        if 'a' <= n <= 'z' or n.isdigit() or n == '-' or n =='_' or n == '.' :
            pass
        else :
            new_id.remove(n)
    
    # 3단계 - 리스트 연속 중복 제거
    new = []
    for i in range(len(new_id)) :
        if i == 0 :
            new.append(new_id[i])
        elif new_id[i] == '.' and new[-1] == '.' :
            pass
        else :
            new.append(new_id[i])
    
    
    # 4단계 + 5단계
    if new :
        if new[0] == '.' :
            new.pop(0)
    else :
        new.append("a")
    if new :
        if new[-1] == '.' :
            new.pop(-1)
    else :
        new.append("a")
    
    # 6단계
    if len(new) >= 16 :
        new = new[:15]
        if new[-1] == '.' :
            new.pop()
    
    # 7단계
    if len(new) <= 2 :
        while len(new) < 3 :
            new.append(new[-1])
    
    return ''.join(new)