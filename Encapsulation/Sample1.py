

class Demo2:

   def __init__(self):
       self.__num1=10       #private variable
       self.__num2=20
       self.__num3=20

   def add(self):
       print(self.__num1+self.__num2+self.__num3)

   def mult(self):
       print(self.__num2 * self.__num3)

   def squareOfNum(self):
       print(self.__num3*self.__num3)

d2=Demo2()
d2.add()
d2.mult()
d2.squareOfNum()

# print(d2.num1) # This will raise an AttributeError since num1 is private


