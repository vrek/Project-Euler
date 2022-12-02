"""Calculates the smallest possible integer that can be devided by all numbers between low_num and high_num evenly"""
def prob5(low_num, high_num):
    for num in range(low_num,high_num):
        if all(num % n ==0 for n in range(low):
               return num
        else:
            return None