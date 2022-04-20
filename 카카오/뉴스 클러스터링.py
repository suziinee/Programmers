def solution(str1, str2) :

    str1 = str1.upper()
    str2 = str2.upper()

    str1_lst = []
    str2_lst = []

    for i in range(len(str1) - 1) :
        if str1[i:i+2].isalpha() :
            str1_lst.append(str1[i:i+2])
    for i in range(len(str2) - 1) :
        if str2[i:i+2].isalpha() :
            str2_lst.append(str2[i:i+2])
  
    # 교집합
    copy1 = str1_lst.copy()
    copy2 = str2_lst.copy()
    a = []
    for i in copy1 :
        if i in copy2 :
            a.append(i)
            copy2.remove(i)
    
    # 합집합
    str1_lst.extend(str2_lst)
    b = str1_lst.copy()
    for i in a :
        b.remove(i)

    if len(a) == 0 and len(b) == 0 :
      return 65536
    else :
      return int(len(a) / len(b) * 65536)