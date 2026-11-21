try:
    n=int(input("Enter no:"))
    print(n)
except ValueError:
    print("Invalid Input")
finally:
    print("program executed...")
