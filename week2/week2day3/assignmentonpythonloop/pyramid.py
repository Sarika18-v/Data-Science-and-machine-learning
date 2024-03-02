def stringPyramid(_string , direction):
    new_string = ''
    _length = len(_string)
    if direction:
        for i in range(1, len(_string)+1):
            print(" " * (_length - i) , _string[:i] ," " * (_length-i))
    else:
        for i in range(len(_string) , 0 , -1):
            print(" " * (_length - i) , _string[:i] ," " * (_length-i))

_string = input("Enter a string")
direction = True
direction_input = input("Enter 'U' for Upward and 'D' for Downward")
if direction_input.lower() == 'u':
    drection = True
elif direction_input.lower() == 'd':
    direction = False
else:
    print("Invalid Command")
stringPyramid(_string, direction)