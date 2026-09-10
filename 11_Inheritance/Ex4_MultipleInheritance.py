print("---Ex4: Multiple Inheritance----")

#super class 1
class Father:
    def car(self):
        print("Car: BMW")

    def home(self):
        print("home: 3BHK")

#super class 2
class Mother:
    def money(self):
        print("money: 1L")


#sub class
class Son(Father,Mother):
    def bike(self):
        print("bike Yamaha FZ v3")

    # def car(self):
    #     print("Car: BMW")
    #
    # def home(self):
    #     print("home: 3BHK")
    #
    # def money(self):
    #     print("money: 1L")

s=Son()
s.bike()
s.car()
s.home()
s.money()


