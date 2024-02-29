#2.Write a python function to reverse a string
#initializing function
def reverse_string(string):
    #Slice
    string=string[::-1]
    return string
#driving code
a = "sarikapokhrel"
 
print("The original string is : ", end="")
print(a)
 #function calling
print("The reversed string is : ", end="")
print(reverse_string(a))