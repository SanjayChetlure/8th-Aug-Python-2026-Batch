
print("---Ex6: Default or Optional Parameter---")

def studentDetails(name, age=10):
    print("Student Name: ",name)
    print("Student Age:",age)


studentDetails("Amol")
studentDetails("Amol",20)


print("---------")

def studentDetails1(name="Amol", age=10):
    print("Student Name: ",name)
    print("Student Age:",age)


studentDetails1()
studentDetails1("Rahul")
studentDetails1("Ganesh",20)