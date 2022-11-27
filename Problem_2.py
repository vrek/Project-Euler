def prob2(max_value):
    from functools import lru_cache
    
    fib_total = 0
    fib_value = 0
    n = 1
    
    @lru_cache(maxsize = 1000)
    def fibonacci(n):
        if type(n) != int:
            raise TypeError("n must be a positive int")
        if n < 1:
            raise ValueError("n must be a positive int")
    
        if n==1 or n==2:
            return 1
        elif n>2:
            return fibonacci(n-1)+fibonacci(n-2)
    
    
    while True:
        nextTerm = fibonacci(n)
        if nextTerm > max_value:
            break
        if nextTerm % 2 == 0:
            fib_total += nextTerm
        n += 1
    
    print(fib_total)


