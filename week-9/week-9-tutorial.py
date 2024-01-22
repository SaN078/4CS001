try:
    result = []
    with open(r'C:\Users\Sangeet Raut\Desktop\4CS001\week-9\test.txt','r') as usr_input:
        data = usr_input.read()
        print(data)
        
    

except (FileNotFoundError, ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")



def divide_numbers(num1,num2):
    try:
        result = num1/num2

    except ZeroDivisionError:
        print('Error: cannot ')