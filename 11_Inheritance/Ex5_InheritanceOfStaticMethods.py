
#Super class
class Test1:
    @staticmethod
    def m1():
        print("static method m1 from super class")


#Sub class
class Test2(Test1):
    @staticmethod
    def m2():
        print("static method m2 from sub class")

    # @staticmethod
    # def m1():
    #     print("static method m1 from super class")


Test2.m2()
Test2.m1()