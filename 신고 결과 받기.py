def solution(id_list, report, k):

    d = {} # 신고당한애 : [신고한애들]
    for id in id_list :
        d[id] = []

    for r in report :
        ids = r.split()
        d[ids[1]].append(ids[0])

    answer = {}
    for id in id_list :
        answer[id] = 0

    for key, value in d.items() :
        if len(set(value)) >= k :
            for id in list(set(value)) :
                answer[id] += 1

    return list(answer.values())