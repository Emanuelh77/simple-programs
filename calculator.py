#Calculator
#performs simple arithmetic on values fed by the user

import math
import time

print('Starting calculator...')
time.sleep(1)

#calculator function
def calculator():
    first_number = int(input('please enter the first number: ').strip())
    first_choice = input('would you like to enter a second number? (y/n) ').strip()

    if(first_choice == 'y'):
        second_number = int(input('please enter the second number: ').strip())
        print('what kind of operation would you like to perform on these values? (type in a number) ')
        choice = int(input('[1]addition [2]subtraction [3]multiplication [4]division ').strip())

        if(choice) == 1:
            print(str(first_number) + '+' + str(second_number) + ' = ' + str(add(first_number,second_number)))
        elif choice == 2:
            print(str(first_number) + '-' + str(second_number) +
                  ' = ' + str(subtract(first_number, second_number)))
        elif choice == 3:
            print(str(first_number) + '*' + str(second_number) +
                  ' = ' + str(multiply(first_number, second_number)))
        elif choice == 4:
            print(str(first_number) + '/' + str(second_number) +
                  ' = ' + str(divide(first_number, second_number)))
    else:
        print("[1] to get the square root of " + str(first_number))
        print("[2] to get " + str(first_number) + " squared")
        option  = int(input("type 1 or 2 to continue ").strip())
        if(option == 1):
            print("square root of " + str(first_number) + " is " + str(sq_root(first_number)))
        elif(option == 2):
            print(str(first_number) + " squared is " + str(squared(first_number)))
    calculate_again()


def sq_root(number):
    sq_root_number = math.sqrt(number)
    return sq_root_number

def squared(number):
    return number**2

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def calculate_again():
    print('\n')
    option = input('would you like to keep using the calculator?(y/n) ').strip().lower()
    if option == 'y':
        calculator()
    else:
        pass

if __name__ == '__main__':
    calculator()

