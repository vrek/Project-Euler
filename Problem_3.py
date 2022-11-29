def prob3(value):
    divisor = 2
    while divisor ** 2 < value:
        while value % divisor == 0:
            value = value / divisor
        divisor = divisor + 1
    return value