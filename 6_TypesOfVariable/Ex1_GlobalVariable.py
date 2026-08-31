print("------Ex1: Global variable--------")

num1=10      #Global variable

def f1():
    print("Running f1",num1)                  #variableName

def f2():
    print("Running f2",num1)


class Test1:

    def m1(self):
        print("Running non-static method m1 from Test1 class",num1)

    @staticmethod
    def m2():
        print("Running static method m2 from Test1 class",num1)


f1()
f2()

t1=Test1()
t1.m1()

Test1.m2()




