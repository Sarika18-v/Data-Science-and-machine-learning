#Q.7 Write a Python function that takes a number as a parameter and check the number is prime or not
def prime(number):
    #checking if number is equal to 1
    if number==1:
        return False
    #checking if number is equal to 2
    elif number==2:
        return True
    else:
        #Using x as a iterator between 2 and n-1
        for x in range(2,number):
            #checking if the number is divided by any other number between 2 and n-1 or not
            if number%x ==0:
                return False
            else:
                return True
#driving code
number=98
print(prime(number))
