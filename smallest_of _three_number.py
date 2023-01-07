print("smallest of three number")
u1=int(input("enter 1st number"))
u2=int(input("enter 2nd number"))
u3=int(input("enter 3rd number"))
if u1<u2:
    if u1<u3:
        print(u1,"is samllest")
    else:
        print(u3,"is smallest")
elif u2<u1:
    if u2<u3:
        print(u2,"is smallest")
    else:
        print(u3,"is samllest")
else:
    print(u3,"is smallest")