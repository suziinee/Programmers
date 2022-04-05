def solution(answers):
    s1 = [1, 2, 3, 4, 5] * 2000
    s2 = [2,1,2,3,2,4,2,5] * 1250
    s3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    ans = {1 : 0, 2 : 0, 3 : 0}
    
    for i in range(len(answers)) :
        if answers[i] == s1[i%5] : 
            ans[1] += 1
        if answers[i] == s2[i%8] :
            ans[2] += 1
        if answers[i] == s3[i%10] :
            ans[3] += 1
    
    res = []
    max_val = max(ans.values())
    for i in range(1, 4) :
        if ans[i] == max_val :
            res.append(i)
            
    return res