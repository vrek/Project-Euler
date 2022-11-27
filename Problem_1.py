def prob1():

    total = 0
    
    for number in range(1,1000):
        if number%5 == 0 or number%3 == 0:
            total = total + number
    print(total)