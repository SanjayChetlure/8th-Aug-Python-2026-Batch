print("----Program without exception handling-----")


# num1=12
# num2=0
# num3=num1/num2    #10/0
# print(num3)
# print("Hi")
# print("Hello")



print("------Ex1.1: basic example of Exception handling-----")


n1=10
n2=0
try:
   n3=n1/n2   #10/0            #risky code
   print(n3)
except ZeroDivisionError:            #expected exception name
   print("ZeroDivisionError handled")              #msg in except block
print("Hi")
print("Hello")


print("------Ex1.2: Alternate code in except block-----")


n1=10
n2=0
try:
   n3=n1/n2   #10/0            #risky code
   print(n3)
except ZeroDivisionError:            #expected exception name
   print(n1/1)                       #Alternate code

print("Hi")
print("Hello")


print("------Ex1.3: Alternate code & msg in except block-----")


n1=10
n2=0
try:
   n3=n1/n2   #10/0            #risky code
   print(n3)
except ZeroDivisionError:
   print(n1/1)                         #Alternate code
   print("ZeroDivisionError handled")  #msg

print("Hi")
print("Hello")


print("------2: Example of Multiple Except block------")
n1=10
n2=0

try:
    print(n1/n2)
except ValueError:
    print("ValueError Handled")
except ZeroDivisionError:
    print("ZeroDivisionError Handled")

print("program ended")


print("-----------3.1: Example of Generic exception-----------")
n1=10
n2=0

try:
    print(n1/n2)          #risky code
except:                    #bydefault expectedExceptionName=Exception
    print("Generic exception handled")

print("program ended")

print("-----------3.2: Example of Generic exception-----------")
n1=10
n2=0

try:
    print(n1/n2)          #risky code
except Exception:
    print("Generic exception handled")

print("program ended")

print("-----------3.3: Example of Generic exception-----------")
n1=10
n2=0

try:
    print(n1/n2)          #risky code
except Exception as s1:
    print(s1)
    print("Generic exception handled")


print("program ended")


print("-----4: Example of Correct way of using Generic exception-------")
n1=10
n2=0

print("program started")
try:
   print(n1/n2)
except ValueError:
   print("Value Error Handled")
except ZeroDivisionError:
   print("ZeroDivisionError handled")
except Exception as e:
   print("Generic Exception handled")
   print(e)

print("program ended")





print("--------6: Example of finally block-------------")
a=10
b=0
div=0
try:
  div=a/b
except:
   print("Exception Handled")
finally:
   print("running finally block")


print(div)
print("Hi Hello")


print("------7: Throw exception using raise keyword-------")

age=15

if age<18:
    raise Exception("Age must be 18 or above")








