class Car:
    def __init__(self, brand, model, color):
        self.brand=brand
        self.model=model
        self.color=color

    def showgeninfo(self):
        
        print(f"color: {self.color}\nbrand: {self.brand}\nmodel: {self.model}")

class carInfo(Car):
    def __init__(self, brand, model, color, mileage, year, engine):
        super().__init__(brand, model, color)
        self.mileage=mileage
        self.year=year
        self.engine=engine

    def showadinfo(self):
        print(f"mileage: {self.mileage}\nyear: {self.year}\nengine: {self.engine}")


carinfo=carInfo("Toyota", "Supra", "Red", "5", "1982", "2.8-liter 12-valve DOHC")

carinfo.showgeninfo()
carinfo.showadinfo()