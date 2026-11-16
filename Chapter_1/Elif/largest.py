a = int(input("Enter a first Number :"))
b = int(input("Enter a second Number :"))
c = int(input("Enter a third Number :"))
if a>=b and a>=c:
    print(a, " is Largest Number")
elif b>=a and b>=c:
    print(b, "is Largest Number")
else:
    print(c,"is Largest Number")