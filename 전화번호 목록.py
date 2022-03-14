def solution(phone_book) :

    phone_book.sort()

    from collections import deque
    pb = deque(phone_book)

    while pb :
        now = pb.popleft()
        for p in pb :
            if p.find(now) == 0 : 
                return False
    return True
    


    

