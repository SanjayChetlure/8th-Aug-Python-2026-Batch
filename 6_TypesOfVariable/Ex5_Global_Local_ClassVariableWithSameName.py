print("----Ex5_Global_Local_Class Variable With Same Name---")


a,b=10,20        #global variable

class Test5:

    a,b=30,40        #class variable

    def add(self):
        a,b=50,60         #local variable
        print(a+b)                               #local variable calling
        print(self.a+self.b)                     #class variable calling
        print(globals()['a']+globals()['b'])     #global variable calling



t5=Test5()
t5.add()
