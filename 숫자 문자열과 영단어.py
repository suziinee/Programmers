def solution(s):
    dct = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9", "zero" : "0"} #key에 one, value에 "1"
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    answer = ''

    i = 0
    temp = s[i]
    while i < len(s)-1 : 
        if temp in num :
            answer += temp
            i += 1
            temp = s[i]
        elif temp in dct.keys() :
            answer += dct[temp]
            i += 1
            temp = s[i]
        else :
            i += 1
            temp += s[i]
    if temp in num :
        answer += temp
    elif temp in dct.keys() :
        answer += dct[temp]
        
		return int(answer)