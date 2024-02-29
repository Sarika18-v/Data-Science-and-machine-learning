#Write a python program to insert a given string at the beginning of all items in a list.**
  #`sample_list = [1, 2, 3, 4]`  `str_to_inser = "emp"`  `output_list = ['emp1', 'emp2', 'emp3', 'emp4']`

num = [1, 2, 3, 4]

# use of list comprehension i.e enemurate
# This effectively generates a list of strings with elements like 'emp1', 'emp2', 'emp3', 'emp4'
new_list = ['emp{0}'.format(i) for i in num]

# Print the new list 'new_list' containing the formatted strings
print(new_list)
