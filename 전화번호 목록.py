def solution(phone_book) :

    phone_book.sort()

    from collections import deque
    pb = deque(phone_book)

    hash = {p : 0 for p in phone_book}

    while pb :
        now = pb.popleft()
        for key in hash.keys() :
            if key.find(now) == 0 and key != now : 
                return False
    return True
    


    

