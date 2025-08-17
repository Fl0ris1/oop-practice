import os
os.system("cls")

class Rectangle():
    def __init__(self):
        self.length=0
        self.width=0
        self.perimiter=0
        self.area=0
        
    def askLW(self):
        self.length=float(input("How Much Units Is The Length Of Your Rectangle?\n"))
        self.width=float(input("How Much Units Is The Width Of Your Rectangle?\n"))
        
    def calculatePerimiter(self):
        self.perimiter=(self.length+self.width)*2
        
    def calculateArea(self):
        self.area=self.length*self.width
        
        
    
rectangle1=Rectangle()

rectangle1.askLW()
rectangle1.calculatePerimiter()
rectangle1.calculateArea()

os.system("cls")

print(f"The Perimiter Of  Your Rectangle Is {rectangle1.perimiter} Units\nThe Area of Your Rectangle Is {rectangle1.area} Units")