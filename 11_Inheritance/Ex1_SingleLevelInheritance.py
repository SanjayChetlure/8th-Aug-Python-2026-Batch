print("---Ex1: Single Level Inheritance----")


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


s=Son()
s.mobile()
s.car()
s.money()
s.home()