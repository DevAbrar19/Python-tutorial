class Student:


    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    @staticmethod
    def average():
        print("working")

    # def hello(self):
    #     print("Welcome", self.name)

    # def getMarks(self):
    #     return self.marks
    
    # def setMarks(self, marks):
    #     self.marks = marks
    

s1 = Student("Ajwad Abrar", 20, 10 ,20)
Student.average()
# print(s1.name, s1.marks)
# s1.hello()
# print(s1.getMarks())
# s1.setMarks(10)
# print(s1.getMarks())
