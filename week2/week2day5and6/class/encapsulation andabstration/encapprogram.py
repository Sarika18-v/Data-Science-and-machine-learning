#FOR PRIVATE YOU HAVE TO USE double UNDERSCORE BEFORE THE ATTRIBUTE
class Person:
    """private access"""
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def display(self):
        print(f"The person {self.__name} is {self.__age}years old")
if __name__=="__main__":
    person_test=Person(name="Ram",age=22)
    person_test.display()
