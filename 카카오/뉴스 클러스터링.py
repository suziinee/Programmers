def solution(str1, str2) :

    str1 = str1.upper()
    str2 = str2.upper()

    str1_lst = [str1[i:i+2] for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    str2_lst = [str2[i:i+2] for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]
  
    # 합집합, 교집합 만들기
    all_ = set(str1_lst) | set(str2_lst)
    a = []
    b = []
    if all_ :
        for i in all_ :
            a.extend([i] * min(str1_lst.count(i), str2_lst.count(i)))
            b.extend([i] * max(str1_lst.count(i), str2_lst.count(i)))
        ans = int(len(a) / len(b) * 65536)
        return ans
    else :
        return 65536

    