print("-------Ex2: Example of static methods-------")


class Demo2:
    @staticmethod
    def m1():
        print("running static method m1 from Demo2 class")

    @staticmethod
    def m2():
        print("running static method m2 from Demo2 class")

    @staticmethod
    def findCubeOfNum(num1):
        print(num1*num1*num1)
        # num2=num1*num1*num1
        # print(num2)

#How to call static method
# className.methodName()
Demo2.m1()
Demo2.m2()
Demo2.findCubeOfNum(10)
Demo2.findCubeOfNum(5)

print("------")

class ArithmaticOperation:
    @staticmethod
    def add(num1, num2):
        print(num1+num2)

    @staticmethod
    def mult(num1, num2):
        print(num1*num2)

    @staticmethod
    def sub(num1, num2):
        print(num1-num2)

    @staticmethod
    def div(num1, num2):
        print(num1 / num2)


ArithmaticOperation.add(5,9)     #className.methodName(inp1, inp2)
ArithmaticOperation.add(8,9)
ArithmaticOperation.mult(9,15)
ArithmaticOperation.sub(2,7)
ArithmaticOperation.div(8,2)




