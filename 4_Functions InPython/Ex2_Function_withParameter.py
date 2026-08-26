print("------Ex2: function without parameter--------")

#With 2 parameter function
def add(num1,num2):    #num1=4, num2=5
    num3=num1+num2
    print(num3)

add(10,20)
add(4,5)
add(9,18)


print("---")

def studentDetails(fn,ln):
    print(fn, ln)

studentDetails("amol","patil")
studentDetails("ganesh","patil")


print("---")

def studentInfo(name,rollNum,per,grade):
    print("studnet Name: ",name)
    print("student roll num: ",rollNum)
    print("Student percentage: ",per)
    print("Student grade: ",grade)

studentInfo("Amol",101,65.1,"A")
studentInfo("ganesh",102,78.1,"A")
