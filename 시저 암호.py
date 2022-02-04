def solution(s, n):
    answer = ''
    
    for word in s :
        if word.islower() :
            if chr(ord(word) + n).islower() :
                answer += chr(ord(word) + n)
            else :
                answer += chr(n - 1 - (ord('z') - ord(word)) + ord('a'))
        elif word.isupper() :
            if chr(ord(word) + n).isupper() :
                answer += chr(ord(word) + n)
            else : 
                answer += chr(n - 1 - (ord('Z') - ord(word)) + ord('A'))
        else :
            answer += ' '
                
    return answer