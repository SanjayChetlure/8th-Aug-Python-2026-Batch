print("---Ex4_Global_Local_Class_VariablesInSameExample.py----")

num1=10         #global variable

def f1():
    num2=20           #local variable
    print(num1)           #calling global variable
    print(num2)           #calling local variable

def f2(num2):          #local variable
    print(num1)           #calling global variable
    print(num2)           #calling local variable

class Test4:
    num3=30
    def m1(self):
        num2=20
        print(num1)          #calling global variable
        print(num2)          #calling local variable
        print(self.num3)     #calling class variable

    @staticmethod
    def m2():
        num2=20
        print(num1)          #calling global variable
        print(num2)          #calling local variable
        print(Test4.num3)    #calling class variable


f1()
f2(50)
print("---")

t4=Test4()
t4.m1()

print("---")

Test4.m2()



