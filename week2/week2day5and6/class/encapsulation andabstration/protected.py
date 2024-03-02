#for protected class we use only a underscore before the attribute 
class Person:
    """protected access"""
    def __init__(self,name,age):
        self._name=name
        self._age=age
class Ram(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
    def display(self):
        print(f"The person {self._name} is {self._age}years old")
if __name__=="__main__":
    person_test=Ram(name="Ram",age=22)
    person_test.display()