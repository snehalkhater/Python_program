class AgeInvalidException(Exception):
    pass
def checkage(age):
    if age < 18 :
        raise AgeInvalidException("Age is Not Valid")
    return age
try :
    checkage(15)
except AgeInvalidException as a:
     print("Error", a)
finally :
     print("code Executed")