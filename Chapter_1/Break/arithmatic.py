while True:
    print("1.Addition")
    print("2.Substration")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    ch=int(input("Enter your choice : "))
    if ch == 5:
        break
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    if ch==1:
        print("Addition is :" ,a+b)
    elif ch==1:
            print("Addition is :" ,a+b)
    elif ch==2:
            print("substration is :" ,a-b)
    elif ch==1:
            print("multiplication is :" ,a*b)
    elif ch==1:
            if b!=0:
             print("division is :" ,a/b)
            else :
             print("Can not divide by zero")
    else:
         print("Enter valid choice")
    
