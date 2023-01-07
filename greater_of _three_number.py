print("greater of three number")
u1=int(input("enter 1st number"))
u2=int(input("enter 2nd number"))
u3=int(input("enter 3rd number"))
if u1>u2:
    if u1>u3:
        print(u1,"is greater")
    else:
        print(u3,"is greater")
elif u2>u1:
    if u2>u3:
        print(u2,"is greatest")
    else:
        print(u3,"is greatest")
else:
    print(u3,"is greatest")