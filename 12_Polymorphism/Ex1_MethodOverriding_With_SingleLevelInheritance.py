print("---Ex1: Method Overriding With Single Level Inheritance---")

#super/parent/base class
class Father:
    def car(self):
        print("Car: BMW")

    def money(self):
        print("money: 1L")

    def home(self):
        print("home: 3BHK")


#sub/child class
class Son(Father):
    def mobile(self):
        print("mobile: Samsung S20 FE")

    def car(self):            #Method Override
        print("Car: Kia")

    def money(self):          #Method Override
        print("money: 1.5L")

    # def home(self):
    #     print("home: 3BHK")


print("---Features of super class(Original data)--")
f=Father()
f.car()
f.money()
f.home()

print("---Features of sub class (Updated data)--")
s=Son()
s.mobile()
s.car()
s.money()
s.home()