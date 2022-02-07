def solution(s):

    idx = 0
    answer = ''

    for word in s :
        if word == ' ' :
            answer += ' '
            idx = 0
        elif idx%2 == 0 :
            answer += word.upper()
            idx += 1
        elif idx%2 == 1 :
            answer += word.lower()
            idx += 1

    return answer