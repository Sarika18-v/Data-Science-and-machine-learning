#Q.3 Write a python function to find factorial of a given non negativenumber
def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial*= i
    return factorial
num=3
print(factorial(num))
