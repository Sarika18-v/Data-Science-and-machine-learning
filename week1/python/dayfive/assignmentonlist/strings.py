#Write a Python program to count the number of strings where the string length is 2 or more
#and the first and last character are same from a given list of strings.
#Input: sample_list = ['abc', 'xyz', 'aba', '1221']`  
#output: str_count = 2`
# Define a function called simple_list that takes a list of words 'words' as input
def simple_list(words):
    #Initializing counter to track of simple list 
    ctr=0
    for item in words:
        #Condition checking
        if len(item) > 2 and item[0] == item[-1]:
          # If the condition is met, increment the counter 'ctr'  
            ctr += 1
            #return counter
    return ctr
#call the function with list as an input
print(simple_list(['abc', 'xyz', 'aba', '1221']))

