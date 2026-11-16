student ={
    "name" :"Snehal",
    "age" : 21,
    "city" : "Karjat",
    "marks" : "83",
}
print("All Keys")
print(student.keys())

student["college"] = "VIIT"
print("After adding new pair")
print(student)

del student["age"]
print("After deleting age")
print(student)

student["city"] = "pune"
print("After modifying city")
print(student)