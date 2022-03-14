def solution(phone_book) :

    hash = {p : 1 for p in phone_book}

    for num in phone_book :
        temp = ""
        for n in num :
            temp += n
            if temp in hash and temp != num :
                return False
    return True
    
    

    

    


    

