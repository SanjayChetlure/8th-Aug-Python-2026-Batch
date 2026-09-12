print("----Example1 of method overloading----")

class ArithmaticOperation:

    # def add(self,num1,num2):
    #     print(num1+num2)
    #
    # def add(self,num1,num2, num3):
    #     print(num1+num2+num3)
    # def add(self,num1,num2, num3,num4):
    #     print(num1+num2+num3+num4)


    def add(self, num1=0, num2=0, num3=0,num4=0):
        print(num1+num2+num3+num4)



a=ArithmaticOperation()
a.add()
a.add(10,20)
a.add(10,20,30)
a.add(10,20,30,40)



print("----Example2 of method overloading----")


class Sample2:

    # def printName(self):
    #     name="abc"
    #     print(name)
    #
    # def printName(self,name):
    #     print(name)

  def printName(self,name="xyz"):
      print(name)


s=Sample2()
s.printName()
s.printName("Mahesh")





