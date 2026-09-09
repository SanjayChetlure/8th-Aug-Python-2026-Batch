
class Student:

    collageName="Abc"          #class/static variable

    def __init__(self,studentName,studentRollNun):
        self.studentName=studentName                   #instance/non-static variable
        self.studentRollNun=studentRollNun


    def studentInfo(self):
        print("Student Name: ",self.studentName)
        print("Student Roll Num: ",self.studentRollNun)
        print("Student College Name: ",Student.collageName)

    @staticmethod
    def m1():
        print("Hi hello GM")


s1=Student("Amol",101)
s1.studentInfo()
print("--")
s2=Student("Akshay",102)
s2.studentInfo()

print("--")
Student.m1()



