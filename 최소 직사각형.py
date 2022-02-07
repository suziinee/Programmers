def solution(sizes):

    # size 재배치
    new_sizes = []
    for size in sizes :
        new_sizes.append([min(size), max(size)])

    temp1 = []
    temp2 = []
    for size in new_sizes :
        temp1.append(size[0])
        temp2.append(size[1])
    return max(temp1) * max(temp2)