def solution(lines):
    import datetime
    diff = datetime.timedelta(seconds = 0.001)
    diff2 = datetime.timedelta(seconds = 0.999)
    start = []
    end = []

    for line in lines :
        a, b, c = line.split()
        time = datetime.datetime.strptime(a + " " + b, "%Y-%m-%d %H:%M:%S.%f")
        c = datetime.timedelta(seconds = float(c[:-1]))
        start.append(time - c + diff)
        end.append(time)

    min_start = min(start)
    max_end = max(end)

    count = {}
    while min_start <= max_end :
        count[min_start] = 0
        min_start += diff

    n = len(start)
    for k in count.keys() :
      for i in range(n) :
        if start[i] <= k <= end[i] :
            count[k] += 1
            continue
        if start[i] <= k + diff2 <= end[i] :
            count[k] += 1
            continue

    return max(count.values())

        



            