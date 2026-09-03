print("-----Ex1.1: user defined without parameter constructor------")

class Demo2:

    #user defined constructor
    #use1: copy all the members of class into object
    def __init__(self):
        print("running user defined constructor")

    def m3(self):
        print("method m3 from Demo2 class")

    def m4(self):
        print("method m4 from Demo2 class")

d2=Demo2()     #constructor calling
d2.m3()
d2.m4()



print("---")


class Demo3:

    #user defined without parameter
    #use1: copy all the members of class into object
    #use2: initialize instance variable
    def __init__(self):
        self.num1=10            # instance/object variable
        self.num2=20

    def add(self):
        print(self.num1+self.num2)

    def mult(self):
        print(self.num1 * self.num2)

d3=Demo3()
d3.add()
d3.mult()





