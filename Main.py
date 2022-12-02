import time
import Problem_1
import Problem_2
import Problem_3
import Problem_4
import Problem_5

def menu():
    """displays the menu to select a problem to solve"""
    print("0 - Exit the program")
    print("1 - Problem 1 Sum of Multiples")
    print("2 - Problem 2 Even Fibonacci numbers")
    print("3 - Problem 3 Largest Prime Factor")
    print("4 - Problem 4 Largest Palidrome Product")
    print("5 - Problem 5 Smallest Multiple")

def check_input_is_int(value):
    """Checks if the vlaue is an integer"""
    try:
        value is int
    except ValueError:
        raise ValueError
    finally:
        pass

def check_input_is_postive(value):
    """Checks if the value is a positive integer"""
    if value<0:
        print("Value entered must be positive")

def verify_input(value):
    """verifies the input is acceptable"""
    try:
        check_input_is_int(value)
        check_input_is_postive(value)
    except ValueError:
        print("Value entered must be positive integer")
        return False
    else:
        return True

def main():
    """Program to solve problems from Project Euler"""
    print("Welcome to solutions to Project Euler")
    menu()
    problem_set = int(input("Which problem set do you want the answer to?"))
    is_valid = verify_input(problem_set)
    if not is_valid:
        menu()
        problem_set = int(input("Which problem set do you want the answer to?"))
        is_valid = verify_input(problem_set)
    while problem_set != 0 and is_valid is True:
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
        elif problem_set == 5:
            
            low_num = int(input("What is the low number you want to limit the calculation to?"))
            high_num = int(input("What is the high number you want to limit the calculation to?"))
            start_time = time.perf_counter()
            print(Problem_5.prob5(low_num, high_num))
            end_time = time.perf_counter()
            print(f"This took {end_time - start_time:0.4f} seconds")
        else:
            print("Sorry that problem is not answered yet!")
        menu()
        problem_set = int(input("Which problem set do you want the answer to?"))
        is_valid = verify_input(problem_set)

    print("Thank you for using the program")

main()
