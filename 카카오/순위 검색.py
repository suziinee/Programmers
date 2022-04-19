def solution(info, query) :

    from collections import defaultdict
    from itertools import product
    from bisect import bisect_left

    info_dict = defaultdict(list)
    ans = []
    binarys = list(product(True, False), repeat = 4)

    for i in info :
        i = i.split()
        score = int(i.pop())
        for b in binarys :
            key = ""
            for k in range(4) :
                if b[k] :
                    key += i[k]
                    key += "/"
                else :
                    key += "-"
                    key += "/"
            info_dict[key[:-1]].append(score)

    # 점수 정렬
    info_dict = {key : sorted(value) for key, value in info_dict.items()}

    query = [x.split() for x in query]
    for q in query :
        score = int(q.pop())
        key = "".join(q).replace("and", "/")
        x = bisect_left(info_dict[key], score)
        ans.append(len(info_dict[key] - x))
    
    return ans
