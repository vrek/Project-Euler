import time
import Problem_1
import Problem_2
import Problem_3
import Problem_4

def menu():
    print("0 - Exit the program")
    print("1 - Problem 1 Sum of Multiples")
    print("2 - Problem 2 Even Fibonacci numbers")
    print("3 - Problem 3 Largest Prime Factor")
    print("4 - Problem 4 Largest Palidrome Product")

def check_input_is_int(value):
    try:
        value=int(value)
    except ValueError:
        print("Value must be an integer")
    finally:
        pass

def check_input_is_postive(value):
    if value<0:
        print("Value entered must be positive")


def verify_input(value):
    try:
        check_input_is_int(value)
        check_input_is_postive(value)
    except ValueError:
        print("Value entered must be positive integer")
    finally:
        pass

def Main():
    print("Welcome to solutions to Project Euler")
    menu()
    problem_set = input("Which problem set do you want the answer to?")
    verify_input(problem_set)
    problem_set=int(problem_set)
    while problem_set != 0:
        
        if problem_set == 1:
            prob1_max = int(input("What is the highest natual number to include?"))
            prob1_multi1 = int(input("What is the first value for the multiples?"))
            prob1_multi2 = int(input("What is the second value for the multiples?"))
            start_time = time.perf_counter()
            print(Problem_1.prob1(prob1_max, prob1_multi1, prob1_multi2))
            end_time = time.perf_counter()
            print(f"This took {end_time - start_time:0.4f} seconds")
        elif problem_set == 2:
            start_time = time.perf_counter()
            print(Problem_2.prob2(int(input("What is this highest value for fibonacci you want?"))))
            end_time = time.perf_counter()
            print(f"This took {end_time - start_time:0.4f} seconds")
        elif problem_set == 3:
            start_time = time.perf_counter()
            print(Problem_3.prob3(int(input("What is the number you want the largest prime factor for?"))))
            end_time = time.perf_counter()
            print(f"This took {end_time - start_time:0.4f} seconds")
        elif problem_set == 4:
            start_time = time.perf_counter()
            print(Problem_4.prob4(int(input("How many decimal places should the starting numbers be?"))))
            end_time = time.perf_counter()
            print(f"This took {end_time - start_time:0.4f} seconds")
        else:
            print("Sorry that problem is not answered yet!")
        menu()
        problem_set = int(input("Which problem set do you want the answer to?"))

    print("Thank you for using the program")

Main()
