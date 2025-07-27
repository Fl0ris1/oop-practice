from clear_screen import clear
class Student:
    def __init__(self):
        self.name=""
        self.year=""
    def askInfo(self):
        self.name=input("Input Your Name: ")
        self.year=input("Input Your Year: ")

    def showInfo(self):
        print(f"Name: {self.name}\nYear: {self.year}")

class AllDetails(Student):
    def __init__(self):
        super().__init__()
        self.mark1=0
        self.mark2=0
        self.mark3=0
        self.total=0
        self.average=0
    
    def askDetails(self):
        self.mark1=int(input("Input Your Mark for Maths: "))
        self.mark2=int(input("Input Your Mark for Biology: "))
        self.mark3=int(input("Input Your Mark for Science: "))

    def calc(self):
        self.total=self.mark1+self.mark2+self.mark3
        self.average=self.total//3

    def showDetails(self):
        clear()
        print(f"Your Total is: {self.total}\nYour Average is: {self.average}")
        if self.average==10:
            print("Excellent")

        elif self.average==9:
            print("Very Good")
            
        elif self.average==8:
            print("Good")

        elif self.average==7:
            print("Above Average")

        elif self.average==6:
            print("Satisfactory")

        elif self.average<=5:
            print("Failing")
        
student1=AllDetails()
student1.askInfo()
student1.askDetails()
student1.calc()
student1.showDetails()