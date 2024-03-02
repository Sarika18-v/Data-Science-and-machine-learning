'''Objective
Create a set of classes representing different animals, introducing multiple 
levels of inheritance and abstract classes.
Requirements
Create an abstract class called Animal with abstract methods:
speak: Abstract method representing the sound the animal makes.
move: Abstract method representing how the animal moves.
eat: Abstract method representing what the animal eats.
Implement three concrete classes: Mammal, Bird, and Fish, 
inheriting from the Animal class. Implement the abstract methods accordingly.
Create concrete classes for specific animals within each category:
For Mammal: Implement classes like Dog and Cat.
For Bird: Implement classes like Eagle and Penguin.
For Fish: Implement classes like Salmon and Goldfish.
Add unique methods for each specific animal:
For example, bark for Dog, fly for Eagle, swim for Salmon.
Demonstrate the usage of these classes by creating instances and calling 
various methods.
'''
from abc import ABC , abstractmethod

class Animal(ABC):

    def __init__(self ,name, sound , movement , food ):
        self.sound = sound
        self.name = name 
        self.movement = movement
        self.food = food
        
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def eat(self):
        pass
class Mammal(Animal):
    def __init__(self, name , sound, movement ,food):
        super().__init__(name,sound, movement ,food)

    def speak(self):
        print(f"{self.name} make {self.sound}. ")

    def move(self):
        print(f"{self.name} can {self.movement}. ")

    def eat(self):
        print(f"{self.name} eat {self.food}. ")


mammal = Mammal("Mammals","sound" , "walk" , "food")
mammal.speak()
mammal.move()
mammal.eat()

print("\n")
class Bird(Animal):
    def __init__(self ,name, sound , movement , food):
        super().__init__(name,sound, movement , food)
        

    def speak(self):
        print(f"{self.name} can make {self.sound}")

    def move(self):
        print(f"{self.name} can  {self.movement}")

    def eat(self):
        print(f"{self.name} eat {self.food}")

birds = Bird("Birds","sound" , "fly","insect")
birds.speak()
birds.move()
birds.eat()

print("\n")
class Fish(Animal):
    def __init__(self ,name, sound , movement , food):
        super().__init__(name,sound, movement , food)
        

    def speak(self):
        print(f"{self.name} can make {self.sound}")

    def move(self):
        print(f"{self.name} can  {self.movement}")

    def eat(self):
        print(f"{self.name} eat {self.food}")

fish = Fish("Fish","sound" , "swim","insect")
fish.speak()
fish.move()
fish.eat()
print ("\n")
      
class Dog(Mammal):
    def __init__(self, sound):
        super().__init__("Dog","bark", "run", "dog food")
        self.sound = sound

    def bark(self):
        print(f"The Dog {self.sound} when see unknown")
        

class Cat(Mammal):
    def __init__(self):
        super().__init__("Cat","meow","jump","fish")

class Eagle(Bird):
    def __init__(self, high):
        self.high = high
        super().__init__("Eagle","chow","fly","snake")

    def fly(self):
        print(f"Eagle {self.high} high in sky ")

class Penguin(Bird):
    def __init__(self):
        super().__init__("Penguin","quack","walk","fish")

class Salmon(Fish):
    def __init__(self, under_water):
        self.under_water = under_water
        super().__init__("Salmon","jujuju","swim","insect")

    def swim(self):
        print(f"Salmon swmin {self.under_water} under water")

class GoldFish(Fish):
    def __init__(self):
        super().__init__("GoldFish","shhhhhhh","swim","insect")
cat = Cat()
dog = Dog("bark")
eagle = Eagle("fly")
penguin = Penguin()
salmon = Salmon("swim")
goldFish = GoldFish()


dog.speak()
dog.eat()
dog.bark()
dog.move()
print("\n")
cat.speak()
cat.eat()
cat.move()
print("\n")
eagle.speak()
eagle.eat()
eagle.fly()
eagle.move()
print("\n")
penguin.speak()
penguin.eat()
penguin.move()
print("\n")
salmon.speak()
salmon.eat()
salmon.swim()
salmon.move()
print("\n")
goldFish.speak()
goldFish.eat()
goldFish.move()