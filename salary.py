import os
os.system("cls")
class Salary():
    def __init__(self):
        self.grossSalary=0 #bruto
        self.netSalary=0 #netto
    
    def askGross(self):
        self.grossSalary=float(input("Input Your Gross Salary: "))
        
class Spendings(Salary):
    def __init__(self):
        super().__init__()
        self.taxpercentage=0
        self.transportation=0
        self.livingExpenses=0
        self.investments=0
        self.otherExpenses=0
        self.totalSpendings=0
        self.monthlySavings=0
    
    def askInfo(self):
        self.taxpercentage=float(input("Input Your Income Tax Percentage: "))
        self.transportation=float(input("Input Your Monthly Transportation Expenses: "))
        self.livingExpenses=float(input("Input Your Monthly Living Expenses: "))
        self.investments=float(input("Input Your Monthly Investment Costs: "))
        self.otherExpenses=float(input("Input The Total Cost Of Remaining Expenses: "))
          
    def calculateNet(self):
        self.netSalary=self.grossSalary-(self.grossSalary/100*self.taxpercentage)
        return self.netSalary
        
    def calculateSpendings(self):
        self.totalSpendings=self.transportation+self.livingExpenses+self.investments+self.otherExpenses
        return self.totalSpendings
        
    def calculateSavings(self):
        self.monthlySavings=self.netSalary-self.totalSpendings
        return self.monthlySavings
                

user=Spendings()

user.askGross()
user.askInfo()

os.system("cls")
print(f"Your Monthly Net Income is: {user.calculateNet()}$\nYou're Spending {user.calculateSpendings()}$ Per Month\nYour Total Savings is {user.calculateSavings()}$")
