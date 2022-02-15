def solution(numbers):
    from itertools import permutations
    a = set()
    primes = []

    for i in range(len(numbers)) :
        a |= set(map(int, map("".join, permutations(list(numbers), i + 1))))
    
    def prime_bool(n) :
        for i in range(2, n) :
            if n % i == 0 :
                return False
        return True
    
    a -= set(range(0, 2))
    a = list(a)
    for i in a :
        if prime_bool(i) == True :
            primes.append(i)
    
    return len(primes)