def solution(lottos, win_nums):
    ans = []
    zero_count = len([x for x in lottos if x == 0])

    # 최고 순위 만들기
    lottos_new = [x for x in lottos if x != 0]
    dup = [x for x in lottos_new if x in win_nums]
    max_score = len(dup) + zero_count

    # 최저 순위 만들기
    min_score = len(dup)

    d = {6:1, 5:2, 4:3, 3:4, 2:5} # score : 등수
    if max_score != 1 and max_score != 0 :
        ans.append(d[max_score])
    else :
        ans.append(6)
    if min_score != 1 and min_score != 0 :
        ans.append(d[min_score])
    else :
        ans.append(6)

    return ans