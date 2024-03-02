'''Create a base class called Vehicle with the following attributes:
make: Make of the vehicle (e.g., Ford, Honda).
model: Model of the vehicle (e.g., Civic, F-150).
year: Year of manufacture.
fuel_type: Type of fuel the vehicle uses (e.g., Gasoline, Electric).'''
class vehicle:
    def __init__(self,maker,model,mfd_year,fuel_type):
        self.maker=maker
        self.model=model
        self.mfdyear=mfd_year
        self.fuel_type=fuel_type
    def make(self):
            print(f"The maker is {self.maker}")
    def modelno(self):
            print(f"model of car is {self.model}")
    def year(self):
            print(f"manufactured in {self.mfdyear}")
    def fueltype(self):
            print(f"The type of car is {self.fuel_type}")
    def call(self):
        self.make()
        self.modelno()
        self.year()
        self.fueltype()
'''Create two subclasses: Car and Truck, inheriting from the Vehicle class. 
Implement the __init__ method using super().__init__ to initialize attributes 
from the parent class.'''
class Car(vehicle):
    def __init__(self,make,model,year,fuel_type):
        super().__init__(make,model,year,fuel_type)
class Truck(vehicle):
    def __init__(self,make,model,year,fuel_type):
        super().__init__(make,model,year,fuel_type)
'''Create a subclass of Car called ElectricCar. Add an additional attribute:
battery_capacity: Capacity of the electric car's battery in kWh.
Create a subclass of Truck called HybridTruck. Add an additional attribute:
electric_motor_power: Power of the electric motor in the hybrid truck.
Demonstrate the usage of these classes by creating instances and 
displaying information about the vehicles.'''
class ElectricCar(Car):
    def __init__(self,make,model,year,fuel_type,battery_capacity):
        self.battery_capacity=battery_capacity
        super().__init__(make,model,year,fuel_type)
    def battery(self):
        print(f"Battery capacity is {self.battery_capacity}")
class HybridTruck(Truck):
    def __init__(self,make,model,year,fuel_type,electric_motor_power):
        self.power=electric_motor_power
        super().__init__(make,model,year,fuel_type)
    def powerw(self):
        print(f"Battery capacity is {self.power}")
ecar=ElectricCar("Honda","E 23","2011","Petrol","80 kwh")
ecar.call()
ecar.battery()
Htruck=HybridTruck("TATA","s 23","2089","Diesel","800 rpm")
Htruck.call()
Htruck.powerw()


        
        
