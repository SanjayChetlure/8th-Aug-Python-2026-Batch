print("-----Ex1: Default Constructor------")


class Demo1:

    #default Constructor
    #use1: copy all the members of class into object
    # def __init__(self):
    #     constructor body

    def m1(self):
        print("Running non-static method from Demo1 class")

    def m2(self):
        print("Running non-static method from Demo1 class")


d1=Demo1()        #Object Creation -> constructor calling
d1.m1()
d1.m2()


# 1: d1 -> objectName   -> use to refer/identify an object
#2: Demo1()  -> className()  -> constructor calling  -> copy all the members of class into object



class Demo2:

    @staticmethod
    def m2():
        print("running static method")

Demo2.m2()


