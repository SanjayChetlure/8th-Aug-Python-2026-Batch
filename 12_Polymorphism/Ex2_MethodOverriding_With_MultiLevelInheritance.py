print("---Ex2: Method Overriding With multi Level Inheritance---")


class GrandFather:
    def home(self):
        print("home: 3BHK")


class Father(GrandFather):
    def money(self):
        print("money: 1L")

    def home(self):           #Method Override
        print("home: 4BHK")


#sub/child class
class Son(Father):
    def mobile(self):
        print("mobile: Samsung S20 FE")

    def money(self):               #Method Override
        print("money: 2L")

    def home(self):               #Method Override
        print("home: 2BHK")


s=Son()
s.mobile()
s.home()
s.money()


