# Module1: Operations

# Syntax:
# import moduleName

# moduleName.fn()            #fn calling

# objName=moduleName.className()          #calling non-static method
# objName.methodName()

#moduleName.className.methodName()        #calling static method


import calculator1
import calculator2

print("------contents of Calculator1 module-----")
calculator1.add(2,3)       #fn calling
calculator1.add(7,8)
calculator1.mult(4,5)

d1=calculator1.Demo1()                #object creation
d1.m1()                               #method calling
d1.m2()
d1.m2()

calculator1.Demo1.m3()             #calling static method
calculator1.Demo1.m3()


print("------contents of Calculator2 module-----")


calculator2.div(6,2)             #fn calling
calculator2.sub(90,40)

d2=calculator2.Demo2()                       #object creation
d2.m4()                                      #non-static method calling

calculator2.Demo2.m5()                      #static method calling

