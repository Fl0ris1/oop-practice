class School:
    def __init__(self,name):
        self.name=name
        
    def showname(self):
        print(f"Hi my name is {self.name}")

class Student(School):
    def __init__(self, name, age, grade, group):
        super().__init__(name)
        self.age=age
        self.grade=grade
        self.group=group

    def showinfo(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}\nGroup: {self.group}")

student=Student("Floris", "14", "2", "D")
student.showname()
student.showinfo()