

class Student:
    name = "Rahul"                #public -> access specifier

    def display(self):            #public -> access specifier
        print("Name:", self.name)

s = Student()
print(s.name)
s.display()
