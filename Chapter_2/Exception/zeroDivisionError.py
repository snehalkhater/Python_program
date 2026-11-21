try:
    a=10
    b=0
    c=a/b
except ZeroDivisionError:
    print("you cannot divide by zero")
else:
    print(c)
finally :
    print("Program Executed...")