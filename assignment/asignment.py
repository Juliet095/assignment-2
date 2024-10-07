#no 1
# The volume of a sphere with radius r is (4/3)* pie * r**2.
# What is the volume of the sphere with radius 5.
# Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal placesradius = int(input("Enter the radius of a sphere: "))
pie=(22/7)
radius = int(input("enter the radius of the sphere: "))
volume = (4/3)*pie*radius**2
print(f"the volume of the sphere is {volume:.2f}")


#
#no 2
# Create a program to calculate the area of a triangle (1/2 * base * height).
# Base and height should be entered using the keyboard. 
def triangle_area():
    base = int(input("Enter the base of a triangle"))
    height = int(input("Enter the height of a triangle"))
    area =(1/2)* base *height
    print(f"The area of the base{base} and height {height} is {area}")
# call the function
triangle_area()
# no 3
# wITI has tasked you to automate a simple grading system. 
# As a python student, write a program using to display the grades that
# the student will be receiving based on the mark scored in a subject. 
# The grades are:
# 90% - 100% Grade is A
# 80% - 89%  Grade is B
# 70% - 79% Grade is C
# 60% - 69% Grade is D
# 50 - 59% Grade is E
# < 50% Fail
def calculate_Grades():
    print(" calculate student grades...")
    #student marks
    mark = int(input("Enter marks scored:\t"))
    # Testing student mark
    if mark>=90 and mark<=100:
        print("Grade is A")
    elif mark >=80 and mark<=89:
        print("Grade is B")
    elif mark>=70 and mark<=79:
        print("Grade is C")
    elif mark>=60 and mark<=69:
        print("Grade is D")
    elif mark>=50 and mark<=59:
        print("Grade is E")
    else:
        print("Fail")
# call the function
calculate_Grades()



# no 4
# WITI Acamedy is proposing a sacco to help students save their money. 
# Design a platform that will do the following.
# Welcome to, WITI Academy sacco. 
# 1. Deposit money
# 2. Withdraw money 
# 3. Check Balance 
# Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
# If the student selects 2, money should be withdrawn and a minimum withdrawal is 500. 
# If the student selects 3, the account balance should be displayed. 

def saccoTransactions():
    account_balance = 0
    run = 1
    while run == 1:
        print("\nwelcome to, WITI Academy.")
        #menu
        print("1, Depodit money")
        print("2, Withdraw money")
        print("3, account balance")
        student_choice = int(input("Enter your selection (1,2,or3): "))
        #performing the transaction of the student selection
        if student_choice == 1:
            print('\n...proessing a deposit transaction..')
            deposit_amount = int(input("Enter amount to be deposited"))
            # check if deposit amount is less than 1000
            if deposit_amount <1000:
                print('\nminimum deposit is 1000')
        if student_choice == 2:
            print('\n...proessing a withdraw transaction..')
            withdraw_amount = int(input("Enter amount to be withdrawn"))
        
            if account_balance == 0:
                print("your balance is 0")
            elif withdraw_amount < 500:
                print('minimum withdraw amount is 500')
            elif withdraw_amount>account_balance:
                print(f"withdraw failed,insufficiet funds")
            else:
                account_balance -= withdraw_amount
                print(f"Dear student, you have withdrawn {withdraw_amount}:,and your new account balance is {account_balance}")
        elif student_choice ==3:
            print(f"your account balance is {account_balance:,}")
        else:
            print("you enterd a wrong choice!! please select 1,2,3\n")
            run = int(input("Enter 1 to continue or any number to exit : "))
        if run!=1:
            print ("Thanks for using our sacco")
            break

saccoTransactions()                                       

                

