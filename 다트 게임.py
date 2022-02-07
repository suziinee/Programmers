def solution(dartResult):
    l = []
    bonus = ['S', 'D', 'T']
    option = ['*', '#']
    
    # option과 분리해서 넣기
    temp = ''
    for i in range(len(dartResult)) :
        if dartResult[i] in option :
            l.append(dartResult[i])
        elif dartResult[i] in bonus :
            temp += dartResult[i]
            l.append(temp)
            temp = ''
        else :
            temp += dartResult[i]
    
    # score로 변경해주는 함수
    def score(string) :
        bonus = string[-1]
        num = int(string[:-1])
        if bonus == 'S' :
            return num**1
        elif bonus == 'D' :
            return num**2
        elif bonus == 'T' :
            return num**3
    
    # score 변경
    for i in range(len(l)) :
        if l[i] not in option :
            l[i] = score(l[i])
    
    # option 계산
    for i in range(1, len(l)) :
        if l[i] == '#' :
            l[i-1] = -l[i-1]
            continue
        elif l[i] == '*' and i == 1 :
            l[i-1] = 2 * l[i-1]
            continue
        elif l[i] == '*' and i >= 2 :
            l[i-1] = 2 * l[i-1]
            if l[i-2] not in option :
                l[i-2] = 2 * l[i-2]
            else :
                l[i-3] = 2 * l[i-3]
    
    ans = 0
    for i in l :
        if i not in option :
            ans += i
    return ans