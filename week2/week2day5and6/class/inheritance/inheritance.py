class Car:
    def __init__(self, tyres, doors):
        self.tyres=tyres
        self.doors=doors    
class Maruti(Car):
    def __init__(self, tyres, doors, window, engine_type):
        self.window=window
        self.engine_type=engine_type
        Car.__init__(self,tyres,doors)
    def display(self):
        print(self.tyres)
        print(self.doors)
        print(self.window)
        print(self.engine_type)
car1=Maruti(4,4,4,"petrol")
car1.display()