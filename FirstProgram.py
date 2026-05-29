class Employee:
    def __init__(self, role, dept, sal):
        self.role = role
        self.dept = dept
        self.sal = sal
    
    def showDetails(self):
        print(self.role)
        print(self.dept)
        print(self.sal)

class Engineer(Employee):
    def __init__(self, role, dept, sal, name, age):
        super().__init__(role, dept, sal)
        self.name = name
        self.age = age

e = Engineer("IT", "CSE", 5000, "Ajwad", 20)
e.showDetails()
print(e.name)
print(e.age)