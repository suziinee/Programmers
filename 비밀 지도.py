def solution(n, arr1, arr2):
    
    arr1 = [bin(i)[2:].zfill(n) for i in arr1]
    arr2 = [bin(i)[2:].zfill(n) for i in arr2]

    ans = []

    for a, b in zip(arr1, arr2) :
        res = ''
        for i in range(n) :
            res += str(int(a[i]) | int(b[i]))
        ans.append(res)

    ans = [i.replace('1', '#') for i in ans]
    ans = [i.replace('0', ' ') for i in ans]

    return ans  