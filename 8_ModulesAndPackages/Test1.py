
#from packageName import moduleName

from Ex8_Packages2 import Test2, Test3


Test2.f1()           #fn calling
Test2.f2()

d5=Test2.Demo5()          #object creation
d5.m1()                   #non-static method calling


Test2.Demo5.m2()        #static method calling


print("----")

Test3.f3()
Test3.f4()