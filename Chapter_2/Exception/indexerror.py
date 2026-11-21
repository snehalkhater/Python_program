try:
    n=[10,20,30]
    print(n[5])
except IndexError:
    print("Invalid Index")
finally:
    print("Program Executed...")