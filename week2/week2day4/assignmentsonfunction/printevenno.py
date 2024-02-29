#Q.8 Write a python function to print the even numbers from a given list.
def even(list):
    #enum a empty list to store even numbers.
    enum=[]
    #Iteration throughout the list
    for items in list:
        #checking if the number is divisible by 2 or not.
        if items%2==0:
            #If item is even append it to the enum
            enum.append(items)
    return enum
            
        #driving code
list=[1,3,90,21,22,80]
print(even(list))