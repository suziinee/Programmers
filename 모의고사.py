def solution(answers):
    s1 = [1,2,3,4,5]
    cnt1 = 0
    s2 = [2,1,2,3,2,4,2,5]
    cnt2 = 0
    s3 = [3,3,1,1,2,2,4,4,5,5]
    cnt3 = 0
    
    for i in range(len(answers)) :
        if answers[i] == s1[i%5] : 
            cnt1 += 1
        if answers[i] == s2[i%8] :
            cnt2 += 1
        if answers[i] == s3[i%10] :
            cnt3 += 1
    
    d = {1 : cnt1, 2 : cnt2, 3 : cnt3}
    ans = []
    max_val = max(d.values())
    for k, v in d.items() :
        if v == max_val :
            ans.append(k)
            
    return ans