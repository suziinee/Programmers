def solution(n, arr1, arr2):
    
    def bin_change(s, n) :
        l = list(s)
        l.remove('b')
        l = l[1:]
        while len(l) < n :
            l.insert(0, '0')
        return ''.join(l)
    
    new = []
    for i in range(n) :
        new.append(bin_change(bin(arr1[i] | arr2[i]), n))
    
    ans = []
    for i in new :
        i = i.replace('1', '#')
        i = i.replace('0', ' ')
        ans.append(i)
    return ans