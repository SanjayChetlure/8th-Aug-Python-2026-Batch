

class Demo4:

    #user defined with 2 parameter constructor
    #use1: copy all the members of class into object
    #use2: initialize instance variable
    def __init__(self,a,b):
        self.num1=a            # instanceVariable=localVariable
        self.num2=b

    def add(self):
        print(self.num1+self.num2)

    def mult(self):
        print(self.num1 * self.num2)



d3=Demo4(10,20)
d3.add()
d3.mult()

print("--")

d4=Demo4(50,60)
d4.add()
d4.mult()

print("--")

d5=Demo4(4,6)
d5.add()
d5.mult()