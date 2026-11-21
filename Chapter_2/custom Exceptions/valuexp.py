def checkage(age):
    if age < 0 :
         raise ValueError("Age can not be negative")
    else:
         print("Age is positive")
    return age
try :
     checkage(5)
except ValueError as e:
     print("Error", e)
finally :
     print("code Executed")