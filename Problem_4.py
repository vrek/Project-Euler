def is_palindrome(value):
    return str(value) == str(value)[::-1]

def prob4(decimals):
    next_guess = 0
    current_guess = 0
    for i in range(((10**decimals)-1), (10**(decimals-1)-1), -1):
        for j in range(i, (10**(decimals-1))-1, -1):
            next_guess = i * j
            if(next_guess > current_guess):
                if(is_palindrome(next_guess)):
                    current_guess = next_guess
                    break
                else:
                    j -= 1
    return current_guess