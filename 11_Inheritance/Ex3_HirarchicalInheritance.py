print("---Ex3: Hirarchical Inheritance----")


#super/parent/base class
class Father:
    def car(self):
        print("Car: BMW")

    def money(self):
        print("money: 1L")

    def home(self):
        print("home: 3BHK")

#sub class1
class Son1(Father):
    def bike(self):
        print("bike: YAMAHA FZ V3")

    # def car(self):
    #     print("Car: BMW")
    #
    # def money(self):
    #     print("money: 1L")
    #
    # def home(self):
    #     print("home: 3BHK")

#sub class2
class Son2(Father):
    def laptop(self):
        print("Laptop: HP Envy")

    # def car(self):
    #     print("Car: BMW")
    #
    # def money(self):
    #     print("money: 1L")
    #
    # def home(self):
    #     print("home: 3BHK")


print("----Features of Sub class 1---")
s1=Son1()
s1.car()
s1.money()
s1.home()
s1.bike()

print("----Features of Sub class 2---")
s2=Son2()
s2.car()
s2.money()
s2.home()
s2.laptop()
