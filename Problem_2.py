"""finds  the sum of all even fibonacci numbers below max_value"""
def prob2(max_value):
    from functools import lru_cache
    fib_total = 0
    num = 1
    @lru_cache(maxsize = 1000)
    def fibonacci(num):
        if not isinstance(num, int):
            raise TypeError("n must be a positive int")
        if num < 1:
            raise ValueError("n must be a positive int")
        if num==1 or num==2:
            return 1
        elif num>2:
            return fibonacci(num-1)+fibonacci(num-2)
    while True:
        nextTerm = fibonacci(num)
        if nextTerm > max_value:
            break
        if nextTerm % 2 == 0:
            fib_total += nextTerm
        num += 1
    return fib_total


