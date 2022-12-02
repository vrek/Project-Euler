"""Finds the sum of all multiples of multi1 and multi2 below max_num"""
def prob1(max_num, multi1, multi2):

    total = 0
    
    for number in range(1,max_num):
        if number%multi1 == 0 or number%multi2 == 0:
            total = total + number
    return total