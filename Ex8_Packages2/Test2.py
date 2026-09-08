
def f1():
    print("Running function f1 2nd package")


def f2():
    print("Running function f2 2nd package")


class Demo5:

    def m1(self):
        print("Running non-static method m1 from 2nd package - Demo5 class")


    @staticmethod
    def m2():
        print("Running static method m2 from 2nd package - Demo5 class")

