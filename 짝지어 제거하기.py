def solution(s):

    s = list(s)
    stack = [s[0]]
    s.pop(0)

    for word in s :
        if stack : 
            if stack[-1] == word :
                stack.pop(-1)
            else :
                stack.append(word)
        else :
            stack.append(word)

    return not(stack)