import time
import Problem_1
import Problem_2
import Problem_3

def menu():
    print("0 - Exit the program")
    print("1 - Problem 1 Multiples of 3 or 5")
    print("2 - Problem 2 Even Fibonacci numbers")
    print("3 - Problem 3 Largest Prime Factor")

def Main():
    print("Welcome to solutions to Project Euler")
    menu()
    problem_set = int(input("Which problem set do you want the answer to?"))
    while problem_set != 0:
        if problem_set < 1:
            raise ValueError("Your selection must be a positive integer")
        if type(problem_set) != int:
            raise TypeError("Your selection must be a positive integer")
        if problem_set == 1:
            start_time = time.perf_counter()
            Problem_1.prob1()
            end_time = time.perf_counter()
            print(f"This took {end_time - start_time:0.4f} seconds")
        elif problem_set == 2:
            start_time = time.perf_counter()
            Problem_2.prob2(int(input("What is this highest value for fibonacci you want?")))
            end_time = time.perf_counter()
            print(f"This took {end_time - start_time:0.4f} seconds")
        elif problem_set == 3:
            start_time = time.perf_counter()
            Problem_3.prob3(int(input("What is this number do you want the largest prime factor for?")))
            end_time = time.perf_counter()
            print(f"This took {end_time - start_time:0.4f} seconds")
        else:
            print("Sorry that problem is not answered yet!")
        menu()
        problem_set = int(input("Which problem set do you want the answer to?"))

    print("Thank you for using the program")

Main()
