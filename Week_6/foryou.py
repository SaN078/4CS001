import statistics
import math

def divbyseven(num):
    if (num % 7 == 0):
        return 'It is divisible by 7'
    else:
        return 'It is not divisible by 7'

input_number = int(input('Enter your number: '))
print(divbyseven(input_number))


def SI(p,t,r):
    simple_interest = (p*t*r)/100
    return simple_interest

principle = int(input('Enter principle: '))
rate = int(input('Enter rate: '))
time = int(input('Enter time: '))

result = SI(principle,time,rate)
print(f"The simple interest is {result}")

#Menu driven program!! Basic Arithmetic, factorial, mean median and mode

def welcome_message():
    print("Welcome to MY WORLD")

def basicArithmetic(num1,num2):
    user_selection = int(input("Press 1 for Addition 2 for subtraction 3 for multiplication and 4 for Division"))
    if user_selection == 1:
        return num1 + num2
    elif user_selection == 2:
        return num1-num2
    elif user_selection == 3:
        return num1 * num2
    elif user_selection==4:
        return num1/num2

def factorial(num):
    return math.factorial(num)

def mean_median_mode(numList):
    return statistics.mean(numList)
    return statistics.median(numList) statistics.mode(numList)


