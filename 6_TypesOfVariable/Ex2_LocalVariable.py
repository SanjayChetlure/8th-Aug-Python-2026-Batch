print("------Ex2: local variable--------")

def f1():
    num1=10          #local variable
    print(num1)

def f2(num2):          #local variable
    print(num2)
    # print(num1)

class Test2:
    def m1(self):
        num3=30          #local variable
        print(num3)

    def m2(self,num4):      #local variable
        print(num4)
        # print(num3)

    @staticmethod
    def m3():
        num5=50               #local variable
        print(num5)

    @staticmethod
    def m4(num6):            #local variable
        print(num6)
        # print(num5)


f1()
f2(20)

t2=Test2()
t2.m1()
t2.m2(40)

Test2.m3()
Test2.m4(60)





