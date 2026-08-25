print("---Print num from 1 to 5 without 3rd parameter---")

#start num:1
#end num: 5
#incr/decr: incr by 1

#Syntax:
# for variableName in range(startNum, endNum+1, incr/Decr(optional)):
#     print(variableName)

            #    6<6
for num in range(1,6):       #by default 3rd parameter =1
    print(num)                #1 2 3 4 5

print("----")
for i in range(20, 31):
    print(i)

print("----")
for i in range(5, 11):
    print(i)


print("---Print num from 1 to 5 with 3rd parameter---")
#                6<6
for num in range(1, 6, 1):
    print(num)         #1 2 3 4 5

print("----")
for i in range(20, 31,1):
    print(i)

print("----")
for i in range(5, 11,1):
    print(i)

print("------print even num from 2 to 10-----")
#             12<11
for i in range(2,11,2):
    print(i)             #2 4 6 8 10


print("------print table of 5-----")
for i in range(5,51,5):
    print(i)

print("------print table of 5-----")
for i in range(1,11):
    print(i*6)

print("------print square of num from 5 to 10 -----")
for i in range(5,11):
    print(i*i)

print("----print any message multiple times---")
#             6<6
for i in range(1,21):
    print("Hi")          #Hi Hi Hi Hi Hi


print("-----print num from 5 to 1-----")
#             0>0
for i in range(5, 0,-1):                  #startNum, emdNum-1, -1
    print(i)            #5 4 3 2 1


print("-----print num from 100 to 20-----")
for i in range(100, 19,-1):
    print(i)


print("-----print even num from 8 to 2-----")
#             0>1
for i in range(8, 1,-2):
    print(i)         # 8 6 4 2


print("-----print even num from 100 to 40-----")
for i in range(100, 39,-2):
    print(i)