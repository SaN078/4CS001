a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))

difference = a-b
differnce2= b-a
if (a<b):
    print(differnce2)
else:
    print(difference)
######################################################################################

percentage=float(input("Enter the percentage to know the grading:"))
if(70<=percentage):
     print(f"{percentage} percentage falls under grading A(GPA 4).")
elif(60<=percentage<=69.99):
    print(f"{percentage} percentage falls under grading B(GPA 3).")
elif(50<=percentage<=59.99):
    print(f"{percentage} percentage falls under grading C(GPA 2).")
elif(43<=percentage<=49.99):
    print(f"{percentage} percentage falls under grading D(GPA 1).")
elif(40<=percentage<=42.99):
    print(f"{percentage} percentage falls under grading E(GPA 0).")
elif(35<=percentage<=39):
    print(f"{percentage} percentage falls under grading CP(Compensated Pass).")
elif(0<=percentage<=34):
    print(f"{percentage} percentage falls under grading F (Fail).")
else:
    print("Please enter the valid percentage")


###############################################################################

number=float(input("Enter a number:"))
if (number%2==0) and (number%3==0):
    print(f"{number} is divisible by 2 and 3.")
else:
    print(f"{number} is not divisible by 2 and 3.")

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if (num1>0) and (num2>0):
     print(num1*num2)
else:
    print("The number must be positive.")




############################################################

workingDays=int(input("Enter the total days of working:"))
absentDays=int(input("Enter the total absent days:"))
percentage=((workingDays-absentDays)/workingDays)*100
if (percentage<80):
    print("You are not eligible to sit in this exam.")
else:
    print("You are eligible to sit in this exam.")

################################################################################

'''Develop a game where there is a zombie who is working straight in the road. while moving ahead, there is a pothole where zombie might fall and die. In right hand side there is a jungle where zombie will get lost and die out of hunger or gets shot by hunter. The only way to win the game is to make zombie move left where zombie will find human '''

password = "password"
print("Welcome to the Zombie Game")
print("-"*100)
user_name = input("Enter your name")
print(f"Hey there, {user_name} Please verify with a password")
user_pw = input("Enter the password")
if user_pw == password:
    print("Welcome to the game \n Let me explain the scenario")
    print('''1. If you walk straight than you fall into the pit and DIE!! \n 2. If you go to the right, you get lost in the jungle and die because hunter shot you!! \n 3. If you go left than you survive and get a human brain treat:) ''')
    print("In this zombies world, you have to survive as long as possible.")

else:
    print('You need to pay $999999999')
    exit()
