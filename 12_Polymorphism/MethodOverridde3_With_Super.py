
class Father:
    def home(self):
        print("home- 2BHK")

class Son(Father):
    def bike(self):
        print("bike- FZ V3")

    def home(self):
        super().home()                  #existing code
        print("home- 1BHK")             #new code

s=Son()
s.bike()
s.home()