print("------Ex3.1: function with single value return type------")


def add(num1, num2):
    num3=num1+num2
    return num3

num4=add(10,20)
print(num4)

print(add(5,6))


print("------")

def getStudentName():
    name="Amol"
    return name

s1=getStudentName()
print(s1)

print(getStudentName())



print("------Ex3.2: function with multiple value return type------")

def arithmaticOperation(n1, n2):
    add=n1+n2
    mult=n1*n2
    return add,mult

n3,n4=arithmaticOperation(10,20)
print(n3)
print(n4)


print(arithmaticOperation(4,5))


