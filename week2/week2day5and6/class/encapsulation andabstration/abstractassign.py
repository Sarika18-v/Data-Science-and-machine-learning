'''Create an abstract class named Shape with the following abstract methods:
area: to calculate the area of the shape.
perimeter: to calculate the perimeter of the shape.
display_info: to display information about the shape.
'''
import math
from abc import ABC,abstractmethod
class shape:
    @abstractmethod
    def calc_area(self):
        pass
    @abstractmethod
    def calc_perimeter(self):
        pass
    @abstractmethod
    def display_info(self):
        pass
'''Implement concrete classes for the following shapes, inheriting 
from the Shape class:
Circle: Representing a circle. It should take the radius as a parameter.
Rectangle: Representing a rectangle. It should take the 
length and width as parameters.
Triangle: Representing an equilateral triangle. 
It should take the side length as a parameter.'''
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def calc_area(self):
        return math.pi*self.radius*self.radius
    def calc_perimeter(self):
        return 2*math.pi*self.radius
    def display_info(self):
        print("Circle:")
        print(" Radius:", self.radius)
        print("Area:", self.calc_area())
        print("Perimeter:", self.calc_perimeter())
         
class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calc_area(self):
        return self.length*self.breadth
    def calc_perimeter(self):
        calc_perimeter=2*(self.length+self.breadth)
        return calc_perimeter
    def display_info(self):
        print("Rectangle:")
        print(" Length:", self.length)
        print(" Breadth:", self.breadth)
        print("Area:", self.calc_area())
        print("Perimeter:", self.calc_perimeter())
class triangle(shape):
    def __init__(self,length):
        self.length=length
    def calc_area(self):
        return (math.sqrt(3)/ 4)*(self.length * self.length)
    def calc_perimeter(self):
        return (3*self.length)
    def display_info(self):
        print("Triangle:")
        print("Side Length:", self.length)
        print("Area:", self.calc_area())
        print("Perimeter:", self.calc_perimeter())


circle = circle(7)
circle.display_info()
print("\n")

length = 5
breadth = 7
name="rectangle"
rectangle =rectangle(8,9)
rectangle.display_info()
print("\n")


triangle=triangle(8)
triangle.display_info()


