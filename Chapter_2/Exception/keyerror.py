try:
    student={
        "name": "snehal",
        "age" :21
        }
    print(student)
except KeyError:
    print("Invalid Keys")
finally:
    print("Program executed...")