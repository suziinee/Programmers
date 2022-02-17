def solution(record):
    
    res = [] # [id, sentence]
    d = {} # id : nickname
    
    for r in record :
        r = r.split()
        id = r[1]
        
        if len(r) == 3 :
            nickname = r[2]
            
        if r[0] == "Enter" :
            d[id] = nickname
            res.append([id, f"{id}님이 들어왔습니다."])
        elif r[0] == "Leave" :
            res.append([id, f"{id}님이 나갔습니다."])
        elif r[0] == "Change" :
            d[id] = nickname
    
    ans = [i[1].replace(i[0], d[i[0]]) for i in res]
    
    return ans