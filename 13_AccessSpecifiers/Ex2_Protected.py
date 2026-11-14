

class Parent:
    _salary = 50000          #protected -> access specifier

    def _display(self):       #protected -> access specifier
        print("Salary:", self._salary)


class Child(Parent):
    def show(self):
        print("Salary:", self._salary)


c = Child()
c.show()
