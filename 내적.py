def solution(a, b):
    n = len(a)
    return sum([a[i] * b[i] for i in range(n)])