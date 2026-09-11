
class Demo1:

    num1=10     #class Variable

    def m1(self):
        print("method m1 from super class")

class Demo2(Demo1):

    num2=20     #class variable

    def m2(self):
        print("method m2 from sub class")
        print(self.num1+self.num2)

d2=Demo2()
d2.m1()
d2.m2()



