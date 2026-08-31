print("---Ex3: Class Variable------")

class Test3:

    num1=10           #class variable

    def m1(self):
        print(self.num1)        #currentClassObjectName(self).variableName

    @staticmethod
    def m2():
        print(Test3.num1)       #currentClassName.variableName



t3=Test3()
t3.m1()
print(t3.num1)         #objectName.variableName


Test3.m2()


