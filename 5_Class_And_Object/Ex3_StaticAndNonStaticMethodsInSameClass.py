print("-----Ex3: Static & non-static methods in same class------------")

class Demo3:
    def m1(self):
        print("running non-static method m1 from Demo3 class")

    def sqaureOfNum(self,num1):
        print("running non-static method sqaureOfNum from Demo3 class")
        print(num1*num1)

    @staticmethod
    def m2():
        print("running static method m2 from Demo3 class")

    @staticmethod
    def cubeOfNum(num1):
        print("running static method cubeOfNum from Demo3 class")
        print(num1*num1*num1)


#call non-static method
d3=Demo3()     #1: Create Object of class
d3.m1()        #2: method call
d3.sqaureOfNum(5)

#call static method
Demo3.m2()      #1: ClassName.methodName()
Demo3.cubeOfNum(5)

