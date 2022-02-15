def solution(numbers):
    from itertools import permutations
    nums = []
    int_nums = []
    primes = []
    
    for i in range(1, len(numbers) + 1) :
        perms = list(permutations(numbers, i))
        for perm in perms : 
            string = ''
            for num in perm :
                string += str(num)
            nums.append(string)
    
    int_nums = list(set([int(i) for i in nums]))
    
    def prime_bool(n) :
        for i in range(2, n) :
            if n % i == 0 :
                return False
        return True
    
    for i in int_nums :
        if i != 0 and i != 1 and prime_bool(i) == True :
            primes.append(i)
    
    return len(primes)