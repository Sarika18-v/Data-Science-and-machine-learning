#Write a python program to check a list is empty or not.
def initial_list(values):
    for items in values:
        if len(items)==0:
            return 0
        else:
            return 1
values=[]
if initial_list(values):
    print("The string isnot empty")
else:
    print("The string is empty")

