print("-------Ex1: Example of non- static methods-------")


class Demo1:            #class declaration
    #non-static
    def m1(self):         #method declaration
        print("running method m1")

   #non-static method
    def findSquareOfNum(self,num1):
        print(num1*num1)

#non-static method call
#1: Create Object of class
#2: method call
# objectName=className()
# objectName.methodName()
d1=Demo1()                #1: object creation
d1.m1()                   #2: method calling
d1.findSquareOfNum(5)
d1.findSquareOfNum(6)

print("------")

class ArithmaticOp:
    def add(self,num1, num2):
        num3=num1+num2
        print(num3)

    def mult(self, num1, num2):
        num3 = num1 * num2
        print(num3)

    def sub(self, num1, num2):
        num3 = num1 - num2
        print(num3)

    def div(self, num1, num2):
        num3 = num1 / num2
        print(num3)

d2=ArithmaticOp()      #contructor
d2.add(7,8)
d2.mult(7,8)
d2.sub(60,40)
d2.div(80,2)
d2.div(50,2)

print("---")
d3=ArithmaticOp()
d3.add(2,7)








