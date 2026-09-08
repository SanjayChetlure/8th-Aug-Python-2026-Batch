

def f1():
    print("running f1 from Sample1 module")

def add():
    num1=10
    num2=20
    print(num1+num2)


class Demo1:

    def m1(self):
        print("Running method m1 from Sample1-Demo5 class ")

    @staticmethod
    def m2():
        print("Running method m2 from Sample1-Demo5 class ")


f1()
add()

d1=Demo1()
d1.m1()

Demo1.m2()