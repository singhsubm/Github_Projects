print("hello world")
#wap for calculator
import math
print('Program for Calculator')
y,z='yes','no'
use=input("Do you want to calculate any number:-")
if use=='yes':
    a=eval(input("enter your 1st number:-"))
    b=eval(input("enter your 2nd number:-"))
    user=input("enter your choice '+'24.2,'-','*','/'")
    if user=='+':
        print("1st number:-",a,"2nd number:-",b)
        print(a+b)
        c=input("do you want again calculate any numbers:-")
        if c==use:
            print("here we go again")
        else:
            print("Thankyou :)")
    elif user=='-':
        print("1st number:-",a,"2nd number:-",b)
        print(a-b)
        c=input("do you want again calculate any numbers:-")
        if c==use:
            print("here we go again")
        else:
            print("Thankyou :)")
    elif user=='*':
        print("1st number:-",a,"2nd number:-",b)
        print(a*b)
        c=input("do you want again calculate any numbers:-")
        if c==use:
            print("here we go again")
        else:
            print("Thankyou :)")
    elif user=='/':
        print("1st number:-",a,"2nd number:-",b)
        print(a/b)
        c=input("do you want again calculate any numbers:-")
        if c==use:
            print("here we go again")
        else:
            print("Thankyou :)")
    else:
        print("1st number:-",a,"2nd number:-",b)
        print("enter valid operator")
        c=input("do you want again calculate any numbers:-")
        if c==use:
            print("here we go again")
        else:
            print("Thankyou :)")
elif use=='no':
    print('Thank you :)')
else:
    print("enter valid input")