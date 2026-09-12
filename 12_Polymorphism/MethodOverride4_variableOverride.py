
print("-----Ex4.1 - Variable override------")
#Super class
class Parent:
    num=10


#sub class
class child(Parent):
    num=20             #variable override

    def m1(self):
        print(self.num)

c=child()
c.m1()




print("-----Ex4.2 - Variable override with super------")
#Super class
class Parent1:
    num=10

#sub class
class child1(Parent1):
    num=20             #variable override

    def m1(self):
        print(super().num)           #calling super class variable
        print(self.num)              #sub/overrided  class


c1=child1()
c1.m1()