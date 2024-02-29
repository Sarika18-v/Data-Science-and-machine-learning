#Write a python function to multiply all the numbers in a list
#initializing function
def calc_product(list):
    multiply=1
    #iteration
    for items in list:
        multiply*=items
    return multiply
#driving code
list=([1,2,3,4])
result=calc_product(list)
print(result)


