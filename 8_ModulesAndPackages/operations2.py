

print("-----Ex2: Examples of Modules (Apr2)----")

# from moduleName import fn1, clasName1
# from moduleName import fn1,fn2, clasName1,className2
# from moduleName import *

# fn()       #function calling
#
# obj1=className()       #object Creation
# obj1.methodName()      #non-static method calling
#
# # className.methodName()     #static method calling

from calculator1 import add,Demo1
from calculator2 import Demo2,sub

print("---Contents of module: calculator1--")
add(4,5)       #fn calling

d1=Demo1()                   #object creation
d1.m1()                      #non-static method calling
d1.m2()

Demo1.m3()                  #static method calling


print("---Contents of module: calculator2--")

sub(10,4)       #fn calling

d2=Demo2()                 #object creation
d2.m4()                   #non-static

Demo2.m5()                   #static method calling



